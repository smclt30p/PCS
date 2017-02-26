from base64 import b64decode
from re import findall, compile
from core.Constants import *
import demjson
import requests
from bs4 import BeautifulSoup

from core.plugins.Plugin import Plugin, PluginException, Playable, DataStream, SubtitleStream

class PluginImpl(Plugin):

    version = "1.0.0_02252017"
    name = "Putlocker"
    author = "PCS Team"
    description = "Putlocker.is plugin for PCS"
    id = 0

    HIDDEN_DATA_REGEX = compile("<script.*>document.write\(doit\(\'([A-Za-z0-9s]+)\'\).+</script>")

    def search(self, query):

        playables = [] # Playable[]

        index = 1
        total = None

        while True:

            try:

                # The search consists of multiple pages, indexed
                # by a number in the URI parameter "page"
                request = requests.get("http://putlocker.is/search/search.php?q=" + query + "&page=" + str(index))

                # housekeeping
                if request.status_code != 200:
                    raise PluginException("Request rejected")

                soup = BeautifulSoup(request.text, "lxml")

                # if the page contains the "Sorry" text,
                # that probably means that the search returned
                # no results, return the empty list
                if "Sorry" in request.text:
                    return playables

                # set up the total page count
                if total is None:

                    # This is probable the biggest hack ever. This returns
                    # the number of pages under the search results, based on
                    # the number inside the last button

                    # find all tables on the website
                    tables = soup.find_all("table")

                    # usually there are 7 tables, and there
                    # is 6 tables if there is no pager,
                    # which means there is only one page
                    # of results
                    if len(tables) == 6:
                        total = 1
                    else:

                        # from the second-to-last table (pager),
                        # get the second-to-last coll
                        # (button before "Next") and parse the number
                        # inside of the button to get the number of
                        # total pages
                        total = int(soup.find_all("table")[-2].find_all("td")[-2].text)

                        # if the search query is too broad (for ex. "a")
                        # we would need to make a lot of requests to the
                        # server stressing the server for nothing.
                        # We limit the number of pages to 20
                        if total > 20:
                            # there is 20 movies per page ( 4 rows, 5 colls )
                            res = total * 4 * 5
                            raise PluginException("Search too broad! ({} results)".format(res))

                # the page consists of tables, and the movie
                # search results are a table in themself
                table_root = soup.find_all("table", class_="table")

                # there should be 2 tables, suggested videos
                # and the search results
                if len(table_root) != 2:
                    raise PluginException("Invalid server response for search!")

                # the second table is the results,
                # and the results are just table data
                table_root = table_root[1]
                table_root = table_root.find_all("td")

                # for each movie grab the poster,
                # the link where it points to and
                # the movie title
                for item in table_root:

                    tempPlayable = Playable()
                    tempPlayable.setTitle(item.a.attrs.get("title"))
                    tempPlayable.setPoster(item.a.img.attrs.get("src"))
                    tempPlayable.putlockerReflink = item.a.attrs.get("href")
                    # important for metadata
                    tempPlayable.setParentPluginId(self.id)
                    playables.append(tempPlayable)

                # increment search result index
                index += 1

                # reached last search page
                if index > total:
                    break

            except BaseException as e:
                raise PluginException(str(e))

        return playables

    def fetchPlayableMetadata(self, playable):

        streams  = [] # DataStream[]
        subtitles = [] # SubtitleStream[]
        # not needed, populated by search
        # posterUrl = None
        description = None
        movieLength = 0

        try:

            # Fetch the HTML page of the movie
            # This downloads the html from links like
            # http://putlockers.ch/watch-game-of-thrones-tvshow-online-free-putlocker.html
            html = requests.get(playable.putlockerReflink)
            if html.status_code != 200:
                raise PluginException("Request rejected")

            # The link to the next piece of the puzzle is hidden
            # in base64 on the site, in a method called doit()
            # This regexes out all the doit() calls on the page
            doit_calls = findall(self.HIDDEN_DATA_REGEX, html.text)
            # forward declare to calm compiler and improve error
            # detection
            iframe_html = None

            # search through the doit() hidden data, searching
            # for a iframe containing the embedding link
            for item in doit_calls:
                decoded_data = b64decode(b64decode(item))
                if TAG_IFRAME in str(decoded_data):
                    iframe_html = str(decoded_data).strip("'b")
                    break

            if iframe_html is None:
                raise PluginException("TV Series from Putlocker not supported yet.")

                # todo: if there is no iframe, its a tv series with episodes

            soup = BeautifulSoup(html.text, "lxml")

            # get some basic metadata
            for item in soup.find_all("strong"):
                if "Synopsis" in item.text:
                    description = item.parent.text

            # The iframe contains a link to the embed
            # html file, that has the necessary stream info
            # this snippet parses the received html
            # and extract's the iframe's src data that looks like this:
            # http://thevideos.tv/embed-tj7e3i7rf6xu-728x410.html
            # We are leaving putlocker at this stage and entering
            # thevideos.tv namespace.
            soup = BeautifulSoup(iframe_html, "lxml")
            element = soup.find_all("iframe")[0]
            attr = element.attrs.get("src")

            # download the embed html
            raw_html = requests.get(attr)

            # housekeeping
            if raw_html.status_code != 200:
                raise PluginException("iframe source fetch rejected!")

            # the embed html contains a jwplayer("vplayer").setup() call
            # that takes a json object as a parameter.
            # that json is crucial for us, it contains links for streams,
            # links to subtitles, movie length etc.
            result = ""

            # locate the index of the function call inside the html
            index = raw_html.text.find("setup(", 0) + len("setup(")
            end = len(raw_html.text) - index

            # parse from the html from the opening bracket of
            # the setup call to the closing one. JSON data is invalid
            # if there is a closing bracket there, so watch for that
            for i in range(index, end):
                if raw_html.text[i] == ')':
                    break
                result += raw_html.text[i]

            # serialize json into a dict and return
            json_instance = demjson.JSON()
            json_instance = json_instance.decode(result)

            for source in json_instance["sources"]:

                dataStream = DataStream()
                dataStream.setLabel(source["label"])
                dataStream.setSource(source["file"])
                streams.append(dataStream)

            for track in json_instance["tracks"]:

                sub = SubtitleStream()
                sub.setLabel(track["label"])
                sub.setSource(track["file"])
                subtitles.append(sub)

            movieLength = int(json_instance["duration"])

        except BaseException as e:
            raise PluginException(str(e))

        playable.setDataStreams(streams)
        playable.setSubtitleStreams(subtitles)
        # not needed, populated by search
        # playable.setPoster(posterUrl)
        playable.setDescription(description)
        playable.setPlayableLength(movieLength)