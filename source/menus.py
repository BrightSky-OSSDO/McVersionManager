"""
Copyright (c) 2023-2024 BrightSky OSSDO
This code is released under the MIT license
"""

# This file is for creating menus

# Import our module for importing custom package files:
import core.import_package

# Import the other modules:
from PyQt5.QtWidgets import QMenu, QAction
import sys

def createFileMenu(parent):
    fileMenu = QMenu("File", parent)

    importPackageItem = QAction("Import package", parent)
    exitItem = QAction("Exit", parent)

    importPackageItem.setStatusTip("Import your own package file to install a Minecraft version that isn't available here")
    exitItem.setStatusTip("Exit McVersionManager")

    importPackageItem.triggered.connect(core.import_package.showFileDialog)
    exitItem.triggered.connect(sys.exit)

    fileMenu.addAction(importPackageItem)
    fileMenu.addAction(exitItem)

    return fileMenu

def createOptionsMenu(parent):
    optionsMenu = QMenu("Options", parent)

    deleteOption = QAction("Delete package files after install", parent)
    uninstallOption = QAction("Uninstall all versions", parent)
    refreshOption = QAction("Refresh version list", parent)

    deleteOption.setCheckable(True)
    uninstallOption.setEnabled(False)

    deleteOption.setChecked(True)

    deleteOption.setStatusTip("Automatically delete downloaded package files after installing them to save disk space")
    uninstallOption.setStatusTip("Uninstall all Minecraft versions, be very careful with this!")
    refreshOption.setStatusTip("Refresh the list of Minecraft versions")

    optionsMenu.addAction(deleteOption)
    optionsMenu.addAction(uninstallOption)
    optionsMenu.addAction(refreshOption)

    return optionsMenu