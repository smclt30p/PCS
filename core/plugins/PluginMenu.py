from PyQt5.QtCore import QObject, pyqtSlot
from PyQt5.QtCore import QSignalMapper
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QAction

from core.plugins.PluginLoader import PluginLoader


class PluginMenu(QObject):

    currRoot = None

    def constructMenu(self, root):

        self.currRoot = root

        root.clear()
        plugins = PluginLoader.getLoadedPlugins()

        if len(plugins) == 0:
            item = root.addAction("No plugins found")
            item.setEnabled(False)
            return

        for plugin in plugins:

            item = root.addMenu(plugin.getPluginName())

            actionToggle = item.addAction("UNDEFINED")

            if plugin.isActive():
                actionToggle.setText("Disable")
            else:
                actionToggle.setText("Enable")

            actionSettings = item.addAction("Settings")

            item.addSeparator()
            actionAbout = item.addAction("About")

            if not plugin.hasAbout or not plugin.isActive():
                actionAbout.setEnabled(False)

            if not plugin.hasSettings or not plugin.isActive():
                actionSettings.setEnabled(False)

            actionAbout.triggered.connect(self.handleAbout)
            #actionSettings.triggered.connect(self.handleToggle)
            actionToggle.triggered.connect(self.handleToggle)

            actionAbout.plugin = plugin
            actionSettings.plugin = plugin
            actionToggle.plugin = plugin

        return root

    def handleToggle(self):

        action = self.sender()

        if action.plugin.isActive():
            action.plugin.setActive(False)
        else:
            action.plugin.setActive(True)


        PluginLoader.reloadPlugins()

        if self.currRoot != None:
            self.constructMenu(self.currRoot)

    def handleAbout(self):
        action = self.sender()
        action.plugin.getAboutInterface().show()