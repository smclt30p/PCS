from PyQt5.QtWidgets import QAction

from core.plugins.PluginLoader import PluginLoader


class PluginMenu:

    @staticmethod
    def constructMenu(root):

        plugins = PluginLoader.getLoadedPlugins()

        for plugin in plugins:
            item = root.addMenu(plugin.getPluginName())
            item.namedPlugin = plugin

            actionDisable = QAction("Disable")
            actionSettings = QAction("Settings")
            actionAbout = QAction("About")

            item.addAction(actionDisable)
            item.addAction(actionSettings)
            item.addSeparator()
            item.addAction(actionAbout)

        return root