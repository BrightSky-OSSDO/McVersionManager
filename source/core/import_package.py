"""
Copyright (c) 2023-2024 BrightSky OSSDO
This code is released under the MIT license
"""

# This file contains package importing functionality for McVersionManager

# Import PyQt modules:
from PyQt5.QtWidgets import QFileDialog, QMessageBox
from PyQt5.QtCore import QDir

def showFileDialog():
    filename, _ = QFileDialog.getOpenFileName(None, "Select Package File", QDir.homePath(), "UWP App Package (*.appx *.msix);;Android Package Kit (*.apk *.xapk);;iOS AppStore Package (*.ipa)")

    if filename:
        invalidPackage(filename)


def invalidPackage(package):
    invalid = QMessageBox()
    invalid.setIcon(QMessageBox.Critical)
    invalid.setWindowTitle("Invalid Package File")
    invalid.setText(f"File '{package}' is not a valid Minecraft package.")
    invalid.exec_()