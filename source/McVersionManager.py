"""
Copyright (c) 2023-2024 BrightSky OSSDO
This code is released under the MIT license
"""

# This file is the entry point to the program

# Import our custom modules:
import tabs
import menus

# Import other modules:
from PyQt5.QtWidgets import QMainWindow, QApplication
import sys

def createMainWindow():
    mainWindow = QMainWindow()
    mainWindow.setWindowTitle("McVersionManager")
    mainWindow.setMinimumSize(300, 200)
    mainWindow.resize(800, 600)

    tabInterface = tabs.createTabs()

    mainWindow.setCentralWidget(tabInterface)

    menubar = mainWindow.menuBar()
    menubar.addMenu(menus.createFileMenu(mainWindow))
    menubar.addMenu(menus.createOptionsMenu(mainWindow))
    mainWindow.setMenuBar(menubar)

    mainWindow.statusBar()

    return mainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = createMainWindow()
    window.show()

    sys.exit(app.exec_())