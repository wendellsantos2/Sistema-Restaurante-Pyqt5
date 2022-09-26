# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login_window.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import resources_rc

class Ui_login_window(object):
    def setupUi(self, login_window):
        if not login_window.objectName():
            login_window.setObjectName(u"login_window")
        login_window.setEnabled(True)
        login_window.resize(1200, 700)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(login_window.sizePolicy().hasHeightForWidth())
        login_window.setSizePolicy(sizePolicy)
        login_window.setMaximumSize(QSize(1200, 700))
        icon = QIcon()
        icon.addFile(u"../static/img/window_icon.ico", QSize(), QIcon.Normal, QIcon.Off)
        login_window.setWindowIcon(icon)
        login_window.setLayoutDirection(Qt.LeftToRight)
        login_window.setStyleSheet(u"QWidget{\n"
"background: url(:/newPrefix/login_wallpaper.jpg);\n"
"}")
        login_window.setIconSize(QSize(32, 32))
        self.centralwidget = QWidget(login_window)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMaximumSize(QSize(9999, 9999))
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(380, 330, 450, 350))
        self.frame.setStyleSheet(u"background:rgba(0,0,0,0.8);\n"
"border: 0.5px solid black;\n"
"border-radius: 10px;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 90, 101, 61))
        self.label.setStyleSheet(u"background:transparent;\n"
"font-family: Trebuchet MS;\n"
"font-size:18px;\n"
"color:white;\n"
"border:none;")
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 170, 101, 61))
        self.label_2.setStyleSheet(u"background:transparent;\n"
"font-family: Trebuchet MS;\n"
"font-size:18px;\n"
"color:white;\n"
"border:none;")
        self.login_input = QLineEdit(self.frame)
        self.login_input.setObjectName(u"login_input")
        self.login_input.setGeometry(QRect(140, 110, 231, 20))
        self.login_input.setStyleSheet(u"background:transparent;\n"
"border:none;\n"
"border-bottom:0.5px solid white;\n"
"border-radius:0px;\n"
"color:white;\n"
"font-size:18px;")
        self.password_input = QLineEdit(self.frame)
        self.password_input.setObjectName(u"password_input")
        self.password_input.setGeometry(QRect(140, 190, 231, 20))
        self.password_input.setStyleSheet(u"background:transparent;\n"
"border:none;\n"
"border-bottom:0.5px solid white;\n"
"border-radius:0px;\n"
"color:white;\n"
"font-size:18px;")
        self.password_input.setEchoMode(QLineEdit.Password)
        self.login_button = QPushButton(self.frame)
        self.login_button.setObjectName(u"login_button")
        self.login_button.setGeometry(QRect(100, 262, 131, 41))
        sizePolicy.setHeightForWidth(self.login_button.sizePolicy().hasHeightForWidth())
        self.login_button.setSizePolicy(sizePolicy)
        self.login_button.setCursor(QCursor(Qt.OpenHandCursor))
        self.login_button.setStyleSheet(u"QPushButton{\n"
"background:#1E90FF;\n"
"color:white;\n"
"font-family: Trebuchet MS;\n"
"font-weight:bold;\n"
"font-size:14px;\n"
"}\n"
"QPushButton:hover{\n"
"background:#4169E1;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/newPrefix/login_button.png", QSize(), QIcon.Normal, QIcon.Off)
        self.login_button.setIcon(icon1)
        self.login_button.setIconSize(QSize(16, 16))
        self.new_register_button = QPushButton(self.frame)
        self.new_register_button.setObjectName(u"new_register_button")
        self.new_register_button.setGeometry(QRect(250, 260, 131, 41))
        self.new_register_button.setCursor(QCursor(Qt.OpenHandCursor))
        self.new_register_button.setStyleSheet(u"QPushButton{\n"
"background:#1E90FF;\n"
"color:white;\n"
"font-family: Trebuchet MS;\n"
"font-weight:bold;\n"
"font-size:14px\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background:#4169E1;\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/newPrefix/cadastrar_button.png", QSize(), QIcon.Normal, QIcon.Off)
        self.new_register_button.setIcon(icon2)
        self.new_register_button.setIconSize(QSize(16, 16))
        self.toolButton = QToolButton(self.centralwidget)
        self.toolButton.setObjectName(u"toolButton")
        self.toolButton.setGeometry(QRect(-10, 0, 1161, 221))
        self.toolButton.setStyleSheet(u"background: transparent;")
        icon3 = QIcon()
        icon3.addFile(u":/newPrefix/logo.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton.setIcon(icon3)
        self.toolButton.setIconSize(QSize(1200, 1200))
        self.toolButton_2 = QToolButton(self.centralwidget)
        self.toolButton_2.setObjectName(u"toolButton_2")
        self.toolButton_2.setGeometry(QRect(520, 260, 161, 121))
        self.toolButton_2.setStyleSheet(u"background:transparent;")
        icon4 = QIcon()
        icon4.addFile(u":/newPrefix/login_user.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_2.setIcon(icon4)
        self.toolButton_2.setIconSize(QSize(100, 100))
        login_window.setCentralWidget(self.centralwidget)

        self.retranslateUi(login_window)

        QMetaObject.connectSlotsByName(login_window)
    # setupUi

    def retranslateUi(self, login_window):
        login_window.setWindowTitle(QCoreApplication.translate("login_window", u"Restaurantes Requinte", None))
        self.label.setText(QCoreApplication.translate("login_window", u"Usuario:", None))
        self.label_2.setText(QCoreApplication.translate("login_window", u"Senha:", None))
        self.password_input.setInputMask("")
        self.login_button.setText(QCoreApplication.translate("login_window", u" Confirmar", None))
        self.new_register_button.setText(QCoreApplication.translate("login_window", u" Cadastrar", None))
        self.toolButton.setText(QCoreApplication.translate("login_window", u"...", None))
        self.toolButton_2.setText(QCoreApplication.translate("login_window", u"...", None))
    # retranslateUi

