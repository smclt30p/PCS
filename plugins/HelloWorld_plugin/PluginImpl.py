from core.plugins.Plugin import Plugin, PluginException, Playable, DataStream, SubtitleStream


"""
This is a skeleton for a PCS plugin. Read the comments
CAREFULLY. This plugin works fine inside PCS, try it.

Rules:

0) The ID must be a UNIQUE int. And 0xCAFEBABE is NOT
unique.
1) The plugin file must only contain one class, called
"PluginImpl" and it must inherit plugin.
2) The PluginImp class must override 2 methods, search()
and fetchPlayableMetadata()
3) The search method must return an array of playables
4) Each item in the playable list must contain a Playable
object that has a title and a ID that is always self.id

All the work is performed inside a worker thread.
To test this plugin, import it into PCS and search for
"hello world".

"""
class PluginImpl(Plugin):

    version = "1.0"
    name = "Hello World"
    author = "PCS Team"
    description = "Hello World demonstration plugin for PCS"
    id = 1

    # todo: doc settings and about

    """
    This method is called when a user inputs something
    inside of the "Search" input box and presses return.

    It's role is to gather data and construct Playable
    object so they can be displayed inside of PCS.

    A Playable is a object which contains abstract data
    about some stream such as the title.

    To implement this, query the API/scape the site and
    append playable objects to the playables array.

    All the work done here is done in a separate thread,
    so do not worry about UI blocking.

    If the search result set is empty just return an empty
    array.

    WARNING: If there is a lot of results, you risk server flooding.
    Please limit the search result set to around 400 results.
    """
    def search(self, query):

        playables = [] # Playable[]

        # Start of implementation

        """
        Here you would query the API/scrape the site
        and construct usable Playble objects from the
        data received from the server. We are just going
        to create some dummy playable to display in PCS
        """

        somePlayable = Playable()

        """
        The minimum amount of data that a
        streamable MUST contain is a title
        and a parent id when it returns from
        the search method. The parent id
        is always self.id
        """
        somePlayable.setTitle("Hello, world!")
        somePlayable.setParentPluginId(self.id)

        """
        Everything else here is a bonus.

        If you have more items in the search results site/API,
        for example a poster, just add it to the somePlayable object

        somePlayable.setPoster("http://www.example.com/poster.jpg")

        But remember, if you add more data here,
        you MUST comment out the setter in fetchPlayableMetadata.

        For example, down in fetchPlayableMedia you MUST have:

        playable.setDataStreams(streams)
        playable.setSubtitleStreams(subtitles)
        # playable.setPoster(posterUrl) <-- COMMENTED OUT !!!
        playable.setDescription(description)
        playable.setPlayableLength(movieLength)

        Don't forget to append the playable to the
        playables list.
        """
        playables.append(somePlayable)

        """
        If you have some exceptions thrown, catch them all
        and re-throw a PluginException. This way, a error
        message is displayed and nothing happens to PCS.
        If you throw something else here, PCS could crash.

        To try it out, comment this out below.
        """

        try:
            raise PluginException("Example error")
        except BaseException as e:
            self.catchException(e)

        # End of implementation

        return playables

    """
    This method is called when a user double clicks
    some search result inside of PCS. ]

    It's role is to fetch the actual stream information
    and the source for subtitles, as well as the poster, length
    and the description.

    Streams are implemented as a DataStream object, which
    has 2 main fields: a source and label.
    The source is a URI to some remote resource, and the label
    is the resource that is displayed inside of PCS in the drop down
    boxes next to the poster.

    For example:

    source -> http://www.example.com/media_720p.mp4
    label -> "720p"

    PCS supports more than one quality of media, just keep appending
    DataStream objects to the streams list.

    Subtitles are implemented as a SubtitleStream object. A subtitle
    stream also has a source and a label, and it's the same as
    with DataStream. The preferred format is SRT, but the
    subtitle decoding varies based on players.

    source -> http://www.example.com/subtutle_english.srt
    label -> "English"

    This method also sets the description, length, and the poster URL.
    The poster URL must point to a drawable that QPixmap supports.

    The description must be a string, if there is none, pass None.

    The poster must be a URL to a remote drawable, if there is none,
    pass None.

    The movieLength must be a integer. If the length is unknown, pass
    0, if the remote object is a live stream, pass -1.

    If you set some other data in search(), such as the poster, you
    must comment out the setter at the end of the method.
    """
    def fetchPlayableMetadata(self, playable):

        streams  = [] # DataStream[]
        subtitles = [] # SubtitleStream[]
        posterUrl = None
        description = None
        movieLength = 0

        # Start of implementation

        """
        There could be more than one stream, if there is just
        create more objects and append them to the
        streams list.

        Each stream is a remote resource and a label.
        """
        someStream = DataStream()
        someStream.setSource("http://www.example.com/data.mp4")
        someStream.setLabel("DUMMY")
        streams.append(someStream)

        """
        There could also be more than one subtitle language.
        Create objects for each language and add to streams.

        Each subtitle is a remote resource and the label.
        """
        someSubtitle = SubtitleStream()
        someSubtitle.setLabel("DUMMY")
        someSubtitle.setSource("http://www.example.com/title.mp4")
        subtitles.append(someSubtitle)

        """
        The poster is a remote resource that is QPixmap compatible.
        """
        posterUrl = "https://upload.wikimedia.org/wikipedia/commons/thumb/6/69/Linus_Torvalds.jpeg/220px-Linus_Torvalds.jpeg"

        """
        If there is no description leave the declaration
        at the start intact.
        """
        description = "Hello world plugin for PCS"

        """
        The movie length in seconds. If the length is unknown,
        leave the declaration at the start intact. If the
        remote playable is a lives tream, pass -1.
        """
        movieLength = 90

        # End of implementation

        """
        I SAID IT 3 TIMES, AND I'M GONNA SAY IT AGAIN.

        If you have added something to the playable
        inside the search method, you MUST COMMENT OUT
        the calls below that match the ones in search().
        """
        playable.setDataStreams(streams)
        playable.setSubtitleStreams(subtitles)
        playable.setPoster(posterUrl)
        playable.setDescription(description)
        playable.setPlayableLength(movieLength)