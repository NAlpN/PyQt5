# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'HastaKaydı.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1092, 803)
        MainWindow.setStyleSheet("/*\n"
"Aqua Style Sheet for QT Applications\n"
"Author: Jaime A. Quiroga P.\n"
"Company: GTRONICK\n"
"Last updated: 22/01/2019, 07:55.\n"
"Available at: https://github.com/GTRONICK/QSS/blob/master/Aqua.qss\n"
"*/\n"
"QMainWindow {\n"
"    background-color:#ececec;\n"
"}\n"
"QTextEdit {\n"
"    border-width: 1px;\n"
"    border-style: solid;\n"
"    border-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));\n"
"}\n"
"QPlainTextEdit {\n"
"    border-width: 1px;\n"
"    border-style: solid;\n"
"    border-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));\n"
"}\n"
"QToolButton {\n"
"    border-style: solid;\n"
"    border-top-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));\n"
"    border-right-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(217, 217, 217), stop:1 rgb(227, 227, 227));\n"
"    border-left-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(227, 227, 227), stop:1 rgb(217, 217, 217));\n"
"    border-bottom-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: rgb(0,0,0);\n"
"    padding: 2px;\n"
"    background-color: rgb(255,255,255);\n"
"}\n"
"QToolButton:hover{\n"
"    border-style: solid;\n"
"    border-top-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(195, 195, 195), stop:1 rgb(222, 222, 222));\n"
"    border-right-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(197, 197, 197), stop:1 rgb(227, 227, 227));\n"
"    border-left-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(227, 227, 227), stop:1 rgb(197, 197, 197));\n"
"    border-bottom-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(195, 195, 195), stop:1 rgb(222, 222, 222));\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: rgb(0,0,0);\n"
"    padding: 2px;\n"
"    background-color: rgb(255,255,255);\n"
"}\n"
"QToolButton:pressed{\n"
"    border-style: solid;\n"
"    border-top-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));\n"
"    border-right-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(217, 217, 217), stop:1 rgb(227, 227, 227));\n"
"    border-left-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(227, 227, 227), stop:1 rgb(217, 217, 217));\n"
"    border-bottom-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: rgb(0,0,0);\n"
"    padding: 2px;\n"
"    background-color: rgb(142,142,142);\n"
"}\n"
"QPushButton{\n"
"    border-style: solid;\n"
"    border-top-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));\n"
"    border-right-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(217, 217, 217), stop:1 rgb(227, 227, 227));\n"
"    border-left-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(227, 227, 227), stop:1 rgb(217, 217, 217));\n"
"    border-bottom-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: rgb(0,0,0);\n"
"    padding: 2px;\n"
"    background-color: rgb(255,255,255);\n"
"}\n"
"QPushButton::default{\n"
"    border-style: solid;\n"
"    border-top-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));\n"
"    border-right-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(217, 217, 217), stop:1 rgb(227, 227, 227));\n"
"    border-left-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(227, 227, 227), stop:1 rgb(217, 217, 217));\n"
"    border-bottom-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: rgb(0,0,0);\n"
"    padding: 2px;\n"
"    background-color: rgb(255,255,255);\n"
"}\n"
"QPushButton:hover{\n"
"    border-style: solid;\n"
"    border-top-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(195, 195, 195), stop:1 rgb(222, 222, 222));\n"
"    border-right-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(197, 197, 197), stop:1 rgb(227, 227, 227));\n"
"    border-left-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(227, 227, 227), stop:1 rgb(197, 197, 197));\n"
"    border-bottom-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(195, 195, 195), stop:1 rgb(222, 222, 222));\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: rgb(0,0,0);\n"
"    padding: 2px;\n"
"    background-color: rgb(255,255,255);\n"
"}\n"
"QPushButton:pressed{\n"
"    border-style: solid;\n"
"    border-top-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));\n"
"    border-right-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(217, 217, 217), stop:1 rgb(227, 227, 227));\n"
"    border-left-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(227, 227, 227), stop:1 rgb(217, 217, 217));\n"
"    border-bottom-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: rgb(0,0,0);\n"
"    padding: 2px;\n"
"    background-color: rgb(142,142,142);\n"
"}\n"
"QPushButton:disabled{\n"
"    border-style: solid;\n"
"    border-top-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));\n"
"    border-right-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(217, 217, 217), stop:1 rgb(227, 227, 227));\n"
"    border-left-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(227, 227, 227), stop:1 rgb(217, 217, 217));\n"
"    border-bottom-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: #808086;\n"
"    padding: 2px;\n"
"    background-color: rgb(142,142,142);\n"
"}\n"
"QLineEdit {\n"
"    border-width: 1px; border-radius: 4px;\n"
"    border-style: solid;\n"
"    border-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));\n"
"}\n"
"QLabel {\n"
"    color: #000000;\n"
"}\n"
"QLCDNumber {\n"
"    color: rgb(0, 113, 255, 255);\n"
"}\n"
"QProgressBar {\n"
"    text-align: center;\n"
"    color: rgb(240, 240, 240);\n"
"    border-width: 1px; \n"
"    border-radius: 10px;\n"
"    border-color: rgb(230, 230, 230);\n"
"    border-style: solid;\n"
"    background-color:rgb(207,207,207);\n"
"}\n"
"QProgressBar::chunk {\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(49, 147, 250, 255), stop:1 rgba(34, 142, 255, 255));\n"
"    border-radius: 10px;\n"
"}\n"
"QMenuBar {\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(207, 209, 207, 255), stop:1 rgba(230, 229, 230, 255));\n"
"}\n"
"QMenuBar::item {\n"
"    color: #000000;\n"
"      spacing: 3px;\n"
"      padding: 1px 4px;\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(207, 209, 207, 255), stop:1 rgba(230, 229, 230, 255));\n"
"}\n"
"\n"
"QMenuBar::item:selected {\n"
"      background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));\n"
"    color: #FFFFFF;\n"
"}\n"
"QMenu::item:selected {\n"
"    border-style: solid;\n"
"    border-top-color: transparent;\n"
"    border-right-color: transparent;\n"
"    border-left-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));\n"
"    border-bottom-color: transparent;\n"
"    border-left-width: 2px;\n"
"    color: #000000;\n"
"    padding-left:15px;\n"
"    padding-top:4px;\n"
"    padding-bottom:4px;\n"
"    padding-right:7px;\n"
"}\n"
"QMenu::item {\n"
"    border-style: solid;\n"
"    border-top-color: transparent;\n"
"    border-right-color: transparent;\n"
"    border-left-color: transparent;\n"
"    border-bottom-color: transparent;\n"
"    border-bottom-width: 1px;\n"
"    color: #000000;\n"
"    padding-left:17px;\n"
"    padding-top:4px;\n"
"    padding-bottom:4px;\n"
"    padding-right:7px;\n"
"}\n"
"QTabWidget {\n"
"    color:rgb(0,0,0);\n"
"    background-color:#000000;\n"
"}\n"
"QTabWidget::pane {\n"
"        border-color: rgb(223,223,223);\n"
"        background-color:rgb(226,226,226);\n"
"        border-style: solid;\n"
"        border-width: 2px;\n"
"        border-radius: 6px;\n"
"}\n"
"QTabBar::tab:first {\n"
"    border-style: solid;\n"
"    border-left-width:1px;\n"
"    border-right-width:0px;\n"
"    border-top-width:1px;\n"
"    border-bottom-width:1px;\n"
"    border-top-color: rgb(209,209,209);\n"
"    border-left-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(209, 209, 209, 209), stop:1 rgba(229, 229, 229, 229));\n"
"    border-bottom-color: rgb(229,229,229);\n"
"    border-top-left-radius: 4px;\n"
"    border-bottom-left-radius: 4px;\n"
"    color: #000000;\n"
"    padding: 3px;\n"
"    margin-left:0px;\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(247, 247, 247, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"QTabBar::tab:last {\n"
"    border-style: solid;\n"
"    border-width:1px;\n"
"    border-top-color: rgb(209,209,209);\n"
"    border-left-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(209, 209, 209, 209), stop:1 rgba(229, 229, 229, 229));\n"
"    border-right-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(209, 209, 209, 209), stop:1 rgba(229, 229, 229, 229));\n"
"    border-bottom-color: rgb(229,229,229);\n"
"    border-top-right-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"    color: #000000;\n"
"    padding: 3px;\n"
"    margin-left:0px;\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(247, 247, 247, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"QTabBar::tab {\n"
"    border-style: solid;\n"
"    border-top-width:1px;\n"
"    border-bottom-width:1px;\n"
"    border-left-width:1px;\n"
"    border-top-color: rgb(209,209,209);\n"
"    border-left-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(209, 209, 209, 209), stop:1 rgba(229, 229, 229, 229));\n"
"    border-bottom-color: rgb(229,229,229);\n"
"    color: #000000;\n"
"    padding: 3px;\n"
"    margin-left:0px;\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(247, 247, 247, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"QTabBar::tab:selected, QTabBar::tab:last:selected, QTabBar::tab:hover {\n"
"      border-style: solid;\n"
"      border-left-width:1px;\n"
"    border-right-color: transparent;\n"
"    border-top-color: rgb(209,209,209);\n"
"    border-left-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(209, 209, 209, 209), stop:1 rgba(229, 229, 229, 229));\n"
"    border-bottom-color: rgb(229,229,229);\n"
"    color: #FFFFFF;\n"
"    padding: 3px;\n"
"    margin-left:0px;\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));\n"
"}\n"
"\n"
"QTabBar::tab:selected, QTabBar::tab:first:selected, QTabBar::tab:hover {\n"
"      border-style: solid;\n"
"      border-left-width:1px;\n"
"      border-bottom-width:1px;\n"
"      border-top-width:1px;\n"
"    border-right-color: transparent;\n"
"    border-top-color: rgb(209,209,209);\n"
"    border-left-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(209, 209, 209, 209), stop:1 rgba(229, 229, 229, 229));\n"
"    border-bottom-color: rgb(229,229,229);\n"
"    color: #FFFFFF;\n"
"    padding: 3px;\n"
"    margin-left:0px;\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));\n"
"}\n"
"\n"
"QCheckBox {\n"
"    color: #000000;\n"
"    padding: 2px;\n"
"}\n"
"QCheckBox:disabled {\n"
"    color: #808086;\n"
"    padding: 2px;\n"
"}\n"
"\n"
"QCheckBox:hover {\n"
"    border-radius:4px;\n"
"    border-style:solid;\n"
"    padding-left: 1px;\n"
"    padding-right: 1px;\n"
"    padding-bottom: 1px;\n"
"    padding-top: 1px;\n"
"    border-width:1px;\n"
"    border-color: transparent;\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    border-style:solid;\n"
"    border-width: 1px;\n"
"    border-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));\n"
"    color: #000000;\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));\n"
"}\n"
"QCheckBox::indicator:unchecked {\n"
"\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    border-style:solid;\n"
"    border-width: 1px;\n"
"    border-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));\n"
"    color: #000000;\n"
"}\n"
"QRadioButton {\n"
"    color: 000000;\n"
"    padding: 1px;\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    border-style:solid;\n"
"    border-radius:5px;\n"
"    border-width: 1px;\n"
"    border-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));\n"
"    color: #a9b7c6;\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));\n"
"}\n"
"QRadioButton::indicator:!checked {\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    border-style:solid;\n"
"    border-radius:5px;\n"
"    border-width: 1px;\n"
"    border-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));\n"
"    color: #a9b7c6;\n"
"    background-color: transparent;\n"
"}\n"
"QStatusBar {\n"
"    color:#027f7f;\n"
"}\n"
"QSpinBox {\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));\n"
"}\n"
"QDoubleSpinBox {\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));\n"
"}\n"
"QTimeEdit {\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));\n"
"}\n"
"QDateTimeEdit {\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));\n"
"}\n"
"QDateEdit {\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));\n"
"}\n"
"\n"
"QToolBox {\n"
"    color: #a9b7c6;\n"
"    background-color:#000000;\n"
"}\n"
"QToolBox::tab {\n"
"    color: #a9b7c6;\n"
"    background-color:#000000;\n"
"}\n"
"QToolBox::tab:selected {\n"
"    color: #FFFFFF;\n"
"    background-color:#000000;\n"
"}\n"
"QScrollArea {\n"
"    color: #FFFFFF;\n"
"    background-color:#000000;\n"
"}\n"
"QSlider::groove:horizontal {\n"
"    height: 5px;\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(49, 147, 250, 255), stop:1 rgba(34, 142, 255, 255));\n"
"}\n"
"QSlider::groove:vertical {\n"
"    width: 5px;\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(49, 147, 250, 255), stop:1 rgba(34, 142, 255, 255));\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background: rgb(253,253,253);\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-color: rgb(207,207,207);\n"
"    width: 12px;\n"
"    margin: -5px 0;\n"
"    border-radius: 7px;\n"
"}\n"
"QSlider::handle:vertical {\n"
"    background: rgb(253,253,253);\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-color: rgb(207,207,207);\n"
"    height: 12px;\n"
"    margin: 0 -5px;\n"
"    border-radius: 7px;\n"
"}\n"
"QSlider::add-page:horizontal {\n"
"    background: rgb(181,181,181);\n"
"}\n"
"QSlider::add-page:vertical {\n"
"    background: rgb(181,181,181);\n"
"}\n"
"QSlider::sub-page:horizontal {\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(49, 147, 250, 255), stop:1 rgba(34, 142, 255, 255));\n"
"}\n"
"QSlider::sub-page:vertical {\n"
"    background-color: qlineargradient(spread:pad, y1:0.5, x1:1, y2:0.5, x2:0, stop:0 rgba(49, 147, 250, 255), stop:1 rgba(34, 142, 255, 255));\n"
"}\n"
"QScrollBar:horizontal {\n"
"    max-height: 20px;\n"
"    border: 1px transparent grey;\n"
"    margin: 0px 20px 0px 20px;\n"
"}\n"
"QScrollBar:vertical {\n"
"    max-width: 20px;\n"
"    border: 1px transparent grey;\n"
"    margin: 20px 0px 20px 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(253,253,253);\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-color: rgb(207,207,207);\n"
"    border-radius: 7px;\n"
"    min-width: 25px;\n"
"}\n"
"QScrollBar::handle:horizontal:hover {\n"
"    background: rgb(253,253,253);\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-color: rgb(147, 200, 200);\n"
"    border-radius: 7px;\n"
"    min-width: 25px;\n"
"}\n"
"QScrollBar::handle:vertical {\n"
"    background: rgb(253,253,253);\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-color: rgb(207,207,207);\n"
"    border-radius: 7px;\n"
"    min-height: 25px;\n"
"}\n"
"QScrollBar::handle:vertical:hover {\n"
"    background: rgb(253,253,253);\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-color: rgb(147, 200, 200);\n"
"    border-radius: 7px;\n"
"    min-height: 25px;\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"   border: 2px transparent grey;\n"
"   border-top-right-radius: 7px;\n"
"   border-bottom-right-radius: 7px;\n"
"   background: rgba(34, 142, 255, 255);\n"
"   width: 20px;\n"
"   subcontrol-position: right;\n"
"   subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::add-line:horizontal:pressed {\n"
"   border: 2px transparent grey;\n"
"   border-top-right-radius: 7px;\n"
"   border-bottom-right-radius: 7px;\n"
"   background: rgb(181,181,181);\n"
"   width: 20px;\n"
"   subcontrol-position: right;\n"
"   subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::add-line:vertical {\n"
"   border: 2px transparent grey;\n"
"   border-bottom-left-radius: 7px;\n"
"   border-bottom-right-radius: 7px;\n"
"   background: rgba(34, 142, 255, 255);\n"
"   height: 20px;\n"
"   subcontrol-position: bottom;\n"
"   subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::add-line:vertical:pressed {\n"
"   border: 2px transparent grey;\n"
"   border-bottom-left-radius: 7px;\n"
"   border-bottom-right-radius: 7px;\n"
"   background: rgb(181,181,181);\n"
"   height: 20px;\n"
"   subcontrol-position: bottom;\n"
"   subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"   border: 2px transparent grey;\n"
"   border-top-left-radius: 7px;\n"
"   border-bottom-left-radius: 7px;\n"
"   background: rgba(34, 142, 255, 255);\n"
"   width: 20px;\n"
"   subcontrol-position: left;\n"
"   subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal:pressed {\n"
"   border: 2px transparent grey;\n"
"   border-top-left-radius: 7px;\n"
"   border-bottom-left-radius: 7px;\n"
"   background: rgb(181,181,181);\n"
"   width: 20px;\n"
"   subcontrol-position: left;\n"
"   subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:vertical {\n"
"   border: 2px transparent grey;\n"
"   border-top-left-radius: 7px;\n"
"   border-top-right-radius: 7px;\n"
"   background: rgba(34, 142, 255, 255);\n"
"   height: 20px;\n"
"   subcontrol-position: top;\n"
"   subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:vertical:pressed {\n"
"   border: 2px transparent grey;\n"
"   border-top-left-radius: 7px;\n"
"   border-top-right-radius: 7px;\n"
"   background: rgb(181,181,181);\n"
"   height: 20px;\n"
"   subcontrol-position: top;\n"
"   subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::left-arrow:horizontal {\n"
"   border: 1px transparent grey;\n"
"   border-top-left-radius: 3px;\n"
"   border-bottom-left-radius: 3px;\n"
"   width: 6px;\n"
"   height: 6px;\n"
"   background: white;\n"
"}\n"
"QScrollBar::right-arrow:horizontal {\n"
"   border: 1px transparent grey;\n"
"   border-top-right-radius: 3px;\n"
"   border-bottom-right-radius: 3px;\n"
"   width: 6px;\n"
"   height: 6px;\n"
"   background: white;\n"
"}\n"
"QScrollBar::up-arrow:vertical {\n"
"   border: 1px transparent grey;\n"
"   border-top-left-radius: 3px;\n"
"   border-top-right-radius: 3px;\n"
"   width: 6px;\n"
"   height: 6px;\n"
"   background: white;\n"
"}\n"
"QScrollBar::down-arrow:vertical {\n"
"   border: 1px transparent grey;\n"
"   border-bottom-left-radius: 3px;\n"
"   border-bottom-right-radius: 3px;\n"
"   width: 6px;\n"
"   height: 6px;\n"
"   background: white;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {\n"
"   background: none;\n"
"}\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"   background: none;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(0, 0, 851, 461))
        self.groupBox.setObjectName("groupBox")
        self.lswSikayet = QtWidgets.QListWidget(self.groupBox)
        self.lswSikayet.setGeometry(QtCore.QRect(70, 260, 341, 192))
        self.lswSikayet.setObjectName("lswSikayet")
        item = QtWidgets.QListWidgetItem()
        self.lswSikayet.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.lswSikayet.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.lswSikayet.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.lswSikayet.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.lswSikayet.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.lswSikayet.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.lswSikayet.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.lswSikayet.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.lswSikayet.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.lswSikayet.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.lswSikayet.addItem(item)
        self.layoutWidget = QtWidgets.QWidget(self.groupBox)
        self.layoutWidget.setGeometry(QtCore.QRect(70, 180, 271, 24))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_7 = QtWidgets.QLabel(self.layoutWidget)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_6.addWidget(self.label_7)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem)
        self.cmbCinsiyet = QtWidgets.QComboBox(self.layoutWidget)
        self.cmbCinsiyet.setObjectName("cmbCinsiyet")
        self.cmbCinsiyet.addItem("")
        self.cmbCinsiyet.addItem("")
        self.horizontalLayout_6.addWidget(self.cmbCinsiyet)
        self.layoutWidget1 = QtWidgets.QWidget(self.groupBox)
        self.layoutWidget1.setGeometry(QtCore.QRect(70, 60, 271, 24))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.lneAd = QtWidgets.QLineEdit(self.layoutWidget1)
        self.lneAd.setObjectName("lneAd")
        self.horizontalLayout_2.addWidget(self.lneAd)
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(70, 240, 111, 16))
        self.label_5.setObjectName("label_5")
        self.layoutWidget2 = QtWidgets.QWidget(self.groupBox)
        self.layoutWidget2.setGeometry(QtCore.QRect(70, 30, 271, 24))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget2)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.lneTC = QtWidgets.QLineEdit(self.layoutWidget2)
        self.lneTC.setObjectName("lneTC")
        self.horizontalLayout.addWidget(self.lneTC)
        self.layoutWidget3 = QtWidgets.QWidget(self.groupBox)
        self.layoutWidget3.setGeometry(QtCore.QRect(70, 90, 271, 24))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget3)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.lneSoyad = QtWidgets.QLineEdit(self.layoutWidget3)
        self.lneSoyad.setObjectName("lneSoyad")
        self.horizontalLayout_3.addWidget(self.lneSoyad)
        self.layoutWidget4 = QtWidgets.QWidget(self.groupBox)
        self.layoutWidget4.setGeometry(QtCore.QRect(70, 120, 271, 24))
        self.layoutWidget4.setObjectName("layoutWidget4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.layoutWidget4)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_6 = QtWidgets.QLabel(self.layoutWidget4)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_4.addWidget(self.label_6)
        self.spnKilo = QtWidgets.QSpinBox(self.layoutWidget4)
        self.spnKilo.setObjectName("spnKilo")
        self.horizontalLayout_4.addWidget(self.spnKilo)
        self.label_9 = QtWidgets.QLabel(self.groupBox)
        self.label_9.setGeometry(QtCore.QRect(420, 40, 91, 16))
        self.label_9.setObjectName("label_9")
        self.clwDgTarihi = QtWidgets.QCalendarWidget(self.groupBox)
        self.clwDgTarihi.setGeometry(QtCore.QRect(420, 70, 421, 381))
        self.clwDgTarihi.setObjectName("clwDgTarihi")
        self.layoutWidget5 = QtWidgets.QWidget(self.groupBox)
        self.layoutWidget5.setGeometry(QtCore.QRect(70, 210, 271, 22))
        self.layoutWidget5.setObjectName("layoutWidget5")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.layoutWidget5)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_8 = QtWidgets.QLabel(self.layoutWidget5)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_7.addWidget(self.label_8)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem4)
        self.cbxMedeniHal = QtWidgets.QCheckBox(self.layoutWidget5)
        self.cbxMedeniHal.setObjectName("cbxMedeniHal")
        self.horizontalLayout_7.addWidget(self.cbxMedeniHal)
        self.layoutWidget6 = QtWidgets.QWidget(self.groupBox)
        self.layoutWidget6.setGeometry(QtCore.QRect(70, 150, 271, 24))
        self.layoutWidget6.setObjectName("layoutWidget6")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.layoutWidget6)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_4 = QtWidgets.QLabel(self.layoutWidget6)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_5.addWidget(self.label_4)
        self.cmbHastaneAdi = QtWidgets.QComboBox(self.layoutWidget6)
        self.cmbHastaneAdi.setObjectName("cmbHastaneAdi")
        self.cmbHastaneAdi.addItem("")
        self.cmbHastaneAdi.addItem("")
        self.cmbHastaneAdi.addItem("")
        self.cmbHastaneAdi.addItem("")
        self.cmbHastaneAdi.addItem("")
        self.cmbHastaneAdi.addItem("")
        self.cmbHastaneAdi.addItem("")
        self.cmbHastaneAdi.addItem("")
        self.horizontalLayout_5.addWidget(self.cmbHastaneAdi)
        self.tblwListe = QtWidgets.QTableWidget(self.centralwidget)
        self.tblwListe.setGeometry(QtCore.QRect(0, 460, 1081, 241))
        self.tblwListe.setRowCount(100)
        self.tblwListe.setColumnCount(10)
        self.tblwListe.setObjectName("tblwListe")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(14, 710, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.lblToplam = QtWidgets.QLabel(self.centralwidget)
        self.lblToplam.setGeometry(QtCore.QRect(180, 710, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lblToplam.setFont(font)
        self.lblToplam.setText("")
        self.lblToplam.setObjectName("lblToplam")
        self.layoutWidget7 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget7.setGeometry(QtCore.QRect(870, 20, 211, 441))
        self.layoutWidget7.setObjectName("layoutWidget7")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget7)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.btnEkle = QtWidgets.QPushButton(self.layoutWidget7)
        self.btnEkle.setObjectName("btnEkle")
        self.verticalLayout.addWidget(self.btnEkle)
        self.btnSil = QtWidgets.QPushButton(self.layoutWidget7)
        self.btnSil.setObjectName("btnSil")
        self.verticalLayout.addWidget(self.btnSil)
        self.btnGuncelle = QtWidgets.QPushButton(self.layoutWidget7)
        self.btnGuncelle.setObjectName("btnGuncelle")
        self.verticalLayout.addWidget(self.btnGuncelle)
        self.btnAra = QtWidgets.QPushButton(self.layoutWidget7)
        self.btnAra.setObjectName("btnAra")
        self.verticalLayout.addWidget(self.btnAra)
        self.btnListele = QtWidgets.QPushButton(self.layoutWidget7)
        self.btnListele.setObjectName("btnListele")
        self.verticalLayout.addWidget(self.btnListele)
        self.btnCikis = QtWidgets.QPushButton(self.layoutWidget7)
        self.btnCikis.setObjectName("btnCikis")
        self.verticalLayout.addWidget(self.btnCikis)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1092, 23))
        self.menubar.setObjectName("menubar")
        self.menuYard_m = QtWidgets.QMenu(self.menubar)
        self.menuYard_m.setObjectName("menuYard_m")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menuHakkinda = QtWidgets.QAction(MainWindow)
        self.menuHakkinda.setObjectName("menuHakkinda")
        self.menuYard_m.addAction(self.menuHakkinda)
        self.menubar.addAction(self.menuYard_m.menuAction())

        self.retranslateUi(MainWindow)
        self.cmbCinsiyet.setCurrentIndex(-1)
        self.cmbHastaneAdi.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "Hasta Bilgileri"))
        __sortingEnabled = self.lswSikayet.isSortingEnabled()
        self.lswSikayet.setSortingEnabled(False)
        item = self.lswSikayet.item(0)
        item.setText(_translate("MainWindow", "Şok"))
        item = self.lswSikayet.item(1)
        item.setText(_translate("MainWindow", "Kalp Ağrısı"))
        item = self.lswSikayet.item(2)
        item.setText(_translate("MainWindow", "Solunum Sıkıntısı"))
        item = self.lswSikayet.item(3)
        item.setText(_translate("MainWindow", "Zehirlenme"))
        item = self.lswSikayet.item(4)
        item.setText(_translate("MainWindow", "Doğum"))
        item = self.lswSikayet.item(5)
        item.setText(_translate("MainWindow", "Karın Ağrısı"))
        item = self.lswSikayet.item(6)
        item.setText(_translate("MainWindow", "Yanık"))
        item = self.lswSikayet.item(7)
        item.setText(_translate("MainWindow", "Kırık"))
        item = self.lswSikayet.item(8)
        item.setText(_translate("MainWindow", "Kanamalar"))
        item = self.lswSikayet.item(9)
        item.setText(_translate("MainWindow", "Baş Ağrısı"))
        item = self.lswSikayet.item(10)
        item.setText(_translate("MainWindow", "Soğuk Algınlığı Şikayetleri"))
        self.lswSikayet.setSortingEnabled(__sortingEnabled)
        self.label_7.setText(_translate("MainWindow", "Hastanın Cinsiyeti:"))
        self.cmbCinsiyet.setItemText(0, _translate("MainWindow", "Erkek"))
        self.cmbCinsiyet.setItemText(1, _translate("MainWindow", "Kadın"))
        self.label_2.setText(_translate("MainWindow", "Hastanın Adı:"))
        self.label_5.setText(_translate("MainWindow", "Hastanın Şikayeti:"))
        self.label.setText(_translate("MainWindow", "TC KİMLİK NUMARASI:"))
        self.label_3.setText(_translate("MainWindow", "Hastanın Soyadı:"))
        self.label_6.setText(_translate("MainWindow", "Hastanın Kilosu:"))
        self.label_9.setText(_translate("MainWindow", "Doğum Tarihi:"))
        self.label_8.setText(_translate("MainWindow", "Hastanın Medeni Hali:"))
        self.cbxMedeniHal.setText(_translate("MainWindow", "Evli"))
        self.label_4.setText(_translate("MainWindow", "Hastane Adı:"))
        self.cmbHastaneAdi.setItemText(0, _translate("MainWindow", "Aşkale Devlet Hastanesi"))
        self.cmbHastaneAdi.setItemText(1, _translate("MainWindow", "Erzurum Bölge Eğitim Araştırma Hastanesi"))
        self.cmbHastaneAdi.setItemText(2, _translate("MainWindow", "Mareşal Çakmak Devlet Hastanesi"))
        self.cmbHastaneAdi.setItemText(3, _translate("MainWindow", "Ataturk Üniversitesi Sağlık Hastanesi"))
        self.cmbHastaneAdi.setItemText(4, _translate("MainWindow", "Aziziye Kadın Doğum ve Çocuk Hastalıkları Hastanesi"))
        self.cmbHastaneAdi.setItemText(5, _translate("MainWindow", "Erzurum Palandöken Devlet Hastanesi"))
        self.cmbHastaneAdi.setItemText(6, _translate("MainWindow", "Özel Buhara Hastanesi"))
        self.cmbHastaneAdi.setItemText(7, _translate("MainWindow", "Horasan Devlet Hastanesi"))
        self.label_10.setText(_translate("MainWindow", "KAYIT SAYISI:"))
        self.btnEkle.setText(_translate("MainWindow", "KAYIT EKLE"))
        self.btnSil.setText(_translate("MainWindow", "KAYIT SİL"))
        self.btnGuncelle.setText(_translate("MainWindow", "KAYIT GÜNCELLE"))
        self.btnAra.setText(_translate("MainWindow", "KAYIT ARA"))
        self.btnListele.setText(_translate("MainWindow", "KAYIT LİSTELE"))
        self.btnCikis.setText(_translate("MainWindow", "ÇIKIŞ"))
        self.menuYard_m.setTitle(_translate("MainWindow", "Yardım"))
        self.menuHakkinda.setText(_translate("MainWindow", "Hakkında"))
