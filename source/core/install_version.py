"""
Copyright (c) 2023-2024 BrightSky OSSDO
This code is released under the MIT license
"""

# This file is for installing Minecraft versions

# Import required modules:
from PyQt5.QtWidgets import QMessageBox, QApplication
from PyQt5.QtCore import Qt
import time

def installVersion():
    QApplication.setOverrideCursor(Qt.WaitCursor)
    time.sleep(2)
    QApplication.restoreOverrideCursor()
    
    failure = QMessageBox()
    failure.setIcon(QMessageBox.Critical)
    failure.setWindowTitle("Unknown Error")
    failure.setText("An unknown error occurred when fetching the package file. Try again with a different Minecraft version.")
    failure.exec_()