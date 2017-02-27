import importlib
import os

from PyQt5.QtCore import QSettings


class Continue(BaseException):
    pass


class PluginLoader:

    loadedPlugins = []
    loaded = False
    settings = QSettings("plugins.ini", QSettings.IniFormat)

    @staticmethod
    def getLoadedPlugins():

        """
        This returns instances for all PluginImpl's from
        core.plugins.load
        :return: [] of plugins
        """

        if not PluginLoader.loaded:

            for plugin in os.listdir("../plugins/."):

                if not plugin.endswith("_plugin"):
                    continue

                mod = importlib.import_module("plugins." + plugin + ".PluginImpl")

                if hasattr(mod, "PluginImpl"):

                    instance = getattr(mod, "PluginImpl")()
                    instance.nativeName = plugin
                    instance.settings = PluginLoader.settings
                    PluginLoader.loadedPlugins.append(instance)

            PluginLoader.loaded = True

        return PluginLoader.loadedPlugins

    @classmethod
    def reloadPlugins(cls):
        print("Reloading plugins...")
        PluginLoader.loadedPlugins = []
        PluginLoader.loaded = False
        PluginLoader.getLoadedPlugins()