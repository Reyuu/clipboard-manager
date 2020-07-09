# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'clipboard_manager.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_Frame(object):
    def setupUi(self, Frame):
        if not Frame.objectName():
            Frame.setObjectName(u"Frame")
        Frame.resize(411, 303)
        self.gridLayout = QGridLayout(Frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.top_bar_layout = QHBoxLayout()
        self.top_bar_layout.setObjectName(u"top_bar_layout")
        self.add_button = QPushButton(Frame)
        self.add_button.setObjectName(u"add_button")

        self.top_bar_layout.addWidget(self.add_button)

        self.remove_button = QPushButton(Frame)
        self.remove_button.setObjectName(u"remove_button")

        self.top_bar_layout.addWidget(self.remove_button)

        self.enable_button = QPushButton(Frame)
        self.enable_button.setObjectName(u"enable_button")

        self.top_bar_layout.addWidget(self.enable_button)

        self.disable_button = QPushButton(Frame)
        self.disable_button.setObjectName(u"disable_button")

        self.top_bar_layout.addWidget(self.disable_button)


        self.verticalLayout.addLayout(self.top_bar_layout)

        self.table_layout = QVBoxLayout()
        self.table_layout.setObjectName(u"table_layout")
        self.table = QTableWidget(Frame)
        if (self.table.columnCount() < 1):
            self.table.setColumnCount(1)
        __qtablewidgetitem = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        self.table.setObjectName(u"table")
        self.table.setAlternatingRowColors(False)
        self.table.setSelectionMode(QAbstractItemView.SingleSelection)
        self.table.setSelectionBehavior(QAbstractItemView.SelectItems)
        self.table.setGridStyle(Qt.SolidLine)
        self.table.setSortingEnabled(False)
        self.table.setCornerButtonEnabled(True)
        self.table.horizontalHeader().setVisible(False)
        self.table.horizontalHeader().setStretchLastSection(True)
        self.table.verticalHeader().setVisible(False)
        self.table.verticalHeader().setCascadingSectionResizes(False)
        self.table.verticalHeader().setProperty("showSortIndicator", True)
        self.table.verticalHeader().setStretchLastSection(False)

        self.table_layout.addWidget(self.table)


        self.verticalLayout.addLayout(self.table_layout)

        self.bottom_bar_layout = QVBoxLayout()
        self.bottom_bar_layout.setObjectName(u"bottom_bar_layout")
        self.checkboxes_layout = QHBoxLayout()
        self.checkboxes_layout.setObjectName(u"checkboxes_layout")
        self.sequential_pasting_checkbox = QCheckBox(Frame)
        self.sequential_pasting_checkbox.setObjectName(u"sequential_pasting_checkbox")

        self.checkboxes_layout.addWidget(self.sequential_pasting_checkbox)

        self.clipboard_capturing_checkbox = QCheckBox(Frame)
        self.clipboard_capturing_checkbox.setObjectName(u"clipboard_capturing_checkbox")

        self.checkboxes_layout.addWidget(self.clipboard_capturing_checkbox)


        self.bottom_bar_layout.addLayout(self.checkboxes_layout)

        self.window_opacity_label = QLabel(Frame)
        self.window_opacity_label.setObjectName(u"window_opacity_label")

        self.bottom_bar_layout.addWidget(self.window_opacity_label)

        self.window_opacity_slider = QSlider(Frame)
        self.window_opacity_slider.setObjectName(u"window_opacity_slider")
        self.window_opacity_slider.setOrientation(Qt.Horizontal)
        self.window_opacity_slider.setRange(10, 100)
        self.window_opacity_slider.setValue(100)

        self.bottom_bar_layout.addWidget(self.window_opacity_slider)


        self.verticalLayout.addLayout(self.bottom_bar_layout)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        QWidget.setTabOrder(self.add_button, self.remove_button)
        QWidget.setTabOrder(self.remove_button, self.enable_button)
        QWidget.setTabOrder(self.enable_button, self.disable_button)
        QWidget.setTabOrder(self.disable_button, self.sequential_pasting_checkbox)
        QWidget.setTabOrder(self.sequential_pasting_checkbox, self.clipboard_capturing_checkbox)
        QWidget.setTabOrder(self.clipboard_capturing_checkbox, self.window_opacity_slider)
        QWidget.setTabOrder(self.window_opacity_slider, self.table)

        self.retranslateUi(Frame)
        self.add_button.clicked.connect(Frame.add_item_to_table)
        self.remove_button.clicked.connect(Frame.remove_item_from_table)
        self.enable_button.clicked.connect(Frame.enable_item_in_table)
        self.disable_button.clicked.connect(Frame.disable_item_in_table)
        self.table.itemClicked.connect(Frame.clicked_item_in_table)
        self.sequential_pasting_checkbox.clicked.connect(Frame.clicked_sequential_pasting)
        self.clipboard_capturing_checkbox.clicked.connect(Frame.clicked_clipboard_capturing)
        self.window_opacity_slider.valueChanged.connect(Frame.changed_window_opacity)

        QMetaObject.connectSlotsByName(Frame)
    # setupUi

    def retranslateUi(self, Frame):
        Frame.setWindowTitle(QCoreApplication.translate("Frame", u"Clipboard manager", None))
        self.add_button.setText(QCoreApplication.translate("Frame", u"Add", None))
        self.remove_button.setText(QCoreApplication.translate("Frame", u"Remove", None))
        self.enable_button.setText(QCoreApplication.translate("Frame", u"Enable", None))
        self.disable_button.setText(QCoreApplication.translate("Frame", u"Disable", None))
        ___qtablewidgetitem = self.table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Frame", u"Nowa kolumna", None));

        self.sequential_pasting_checkbox.setText(QCoreApplication.translate("Frame", u"Sequential pasting", None))
        self.clipboard_capturing_checkbox.setText(QCoreApplication.translate("Frame", u"Clipboard capturing", None))
        self.window_opacity_label.setText(QCoreApplication.translate("Frame", u"Window opacity", None))
    # retranslateUi

