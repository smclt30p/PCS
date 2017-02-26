import importlib
import os

class PluginLoader:

    loadedPlugins = []
    loaded = False

    @staticmethod
    def getLoadedPlugins():

        """
        This returns instances for all PluginImpl's from
        core.plugins.load
        :return: [] of plugins
        """

        if not PluginLoader.loaded:

            for plugin in os.listdir("../core/plugins/load/."):

                mod = importlib.import_module("core.plugins.load." + plugin.replace(".py", ""))

                if hasattr(mod, "PluginImpl"):
                    PluginLoader.loadedPlugins.append(getattr(mod, "PluginImpl")())

                PluginLoader.loaded = True

        return PluginLoader.loadedPlugins