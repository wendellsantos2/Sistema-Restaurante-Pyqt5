# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new_register_window.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import new_register_img_rc

class Ui_new_register_window(object):
    def setupUi(self, new_register_window):
        if not new_register_window.objectName():
            new_register_window.setObjectName(u"new_register_window")
        new_register_window.resize(800, 600)
        new_register_window.setMaximumSize(QSize(800, 600))
        new_register_window.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 97, 117, 255), stop:1 rgba(255, 255, 255, 255));")
        self.centralwidget = QWidget(new_register_window)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(10, 10, 771, 581))
        self.frame.setStyleSheet(u"background:rgba(0,0,0,0.5);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 0, 771, 81))
        self.label.setStyleSheet(u"background:transparent;\n"
"font-family: Trebuchet MS;\n"
"font-weight: bold;\n"
"font-size:25px;\n"
"color:white;\n"
"text-decoration:underline;")
        self.label.setAlignment(Qt.AlignCenter)
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(50, 120, 141, 31))
        self.label_2.setStyleSheet(u"background:transparent;\n"
"color:white;\n"
"font-family: Trebuchet MS;\n"
"font-size:18px;\n"
"")
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(50, 150, 141, 31))
        self.label_3.setStyleSheet(u"background:transparent;\n"
"color:white;\n"
"font-family: Trebuchet MS;\n"
"font-size:18px;\n"
"")
        self.label_3.setAlignment(Qt.AlignCenter)
        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(50, 180, 141, 31))
        self.label_4.setStyleSheet(u"background:transparent;\n"
"color:white;\n"
"font-family: Trebuchet MS;\n"
"font-size:18px;\n"
"")
        self.label_4.setAlignment(Qt.AlignCenter)
        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(30, 210, 181, 31))
        self.label_5.setStyleSheet(u"background:transparent;\n"
"color:white;\n"
"font-family: Trebuchet MS;\n"
"font-size:18px;\n"
"")
        self.label_5.setAlignment(Qt.AlignCenter)
        self.label_6 = QLabel(self.frame)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(50, 240, 141, 31))
        self.label_6.setStyleSheet(u"background:transparent;\n"
"color:white;\n"
"font-family: Trebuchet MS;\n"
"font-size:18px;\n"
"")
        self.label_6.setAlignment(Qt.AlignCenter)
        self.label_7 = QLabel(self.frame)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(50, 270, 141, 31))
        self.label_7.setStyleSheet(u"background:transparent;\n"
"color:white;\n"
"font-family: Trebuchet MS;\n"
"font-size:18px;\n"
"")
        self.label_7.setAlignment(Qt.AlignCenter)
        self.new_name = QLineEdit(self.frame)
        self.new_name.setObjectName(u"new_name")
        self.new_name.setGeometry(QRect(260, 120, 321, 21))
        self.new_name.setStyleSheet(u"background:transparent;\n"
"color:white;\n"
"font-family:Trebuchet MS;\n"
"font-size:18px;\n"
"border:none;\n"
"border-bottom:0.5px solid white;")
        self.new_email = QLineEdit(self.frame)
        self.new_email.setObjectName(u"new_email")
        self.new_email.setGeometry(QRect(260, 150, 321, 21))
        self.new_email.setStyleSheet(u"background:transparent;\n"
"color:white;\n"
"font-family:Trebuchet MS;\n"
"font-size:18px;\n"
"border:none;\n"
"border-bottom:0.5px solid white;")
        self.new_text = QLineEdit(self.frame)
        self.new_text.setObjectName(u"new_text")
        self.new_text.setGeometry(QRect(260, 180, 321, 21))
        self.new_text.setStyleSheet(u"background:transparent;\n"
"color:white;\n"
"font-family:Trebuchet MS;\n"
"font-size:18px;\n"
"border:none;\n"
"border-bottom:0.5px solid white;")
        self.new_dateofbirth = QLineEdit(self.frame)
        self.new_dateofbirth.setObjectName(u"new_dateofbirth")
        self.new_dateofbirth.setGeometry(QRect(260, 210, 321, 21))
        self.new_dateofbirth.setStyleSheet(u"background:transparent;\n"
"color:white;\n"
"font-family:Trebuchet MS;\n"
"font-size:18px;\n"
"border:none;\n"
"border-bottom:0.5px solid white;")
        self.new_user = QLineEdit(self.frame)
        self.new_user.setObjectName(u"new_user")
        self.new_user.setGeometry(QRect(260, 240, 321, 21))
        self.new_user.setStyleSheet(u"background:transparent;\n"
"color:white;\n"
"font-family:Trebuchet MS;\n"
"font-size:18px;\n"
"border:none;\n"
"border-bottom:0.5px solid white;")
        self.new_password = QLineEdit(self.frame)
        self.new_password.setObjectName(u"new_password")
        self.new_password.setGeometry(QRect(260, 270, 321, 21))
        self.new_password.setStyleSheet(u"background:transparent;\n"
"color:white;\n"
"font-family:Trebuchet MS;\n"
"font-size:18px;\n"
"border:none;\n"
"border-bottom:0.5px solid white;")
        self.new_password.setEchoMode(QLineEdit.Password)
        self.new_register_save_button = QPushButton(self.frame)
        self.new_register_save_button.setObjectName(u"new_register_save_button")
        self.new_register_save_button.setGeometry(QRect(250, 360, 131, 41))
        self.new_register_save_button.setCursor(QCursor(Qt.OpenHandCursor))
        self.new_register_save_button.setStyleSheet(u"QPushButton{\n"
"background:#1E90FF;\n"
"color:white;\n"
"font-family:Trebuchet MS;\n"
"font-size:16px;\n"
"font-weight:bold;\n"
"border-radius:10px;\n"
"}\n"
"QPushButton:hover{\n"
"background:#4169E1;\n"
"}")
        icon = QIcon()
        icon.addFile(u":/img/save.png", QSize(), QIcon.Normal, QIcon.Off)
        self.new_register_save_button.setIcon(icon)
        self.new_register_save_button.setIconSize(QSize(16, 16))
        self.new_register_close_button = QPushButton(self.frame)
        self.new_register_close_button.setObjectName(u"new_register_close_button")
        self.new_register_close_button.setGeometry(QRect(440, 360, 131, 41))
        self.new_register_close_button.setCursor(QCursor(Qt.OpenHandCursor))
        self.new_register_close_button.setStyleSheet(u"QPushButton{\n"
"background:#1E90FF;\n"
"color:white;\n"
"font-family:Trebuchet MS;\n"
"font-size:16px;\n"
"font-weight:bold;\n"
"border-radius:10px;\n"
"}\n"
"QPushButton:hover{\n"
"background:#4169E1;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/img/close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.new_register_close_button.setIcon(icon1)
        self.new_register_close_button.setIconSize(QSize(28, 28))
        self.return_saved_label = QLabel(self.frame)
        self.return_saved_label.setObjectName(u"return_saved_label")
        self.return_saved_label.setGeometry(QRect(150, 470, 511, 31))
        self.return_saved_label.setStyleSheet(u"background:transparent;\n"
"color:white;\n"
"font-family: Trebuchet MS;\n"
"font-size:18px;\n"
"")
        self.return_saved_label.setAlignment(Qt.AlignCenter)
        new_register_window.setCentralWidget(self.centralwidget)

        self.retranslateUi(new_register_window)

        QMetaObject.connectSlotsByName(new_register_window)
    # setupUi

    def retranslateUi(self, new_register_window):
        new_register_window.setWindowTitle(QCoreApplication.translate("new_register_window", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("new_register_window", u"CADASTRAR NOVO USUARIO", None))
        self.label_2.setText(QCoreApplication.translate("new_register_window", u"Nome:", None))
        self.label_3.setText(QCoreApplication.translate("new_register_window", u"Email:", None))
        self.label_4.setText(QCoreApplication.translate("new_register_window", u"Telefone:", None))
        self.label_5.setText(QCoreApplication.translate("new_register_window", u"Data de nascimento:", None))
        self.label_6.setText(QCoreApplication.translate("new_register_window", u"Usuario:", None))
        self.label_7.setText(QCoreApplication.translate("new_register_window", u"Senha:", None))
        self.new_register_save_button.setText(QCoreApplication.translate("new_register_window", u" Salvar", None))
        self.new_register_close_button.setText(QCoreApplication.translate("new_register_window", u"Fechar", None))
        self.return_saved_label.setText("")
    # retranslateUi

