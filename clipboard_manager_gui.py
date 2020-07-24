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
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.add_button.sizePolicy().hasHeightForWidth())
        self.add_button.setSizePolicy(sizePolicy)
        icon = QIcon()
        icon.addFile(u"icon/plus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.add_button.setIcon(icon)
        self.add_button.setIconSize(QSize(24, 24))
        self.add_button.setFlat(True)

        self.top_bar_layout.addWidget(self.add_button)

        self.remove_button = QPushButton(Frame)
        self.remove_button.setObjectName(u"remove_button")
        sizePolicy.setHeightForWidth(self.remove_button.sizePolicy().hasHeightForWidth())
        self.remove_button.setSizePolicy(sizePolicy)
        icon1 = QIcon()
        icon1.addFile(u"icon/minus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.remove_button.setIcon(icon1)
        self.remove_button.setIconSize(QSize(24, 24))
        self.remove_button.setFlat(True)

        self.top_bar_layout.addWidget(self.remove_button)

        self.enable_button = QPushButton(Frame)
        self.enable_button.setObjectName(u"enable_button")
        sizePolicy.setHeightForWidth(self.enable_button.sizePolicy().hasHeightForWidth())
        self.enable_button.setSizePolicy(sizePolicy)
        icon2 = QIcon()
        icon2.addFile(u"icon/check-square.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.enable_button.setIcon(icon2)
        self.enable_button.setIconSize(QSize(24, 24))
        self.enable_button.setFlat(True)

        self.top_bar_layout.addWidget(self.enable_button)

        self.disable_button = QPushButton(Frame)
        self.disable_button.setObjectName(u"disable_button")
        sizePolicy.setHeightForWidth(self.disable_button.sizePolicy().hasHeightForWidth())
        self.disable_button.setSizePolicy(sizePolicy)
        icon3 = QIcon()
        icon3.addFile(u"icon/x-square.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.disable_button.setIcon(icon3)
        self.disable_button.setIconSize(QSize(24, 24))
        self.disable_button.setFlat(True)

        self.top_bar_layout.addWidget(self.disable_button)

        self.options_button = QPushButton(Frame)
        self.options_button.setObjectName(u"options_button")
        sizePolicy.setHeightForWidth(self.options_button.sizePolicy().hasHeightForWidth())
        self.options_button.setSizePolicy(sizePolicy)
        icon4 = QIcon()
        icon4.addFile(u"icon/settings.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.options_button.setIcon(icon4)
        self.options_button.setIconSize(QSize(24, 24))
        self.options_button.setFlat(True)

        self.top_bar_layout.addWidget(self.options_button)


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
        self.window_opacity_label = QLabel(Frame)
        self.window_opacity_label.setObjectName(u"window_opacity_label")

        self.bottom_bar_layout.addWidget(self.window_opacity_label)

        self.window_opacity_slider = QSlider(Frame)
        self.window_opacity_slider.setObjectName(u"window_opacity_slider")
        self.window_opacity_slider.setMinimum(10)
        self.window_opacity_slider.setMaximum(100)
        self.window_opacity_slider.setValue(100)
        self.window_opacity_slider.setOrientation(Qt.Horizontal)

        self.bottom_bar_layout.addWidget(self.window_opacity_slider)


        self.verticalLayout.addLayout(self.bottom_bar_layout)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        QWidget.setTabOrder(self.add_button, self.remove_button)
        QWidget.setTabOrder(self.remove_button, self.enable_button)
        QWidget.setTabOrder(self.enable_button, self.disable_button)
        QWidget.setTabOrder(self.disable_button, self.window_opacity_slider)
        QWidget.setTabOrder(self.window_opacity_slider, self.table)

        self.retranslateUi(Frame)
        self.add_button.clicked.connect(Frame.add_item_to_table)
        self.remove_button.clicked.connect(Frame.remove_item_from_table)
        self.enable_button.clicked.connect(Frame.enable_item_in_table)
        self.disable_button.clicked.connect(Frame.disable_item_in_table)
        self.table.itemClicked.connect(Frame.clicked_item_in_table)
        self.window_opacity_slider.valueChanged.connect(Frame.changed_window_opacity)
        self.options_button.clicked.connect(Frame.clicked_settings)
        self.table.itemChanged.connect(Frame.changed_item_in_table)
        self.table.doubleClicked.connect(Frame.doubleclicked_item_in_table)

        QMetaObject.connectSlotsByName(Frame)
    # setupUi

    def retranslateUi(self, Frame):
        Frame.setWindowTitle(QCoreApplication.translate("Frame", u"Clipboard manager", None))
#if QT_CONFIG(tooltip)
        self.add_button.setToolTip(QCoreApplication.translate("Frame", u"Add", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.remove_button.setToolTip(QCoreApplication.translate("Frame", u"Remove", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.enable_button.setToolTip(QCoreApplication.translate("Frame", u"Enable", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.disable_button.setToolTip(QCoreApplication.translate("Frame", u"Disable", None))
#endif // QT_CONFIG(tooltip)
        self.disable_button.setText("")
#if QT_CONFIG(tooltip)
        self.options_button.setToolTip(QCoreApplication.translate("Frame", u"Options", None))
#endif // QT_CONFIG(tooltip)
        self.window_opacity_label.setText(QCoreApplication.translate("Frame", u"Window opacity", None))
    # retranslateUi

