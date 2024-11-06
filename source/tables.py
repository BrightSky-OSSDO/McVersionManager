"""
Copyright (c) 2023-2024 BrightSky OSSDO
This code is released under the MIT license
"""

# This file is for creating the tables

# Import our custom modules:
import core.install_version
import versions

# Import other modules:
from PyQt5.QtWidgets import QTableWidget, QTableView, QHeaderView, QTableWidgetItem, QPushButton
from PyQt5.QtCore import Qt

def createTable1():
    table1 = QTableWidget()
    table1.setRowCount(len(versions.releases))
    table1.setColumnCount(2)
    table1.setShowGrid(False)
    table1.setSelectionBehavior(QTableView.SelectRows)
    table1.setSelectionMode(QTableView.SingleSelection)
    table1.verticalHeader().hide()
    
    header = table1.horizontalHeader()
    header.hide()
    header.setSectionResizeMode(0, QHeaderView.Stretch)
    header.setSectionResizeMode(0, QHeaderView.Stretch)

    for index, item in enumerate(versions.releases):
        item_name = QTableWidgetItem(item)
        table1.setItem(index, 0, item_name)
        item_name.setFlags(item_name.flags() ^ Qt.ItemIsEditable)

        downloadButton = QPushButton("Download")
        downloadButton.clicked.connect(core.install_version.installVersion)
        table1.setCellWidget(index, 1, downloadButton)

    return table1

def createTable2():
    table2 = QTableWidget()
    table2.setRowCount(0)
    table2.setColumnCount(2)
    table2.setShowGrid(False)
    table2.setSelectionBehavior(QTableView.SelectRows)
    table2.setSelectionMode(QTableView.SingleSelection)
    table2.verticalHeader().hide()
    table2.horizontalHeader().hide()

    return table2