# DataStream>
# - str : url of stream
# - str : stream label (ex. 720p)
# + getLabel() : str
# + getSource() : str
#
# SubtitleStream>
# - std : url of subtitle
# - subtitle label (ex. English)
# + getSource() : str
# + getLabel() : str
#
#
# SearchResults>
# - str : plugin name
# [] results : Playable
# + getResults() : [] Playable
# + getPluginName() : str
#
# Playable>
# - str : poster URL
# - str : title
# - parentId : id of parent plugin
# - [] DataStream : streams
# - [] SubtitleStream : subtitles
# + fetchInfo() : void
#
############## IMPLEMENTATION

class Plugin:

    """
    This is the base class for a plugin implementation.
    To implement a PCS plugin, please subclass this class
    and call the child class "PluginImpl". Next, override the
    following methods:

    fetchPlayableMetadata()
    search()

    To see how to implement these methods, refer to the docs below
    and the basic class layout above this description.

    To introduce the plugin to PCS, please override the following
    class members:

    version - Plugin version (ex. 1.0.0)
    name - Plugin name (ex. Example)
    author - Plugin author (ex. Pera Lozac)
    description - Plugin description (ex. Example plugin for PCS)

    """

    version = None # 1.0.0
    name = None # Example
    author = None # Pera Lozac
    description = None # Example plugin for PCS by Pera
    id = -1

    def __init__(self):
        print("{} {} loaded".format(self.name, self.version))

    def fetchPlayableMetadata(self, playable):
        """
        This method populates all the advanced properties
        of a playable object. These include:

        - Stream sources (getDataStreams)
        - Subtitle sources (getSubtitleStreams)
        - The poster of the playable (getPoster)
        - Description of the playable (getDescription)

        This method is called by PCS when a user
        double clicks a search result to fetch more info.
        This is the pre-play method.

        :param playable: The playable object to fetch info for
        :return: void
        """
        pass

    def search(self, query):
        """
        This method must query the web source and
        construct the playable objects.

        This method must populate the most basic info
        for a playable object, and that includes:

        - The title (getTitle)

        This method returns an array of playable objects

        :param query: The search query
        :return: [] Playable : List of playable objects from the search
        """
        pass

    def getVersion(self):
        return self.version

    def getPluginName(self):
        return self.name

    def getPluginAuthor(self):
        return self.author

    def getPluginDescription(self):
        return self.description

    def getPluginId(self):
        return self.id

class DataStream:

    streamSource = None
    streamLabel = None

    def getLabel(self):
        """
        Return the label representing this stream.
        For example, "720p" or "HD"
        :return: str : Label of the stream object
        """
        return self.streamLabel

    def setLabel(self, streamLabel):
        self.streamLabel = streamLabel

    def getSource(self):
        """
        Return the remote location of the streamable object.
        For example, "http://www.example.com/video.mp4"
        :return:
        """
        return self.streamSource

    def setSource(self, streamSource):
        self.streamSource = streamSource

class SubtitleStream:

    streamSource = None
    streamLabel = None

    def getLabel(self):
        """
        Return the label representing the subtitle.
        For example, "English"
        :return: str : Label representing the subtitle
        """
        return self.streamLabel

    def setLabel(self, streamLabel):
        self.streamLabel = streamLabel

    def getSource(self):
        """
        Return the remote location of the subtitle.
        For example, "http://www.example.com/subtitle.srt"
        :return: str : URL of the remote subtitle file
        """
        return self.streamSource

    def setSource(self, streamSource):
        self.streamSource = streamSource

class Playable:

    posterSource = None
    title = None
    description = None
    dataStreams = []
    subtitleStreams = []
    parentId = None
    length = 0
    fetched = False

    def getPoster(self):
        """
        Return the poster of the playable object.
        This should return a str representing a remote
        drawable object that QPixmap supports

        PCS DEVELOPER NOTE: This becomes a QPixmap after
        it has been pulled through the MetadataWorker

        :return: str : URL of remote drawable
        """
        return self.posterSource

    def setPoster(self, posterSource):
        self.posterSource = posterSource

    def getTitle(self):
        """
        Return the title of the playable object.
        This should return a str representing the title
        of the playable.
        This is basic information.
        :return: str : Title of the playable
        """
        return self.title

    def setTitle(self, title):
        self.title = title

    def getDescription(self):
        """
        Return the extended description of a playable.
        This should return a str with the detailed description
        of the playable.
        :return:
        """
        return self.description

    def setDescription(self, description):
        self.description = description

    def getDataStreams(self):
        """
        Return an array of different quality data streams.
        This returns an list of DataStream objects, that
        represent the playable object.
        If there is different qualities available, return more
        than one, if there is just one quality available, return
        just one object in the array.
        :return: [] DataStream : Array of different quality streams
        """
        return self.dataStreams

    def setDataStreams(self, dataStreams):
        self.dataStreams = dataStreams

    def getSubtitleStreams(self):
        """
        Return an array of subtitles for the movie in different
        languages. If there is no subtitles for the playable, return
        an empty array.
        :return: [] SubtitleStream : Array of subtitles
        """
        return self.subtitleStreams

    def setSubtitleStreams(self, subtitleStreams):
        self.subtitleStreams = subtitleStreams

    def getParentPluginId(self):
        """
        Return the ID of the parent plugin of this
        This returns the ID of the plugin that created
        this playable. To be used in lists of playables
        to fetch metadata.
        playable
        :return: int : ID of parent plugin
        """
        return self.parentId

    def setParentPluginId(self, parentId):
        self.parentId = parentId

    def getPlayableLength(self):
        """
        Return the length of the playable item in seconds
        This returns the length of the playable item in seconds.
        If the item is a stream, return -1, if it's unknown, return 0
        :return: int: playable length
        """
        return self.length

    def setPlayableLength(self, length):
        self.length = length

    def isFetched(self):
        """
        Return if the metadata has already been fetched.
        :return:
        """
        return self.fetched

    def setFetched(self, fetched):
        self.fetched = fetched

class PluginException(BaseException):
    pass