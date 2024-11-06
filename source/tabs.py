"""
Copyright (c) 2023-2024 BrightSky OSSDO
This code is released under the MIT license
"""

# This file is for creating tabs

# Import table module:
import tables

# Import other modules:
from PyQt5.QtWidgets import QTabWidget, QWidget, QVBoxLayout

def createTabs():
    tabWidget = QTabWidget()

    tab1 = QWidget()
    tab2 = QWidget()
    tab3 = QWidget()

    table1 = tables.createTable1()
    table2 = tables.createTable2()
    table3 = tables.createTable2() # I know this looks like a typo but it isn't

    layout1 = QVBoxLayout()
    layout1.addWidget(table1)
    tab1.setLayout(layout1)

    layout2 = QVBoxLayout()
    layout2.addWidget(table2)
    tab2.setLayout(layout2)

    layout3 = QVBoxLayout()
    layout3.addWidget(table3)
    tab3.setLayout(layout3)

    tabWidget.addTab(tab1, "Versions")
    tabWidget.addTab(tab2, "Imported")
    tabWidget.addTab(tab3, "Installed")

    return tabWidget