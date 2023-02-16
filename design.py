# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'design.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QMenuBar, QProgressBar, QPushButton, QSizePolicy,
    QStatusBar, QWidget)


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 545)
        icon = QIcon()
        icon.addFile(u"../../../Downloads/favicon (2).ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"QProgressBar::chunk {\n"
"    background-color: #5B76D7;\n"
"}\n"
"")
        MainWindow.setIconSize(QSize(30, 30))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(20, 80, 351, 41))
        self.lineEdit.setStyleSheet(u"border: 3px solid gray;\n"
"border-radius: 10px;\n"
"font-size:15px;\n"
"")
        self.lineEdit.setAlignment(Qt.AlignCenter)
        self.lineEdit_2 = QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(420, 80, 351, 41))
        self.lineEdit_2.setStyleSheet(u"border: 3px solid gray;\n"
"border-radius: 10px;\n"
"font-size:15px;")
        self.lineEdit_2.setAlignment(Qt.AlignCenter)
        self.lineEdit_3 = QLineEdit(self.centralwidget)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(20, 200, 581, 41))
        self.lineEdit_3.setStyleSheet(u"border: 3px solid gray;\n"
"border-radius: 10px;\n"
"font-size:15px;")
        self.lineEdit_3.setAlignment(Qt.AlignCenter)
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(620, 190, 141, 51))
        self.pushButton.setStyleSheet(u"border: 3px solid gray;\n"
"border-radius: 10px;\n"
"background-color: #5B76D7;\n"
"font-size: 15px")
        icon1 = QIcon()
        icon1.addFile(u"../../../Downloads/favicon (1).ico", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(30, 423, 731, 51))
        self.pushButton_2.setStyleSheet(u"border: 3px solid gray;\n"
"border-radius: 10px;\n"
"background-color: #3353CC;\n"
"font-size: 25px")
        icon2 = QIcon()
        icon2.addFile(u"../../../Downloads/favicon.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon2)
        self.pushButton_2.setIconSize(QSize(30, 30))
        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(40, 342, 711, 31))
        self.progressBar.setStyleSheet(u"border: 3px solid gray;\n"
"border-radius: 10px;\n"
"font-size: 15px")
        self.progressBar.setValue(0)
        self.progressBar.setAlignment(Qt.AlignCenter)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(40, 279, 711, 31))
        self.label.setStyleSheet(u"font-size:15px;")
        self.label.setAlignment(Qt.AlignCenter)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 19, 351, 41))
        self.label_2.setStyleSheet(u"font-size:25px;")
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(420, 30, 351, 31))
        self.label_3.setStyleSheet(u"font-size:25px;")
        self.label_3.setAlignment(Qt.AlignCenter)
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(30, 149, 721, 31))
        self.label_4.setStyleSheet(u"font-size:25px;")
        self.label_4.setAlignment(Qt.AlignCenter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"AutoSub", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Open Folder", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Open File", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Input Language", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Output Language", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Please Select The Output Folder", None))
    # retranslateUi

