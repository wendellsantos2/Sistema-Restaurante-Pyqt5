# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'menu.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_menu_window(object):
    def setupUi(self, menu_window):
        if not menu_window.objectName():
            menu_window.setObjectName(u"menu_window")
        menu_window.setWindowModality(Qt.NonModal)
        menu_window.setEnabled(True)
        menu_window.resize(1200, 700)
        menu_window.setMaximumSize(QSize(1200, 700))
        icon = QIcon()
        iconThemeName = u":/menu/window_icon.ico"
        if QIcon.hasThemeIcon(iconThemeName):
            icon = QIcon.fromTheme(iconThemeName)
        else:
            icon.addFile(u":/menu/window_icon.ico", QSize(), QIcon.Normal, QIcon.Off)
        
        menu_window.setWindowIcon(icon)
        menu_window.setStyleSheet(u"QWidget{\n"
"background:url(:/menu/menu_wallpaper.jpg);\n"
"}")
        menu_window.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.centralwidget = QWidget(menu_window)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMaximumSize(QSize(1200, 700))
        self.centralwidget.setStyleSheet(u"")
        self.frame_bar = QFrame(self.centralwidget)
        self.frame_bar.setObjectName(u"frame_bar")
        self.frame_bar.setGeometry(QRect(0, 0, 1200, 52))
        self.frame_bar.setMaximumSize(QSize(1200, 100))
        self.frame_bar.setStyleSheet(u"border: 1px solid black;\n"
"background: transparent;\n"
"border:none;")
        self.frame_bar.setFrameShape(QFrame.StyledPanel)
        self.frame_bar.setFrameShadow(QFrame.Raised)
        self.label_welcome = QLabel(self.frame_bar)
        self.label_welcome.setObjectName(u"label_welcome")
        self.label_welcome.setGeometry(QRect(30, 30, 260, 23))
        self.label_welcome.setStyleSheet(u"font-family: Trebuchet MS;\n"
"font-size: 15px;\n"
"font-weight: bold;\n"
"color: white;\n"
"border:none;\n"
"text-decoration:underline;\n"
"")
        self.label_welcome.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.button_pedido = QPushButton(self.frame_bar)
        self.button_pedido.setObjectName(u"button_pedido")
        self.button_pedido.setGeometry(QRect(300, 30, 101, 23))
        self.button_pedido.setCursor(QCursor(Qt.OpenHandCursor))
        self.button_pedido.setStyleSheet(u"QPushButton{\n"
"border:none;\n"
"font-family: Trebuchet MS;\n"
"font-size:14px;\n"
"color:white;\n"
"font-weight: bold;\n"
"border-left:1px solid white;\n"
"border-right: 1px solid white;\n"
"background-color:rgba(255,255,255,0.2);\n"
"}\n"
"QPushButton:hover{\n"
"text-decoration:underline;\n"
"background-color:rgba(255,255,255,0.6);\n"
"}\n"
"")
        icon1 = QIcon()
        icon1.addFile(u":/menu/pedido_button.png", QSize(), QIcon.Normal, QIcon.Off)
        self.button_pedido.setIcon(icon1)
        self.button_caixa = QPushButton(self.frame_bar)
        self.button_caixa.setObjectName(u"button_caixa")
        self.button_caixa.setGeometry(QRect(410, 30, 101, 23))
        self.button_caixa.setCursor(QCursor(Qt.OpenHandCursor))
        self.button_caixa.setStyleSheet(u"QPushButton{\n"
"border:none;\n"
"font-family: Trebuchet MS;\n"
"font-size:14px;\n"
"color:white;\n"
"font-weight: bold;\n"
"border-left: 1px solid white;\n"
"border-right: 1px solid white;\n"
"background-color:rgba(255,255,255,0.2);\n"
"}\n"
"QPushButton:hover{\n"
"text-decoration:underline;\n"
"background-color:rgba(255,255,255,0.6);\n"
"}\n"
"")
        icon2 = QIcon()
        icon2.addFile(u":/menu/caixa_button.png", QSize(), QIcon.Normal, QIcon.Off)
        self.button_caixa.setIcon(icon2)
        self.button_mesas = QPushButton(self.frame_bar)
        self.button_mesas.setObjectName(u"button_mesas")
        self.button_mesas.setGeometry(QRect(520, 30, 101, 23))
        self.button_mesas.setCursor(QCursor(Qt.OpenHandCursor))
        self.button_mesas.setStyleSheet(u"QPushButton{\n"
"border:none;\n"
"font-family: Trebuchet MS;\n"
"font-size:14px;\n"
"color:white;\n"
"font-weight: bold;\n"
"border-left:1px solid white;\n"
"border-right: 1px solid white;\n"
"background-color:rgba(255,255,255,0.2);\n"
"}\n"
"QPushButton:hover{\n"
"text-decoration:underline;\n"
"background-color:rgba(255,255,255,0.6);\n"
"}\n"
"")
        icon3 = QIcon()
        icon3.addFile(u":/menu/mesa_button.png", QSize(), QIcon.Normal, QIcon.Off)
        self.button_mesas.setIcon(icon3)
        self.button_mesas.setIconSize(QSize(20, 20))
        self.button_produtos = QPushButton(self.frame_bar)
        self.button_produtos.setObjectName(u"button_produtos")
        self.button_produtos.setGeometry(QRect(630, 30, 101, 23))
        self.button_produtos.setCursor(QCursor(Qt.OpenHandCursor))
        self.button_produtos.setStyleSheet(u"QPushButton{\n"
"border:none;\n"
"font-family: Trebuchet MS;\n"
"font-size:14px;\n"
"color:white;\n"
"font-weight: bold;\n"
"border-left:1px solid white;\n"
"border-right: 1px solid white;\n"
"background-color:rgba(255,255,255,0.2);\n"
"}\n"
"QPushButton:hover{\n"
"text-decoration:underline;\n"
"background-color:rgba(255,255,255,0.6);\n"
"}\n"
"")
        icon4 = QIcon()
        icon4.addFile(u":/menu/produtos_button.png", QSize(), QIcon.Normal, QIcon.Off)
        self.button_produtos.setIcon(icon4)
        self.button_relatorio = QPushButton(self.frame_bar)
        self.button_relatorio.setObjectName(u"button_relatorio")
        self.button_relatorio.setGeometry(QRect(740, 30, 101, 23))
        self.button_relatorio.setCursor(QCursor(Qt.OpenHandCursor))
        self.button_relatorio.setStyleSheet(u"QPushButton{\n"
"border:none;\n"
"font-family: Trebuchet MS;\n"
"font-size:14px;\n"
"color:white;\n"
"font-weight: bold;\n"
"border-left:1px solid white;\n"
"border-right: 1px solid white;\n"
"background-color:rgba(255,255,255,0.2);\n"
"}\n"
"QPushButton:hover{\n"
"text-decoration:underline;\n"
"background-color:rgba(255,255,255,0.6);\n"
"}\n"
"")
        icon5 = QIcon()
        icon5.addFile(u":/menu/relatorio_button.png", QSize(), QIcon.Normal, QIcon.Off)
        self.button_relatorio.setIcon(icon5)
        self.button_cliente = QPushButton(self.frame_bar)
        self.button_cliente.setObjectName(u"button_cliente")
        self.button_cliente.setGeometry(QRect(850, 30, 101, 23))
        self.button_cliente.setCursor(QCursor(Qt.OpenHandCursor))
        self.button_cliente.setStyleSheet(u"QPushButton{\n"
"border:none;\n"
"font-family: Trebuchet MS;\n"
"font-size:14px;\n"
"color:white;\n"
"font-weight: bold;\n"
"border-left:1px solid white;\n"
"border-right: 1px solid white;\n"
"background-color:rgba(255,255,255,0.2);\n"
"}\n"
"QPushButton:hover{\n"
"text-decoration:underline;\n"
"background-color:rgba(255,255,255,0.6);\n"
"}\n"
"")
        icon6 = QIcon()
        icon6.addFile(u":/menu/icon-estoque.png", QSize(), QIcon.Normal, QIcon.Off)
        self.button_cliente.setIcon(icon6)
        self.button_cliente.setIconSize(QSize(20, 20))
        self.button_usuario = QPushButton(self.frame_bar)
        self.button_usuario.setObjectName(u"button_usuario")
        self.button_usuario.setGeometry(QRect(960, 30, 101, 23))
        self.button_usuario.setCursor(QCursor(Qt.OpenHandCursor))
        self.button_usuario.setStyleSheet(u"QPushButton{\n"
"border:none;\n"
"font-family: Trebuchet MS;\n"
"font-size:14px;\n"
"color:white;\n"
"font-weight: bold;\n"
"border-left:1px solid white;\n"
"border-right: 1px solid white;\n"
"background-color:rgba(255,255,255,0.2);\n"
"}\n"
"QPushButton:hover{\n"
"text-decoration:underline;\n"
"background-color:rgba(255,255,255,0.6);\n"
"}\n"
"")
        icon7 = QIcon()
        icon7.addFile(u":/menu/developer.png", QSize(), QIcon.Normal, QIcon.Off)
        self.button_usuario.setIcon(icon7)
        self.f_inicio = QFrame(self.centralwidget)
        self.f_inicio.setObjectName(u"f_inicio")
        self.f_inicio.setEnabled(True)
        self.f_inicio.setGeometry(QRect(5, 90, 1190, 600))
        self.f_inicio.setStyleSheet(u"background:rgba(0,0,0,0.5);\n"
"border-radius:10px;\n"
"")
        self.f_inicio.setFrameShape(QFrame.StyledPanel)
        self.f_inicio.setFrameShadow(QFrame.Raised)
        self.f_pedidos = QFrame(self.centralwidget)
        self.f_pedidos.setObjectName(u"f_pedidos")
        self.f_pedidos.setEnabled(True)
        self.f_pedidos.setGeometry(QRect(5, 90, 1190, 600))
        self.f_pedidos.setStyleSheet(u"background:rgba(0,0,0,0.5);\n"
"border-radius:10px;")
        self.f_pedidos.setFrameShape(QFrame.StyledPanel)
        self.f_pedidos.setFrameShadow(QFrame.Raised)
        self.frame = QFrame(self.f_pedidos)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(10, 10, 231, 111))
        self.frame.setStyleSheet(u"background:#6959CD;\n"
"font-family: Trebuchet MS;\n"
"font-size:14px;\n"
"font-weight:bold;\n"
"\n"
"\n"
"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 0, 231, 41))
        self.label.setStyleSheet(u"background:transparent;")
        self.label.setAlignment(Qt.AlignCenter)
        self.box_mesas = QComboBox(self.frame)
        self.box_mesas.addItem("")
        self.box_mesas.addItem("")
        self.box_mesas.addItem("")
        self.box_mesas.addItem("")
        self.box_mesas.addItem("")
        self.box_mesas.addItem("")
        self.box_mesas.addItem("")
        self.box_mesas.addItem("")
        self.box_mesas.addItem("")
        self.box_mesas.addItem("")
        self.box_mesas.addItem("")
        self.box_mesas.addItem("")
        self.box_mesas.addItem("")
        self.box_mesas.addItem("")
        self.box_mesas.addItem("")
        self.box_mesas.addItem("")
        self.box_mesas.addItem("")
        self.box_mesas.addItem("")
        self.box_mesas.addItem("")
        self.box_mesas.addItem("")
        self.box_mesas.addItem("")
        self.box_mesas.addItem("")
        self.box_mesas.addItem("")
        self.box_mesas.addItem("")
        self.box_mesas.addItem("")
        self.box_mesas.addItem("")
        self.box_mesas.addItem("")
        self.box_mesas.addItem("")
        self.box_mesas.addItem("")
        self.box_mesas.addItem("")
        self.box_mesas.addItem("")
        self.box_mesas.addItem("")
        self.box_mesas.addItem("")
        self.box_mesas.addItem("")
        self.box_mesas.addItem("")
        self.box_mesas.addItem("")
        self.box_mesas.addItem("")
        self.box_mesas.addItem("")
        self.box_mesas.addItem("")
        self.box_mesas.addItem("")
        self.box_mesas.addItem("")
        self.box_mesas.addItem("")
        self.box_mesas.addItem("")
        self.box_mesas.addItem("")
        self.box_mesas.addItem("")
        self.box_mesas.addItem("")
        self.box_mesas.addItem("")
        self.box_mesas.addItem("")
        self.box_mesas.addItem("")
        self.box_mesas.addItem("")
        self.box_mesas.addItem("")
        self.box_mesas.addItem("")
        self.box_mesas.setObjectName(u"box_mesas")
        self.box_mesas.setGeometry(QRect(70, 50, 81, 31))
        self.box_mesas.setStyleSheet(u"background:white;\n"
"border-radius:2px;\n"
"border:1px solid white;")
        self.frame_2 = QFrame(self.f_pedidos)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(280, 10, 891, 111))
        self.frame_2.setStyleSheet(u"background:#6959CD;\n"
"font-family: Trebuchet MS;\n"
"font-size:14px;\n"
"font-weight:bold;\n"
"")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.adicionar_button = QPushButton(self.frame_2)
        self.adicionar_button.setObjectName(u"adicionar_button")
        self.adicionar_button.setGeometry(QRect(50, 20, 101, 71))
        self.adicionar_button.setCursor(QCursor(Qt.OpenHandCursor))
        self.adicionar_button.setStyleSheet(u"QPushButton{\n"
"font-family: Trebuchet MS;\n"
"font-size:14px;\n"
"color:white;\n"
"font-weight: bold;\n"
"border:1px solid white;\n"
"background-color:rgba(255,255,255,0.2);\n"
"border-radius:10px;\n"
"}\n"
"QPushButton:hover{\n"
"text-decoration:underline;\n"
"background-color:rgba(255,255,255,0.6);\n"
"\n"
"}\n"
"")
        icon8 = QIcon()
        icon8.addFile(u":/menu/adicionar_button.png", QSize(), QIcon.Normal, QIcon.Off)
        self.adicionar_button.setIcon(icon8)
        self.adicionar_button.setIconSize(QSize(64, 64))
        self.editar_button = QPushButton(self.frame_2)
        self.editar_button.setObjectName(u"editar_button")
        self.editar_button.setGeometry(QRect(210, 20, 101, 71))
        self.editar_button.setCursor(QCursor(Qt.OpenHandCursor))
        self.editar_button.setStyleSheet(u"QPushButton{\n"
"font-family: Trebuchet MS;\n"
"font-size:14px;\n"
"color:white;\n"
"font-weight: bold;\n"
"border:1px solid white;\n"
"background-color:rgba(255,255,255,0.2);\n"
"border-radius:10px;\n"
"}\n"
"QPushButton:hover{\n"
"text-decoration:underline;\n"
"background-color:rgba(255,255,255,0.6);\n"
"\n"
"}\n"
"")
        icon9 = QIcon()
        icon9.addFile(u":/menu/editar_button.png", QSize(), QIcon.Normal, QIcon.Off)
        self.editar_button.setIcon(icon9)
        self.editar_button.setIconSize(QSize(80, 80))
        self.delete_button = QPushButton(self.frame_2)
        self.delete_button.setObjectName(u"delete_button")
        self.delete_button.setGeometry(QRect(370, 20, 101, 71))
        self.delete_button.setCursor(QCursor(Qt.OpenHandCursor))
        self.delete_button.setStyleSheet(u"QPushButton{\n"
"font-family: Trebuchet MS;\n"
"font-size:14px;\n"
"color:white;\n"
"font-weight: bold;\n"
"border:1px solid white;\n"
"background-color:rgba(255,255,255,0.2);\n"
"border-radius:10px;\n"
"}\n"
"QPushButton:hover{\n"
"text-decoration:underline;\n"
"background-color:rgba(255,255,255,0.6);\n"
"\n"
"}\n"
"")
        icon10 = QIcon()
        icon10.addFile(u":/menu/deletar_button.png", QSize(), QIcon.Normal, QIcon.Off)
        self.delete_button.setIcon(icon10)
        self.delete_button.setIconSize(QSize(64, 64))
        self.table_button = QPushButton(self.frame_2)
        self.table_button.setObjectName(u"table_button")
        self.table_button.setGeometry(QRect(530, 20, 101, 71))
        self.table_button.setCursor(QCursor(Qt.OpenHandCursor))
        self.table_button.setStyleSheet(u"QPushButton{\n"
"font-family: Trebuchet MS;\n"
"font-size:14px;\n"
"color:white;\n"
"font-weight: bold;\n"
"border:1px solid white;\n"
"background-color:rgba(255,255,255,0.2);\n"
"border-radius:10px;\n"
"}\n"
"QPushButton:hover{\n"
"text-decoration:underline;\n"
"background-color:rgba(255,255,255,0.6);\n"
"\n"
"}\n"
"")
        icon11 = QIcon()
        icon11.addFile(u":/menu/mesa2_button.png", QSize(), QIcon.Normal, QIcon.Off)
        self.table_button.setIcon(icon11)
        self.table_button.setIconSize(QSize(64, 64))
        self.table_button_2 = QPushButton(self.frame_2)
        self.table_button_2.setObjectName(u"table_button_2")
        self.table_button_2.setGeometry(QRect(690, 20, 101, 71))
        self.table_button_2.setCursor(QCursor(Qt.OpenHandCursor))
        self.table_button_2.setStyleSheet(u"QPushButton{\n"
"font-family: Trebuchet MS;\n"
"font-size:14px;\n"
"color:white;\n"
"font-weight: bold;\n"
"border:1px solid white;\n"
"background-color:rgba(255,255,255,0.2);\n"
"border-radius:10px;\n"
"}\n"
"QPushButton:hover{\n"
"text-decoration:underline;\n"
"background-color:rgba(255,255,255,0.6);\n"
"\n"
"}\n"
"")
        icon12 = QIcon()
        icon12.addFile(u":/menu/entrega_button.png", QSize(), QIcon.Normal, QIcon.Off)
        self.table_button_2.setIcon(icon12)
        self.table_button_2.setIconSize(QSize(64, 64))
        self.frame_3 = QFrame(self.f_pedidos)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(10, 160, 1161, 421))
        self.frame_3.setStyleSheet(u"background:#6959CD;\n"
"font-family: Trebuchet MS;\n"
"font-size:14px;\n"
"font-weight:bold;\n"
"")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.f_buy = QFrame(self.frame_3)
        self.f_buy.setObjectName(u"f_buy")
        self.f_buy.setGeometry(QRect(10, 30, 441, 381))
        self.f_buy.setStyleSheet(u"background:#E0EEEE;\n"
"font-family: Trebuchet MS;\n"
"font-size:14px;\n"
"font-weight:bold;\n"
"")
        self.f_buy.setFrameShape(QFrame.StyledPanel)
        self.f_buy.setFrameShadow(QFrame.Raised)
        self.tableView = QTableView(self.f_buy)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setGeometry(QRect(15, 11, 411, 361))
        self.tableView.setStyleSheet(u"background:white;")
        self.label_2 = QLabel(self.frame_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 10, 441, 20))
        self.label_2.setAlignment(Qt.AlignCenter)
        self.groupBox = QGroupBox(self.frame_3)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(470, 40, 331, 161))
        self.groupBox.setStyleSheet(u"")
        self.textEdit = QTextEdit(self.groupBox)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(3, 20, 321, 131))
        self.textEdit.setStyleSheet(u"background:white;\n"
"border-radius:10px;\n"
"border:none")
        self.produto_confirmar = QPushButton(self.frame_3)
        self.produto_confirmar.setObjectName(u"produto_confirmar")
        self.produto_confirmar.setGeometry(QRect(490, 260, 131, 41))
        self.produto_confirmar.setCursor(QCursor(Qt.OpenHandCursor))
        self.produto_confirmar.setStyleSheet(u"QPushButton{\n"
"background: blue;\n"
"font-family: Trebuchet MS;\n"
"font-size: 16px;\n"
"color: white;\n"
"border-radius:5px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background:#1E90FF;\n"
"}\n"
"")
        self.produto_limpar = QPushButton(self.frame_3)
        self.produto_limpar.setObjectName(u"produto_limpar")
        self.produto_limpar.setGeometry(QRect(640, 260, 131, 41))
        self.produto_limpar.setCursor(QCursor(Qt.OpenHandCursor))
        self.produto_limpar.setStyleSheet(u"QPushButton{\n"
"background: blue;\n"
"font-family: Trebuchet MS;\n"
"font-size: 16px;\n"
"color: white;\n"
"border-radius:5px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background:#1E90FF;\n"
"}\n"
"")
        self.endereco_box = QGroupBox(self.frame_3)
        self.endereco_box.setObjectName(u"endereco_box")
        self.endereco_box.setGeometry(QRect(830, 60, 311, 351))
        self.endereco_box.setStyleSheet(u"border:1px solid black;\n"
"background:rgba(0,0,0,0.5);\n"
"color:white;\n"
"font_family:Trebuchet MS;")
        self.endereco_box.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.endereco_box.setFlat(False)
        self.endereco_box.setCheckable(False)
        self.label_3 = QLabel(self.endereco_box)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(30, 60, 41, 21))
        self.label_3.setStyleSheet(u"background:transparent;\n"
"border:none;")
        self.label_3.setAlignment(Qt.AlignCenter)
        self.label_4 = QLabel(self.endereco_box)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 170, 101, 16))
        self.label_4.setStyleSheet(u"background:transparent;\n"
"border:none;")
        self.label_4.setAlignment(Qt.AlignCenter)
        self.label_5 = QLabel(self.endereco_box)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 210, 101, 16))
        self.label_5.setStyleSheet(u"background:transparent;\n"
"border:none;")
        self.label_5.setAlignment(Qt.AlignCenter)
        self.label_6 = QLabel(self.endereco_box)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(10, 250, 101, 16))
        self.label_6.setStyleSheet(u"background:transparent;\n"
"border:none;")
        self.label_6.setAlignment(Qt.AlignCenter)
        self.label_7 = QLabel(self.endereco_box)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(10, 290, 101, 16))
        self.label_7.setStyleSheet(u"background:transparent;\n"
"border:none;")
        self.label_7.setAlignment(Qt.AlignCenter)
        self.label_8 = QLabel(self.endereco_box)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(110, 170, 190, 16))
        self.label_8.setStyleSheet(u"background: transparent;\n"
"border:none;\n"
"border-bottom: 1px solid white;")
        self.label_9 = QLabel(self.endereco_box)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(110, 210, 190, 16))
        self.label_9.setStyleSheet(u"background: transparent;\n"
"border:none;\n"
"border-bottom: 1px solid white;")
        self.label_10 = QLabel(self.endereco_box)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(110, 250, 190, 16))
        self.label_10.setStyleSheet(u"background: transparent;\n"
"border:none;\n"
"border-bottom: 1px solid white;")
        self.label_11 = QLabel(self.endereco_box)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(120, 290, 180, 16))
        self.label_11.setStyleSheet(u"background: transparent;\n"
"border:none;\n"
"border-bottom: 1px solid white;")
        self.input_cep = QLineEdit(self.endereco_box)
        self.input_cep.setObjectName(u"input_cep")
        self.input_cep.setGeometry(QRect(70, 60, 221, 20))
        self.input_cep.setStyleSheet(u"background:transparent;\n"
"border:none;\n"
"border-bottom: 1px solid white;\n"
"border-radius:none;\n"
"")
        self.produto_buscar = QPushButton(self.endereco_box)
        self.produto_buscar.setObjectName(u"produto_buscar")
        self.produto_buscar.setGeometry(QRect(110, 100, 101, 31))
        self.produto_buscar.setCursor(QCursor(Qt.OpenHandCursor))
        self.produto_buscar.setStyleSheet(u"QPushButton{\n"
"background: blue;\n"
"font-family: Trebuchet MS;\n"
"font-size: 12px;\n"
"color: white;\n"
"border-radius:5px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background:#1E90FF;\n"
"}\n"
"")
        self.f_caixa = QFrame(self.centralwidget)
        self.f_caixa.setObjectName(u"f_caixa")
        self.f_caixa.setGeometry(QRect(5, 90, 1190, 600))
        self.f_caixa.setFocusPolicy(Qt.NoFocus)
        self.f_caixa.setStyleSheet(u"background:rgba(0,0,0,0.5);\n"
"border-radius:10px;\n"
"")
        self.f_caixa.setFrameShape(QFrame.StyledPanel)
        self.f_caixa.setFrameShadow(QFrame.Raised)
        self.groupBox_2 = QGroupBox(self.f_caixa)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(10, 20, 1151, 281))
        self.groupBox_2.setStyleSheet(u"QGroupBox{\n"
"background:transparent;\n"
"color:white;\n"
"font-size:18px;\n"
"font-family: Trebuchet MS;\n"
"border: 1px solid white;\n"
"}")
        self.label_12 = QLabel(self.groupBox_2)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(320, 70, 81, 21))
        self.label_12.setStyleSheet(u"border:none;\n"
"background:transparent;\n"
"color:white;\n"
"font-size:18px;\n"
"font-family: Trebuchet MS;\n"
"")
        self.label_13 = QLabel(self.groupBox_2)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(320, 120, 81, 21))
        self.label_13.setStyleSheet(u"border:none;\n"
"background:transparent;\n"
"color:white;\n"
"font-size:18px;\n"
"font-family: Trebuchet MS;")
        self.abertura_valor = QLineEdit(self.groupBox_2)
        self.abertura_valor.setObjectName(u"abertura_valor")
        self.abertura_valor.setGeometry(QRect(380, 70, 221, 20))
        self.abertura_valor.setStyleSheet(u"border:none;\n"
"border-radius:0px;\n"
"border-bottom:1px solid white;\n"
"background:transparent;\n"
"color:white;\n"
"font-size:18px;\n"
"font-family: Trebuchet MS;")
        self.abertura_data = QDateEdit(self.groupBox_2)
        self.abertura_data.setObjectName(u"abertura_data")
        self.abertura_data.setGeometry(QRect(390, 120, 111, 22))
        self.abertura_data.setStyleSheet(u"border-radius:5px;\n"
"background:transparent;\n"
"color:white;\n"
"font-size:18px;\n"
"font-family: Trebuchet MS;")
        self.confirmar_abertura = QPushButton(self.groupBox_2)
        self.confirmar_abertura.setObjectName(u"confirmar_abertura")
        self.confirmar_abertura.setGeometry(QRect(400, 200, 121, 41))
        self.confirmar_abertura.setCursor(QCursor(Qt.OpenHandCursor))
        self.confirmar_abertura.setStyleSheet(u"QPushButton{\n"
"background:#1E90FF;\n"
"color:white;\n"
"font-size:18px;\n"
"font-family: Trebuchet MS;\n"
"}\n"
"QPushButton:hover{\n"
"text-decoration:underline\n"
"}")
        self.calendarWidget = QCalendarWidget(self.groupBox_2)
        self.calendarWidget.setObjectName(u"calendarWidget")
        self.calendarWidget.setGeometry(QRect(730, 40, 381, 221))
        self.calendarWidget.setStyleSheet(u"background:white;\n"
"border-radius:5px;")
        self.groupBox_3 = QGroupBox(self.f_caixa)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(10, 310, 1151, 281))
        self.groupBox_3.setStyleSheet(u"background:transparent;\n"
"color:white;\n"
"font-size:18px;\n"
"font-family: Trebuchet MS;\n"
"border: 1px solid white;")
        self.label_14 = QLabel(self.groupBox_3)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(100, 60, 331, 21))
        self.label_14.setStyleSheet(u"border:none;")
        self.fecha_data = QDateEdit(self.groupBox_3)
        self.fecha_data.setObjectName(u"fecha_data")
        self.fecha_data.setGeometry(QRect(440, 60, 110, 21))
        self.fecha_data.setStyleSheet(u"border:none;\n"
"text-decoration: underline;\n"
"color:yellow;\n"
"text-weight:bold;")
        self.fecha_buscar = QPushButton(self.groupBox_3)
        self.fecha_buscar.setObjectName(u"fecha_buscar")
        self.fecha_buscar.setGeometry(QRect(580, 60, 111, 23))
        self.fecha_buscar.setStyleSheet(u"QPushButton{\n"
"background:#1E90FF;\n"
"color:white;\n"
"font-size:18px;\n"
"font-family: Trebuchet MS;\n"
"border:none;\n"
"}\n"
"QPushButton:hover{\n"
"text-decoration:underline\n"
"}")
        self.label_15 = QLabel(self.groupBox_3)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(300, 120, 121, 31))
        self.label_15.setStyleSheet(u"border:none;")
        self.label_16 = QLabel(self.groupBox_3)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(360, 160, 61, 31))
        self.label_16.setStyleSheet(u"border:none;")
        self.fecha_confirmar = QPushButton(self.groupBox_3)
        self.fecha_confirmar.setObjectName(u"fecha_confirmar")
        self.fecha_confirmar.setGeometry(QRect(410, 220, 111, 41))
        self.fecha_confirmar.setStyleSheet(u"QPushButton{\n"
"background:#1E90FF;\n"
"color:white;\n"
"font-size:18px;\n"
"font-family: Trebuchet MS;\n"
"border:none;\n"
"}\n"
"QPushButton:hover{\n"
"text-decoration:underline\n"
"}")
        self.fecha_status = QLabel(self.groupBox_3)
        self.fecha_status.setObjectName(u"fecha_status")
        self.fecha_status.setGeometry(QRect(440, 170, 141, 16))
        self.fecha_status.setStyleSheet(u"border:none;\n"
"border-bottom:1px solid white;\n"
"")
        self.fecha_valor = QLabel(self.groupBox_3)
        self.fecha_valor.setObjectName(u"fecha_valor")
        self.fecha_valor.setGeometry(QRect(440, 130, 141, 16))
        self.fecha_valor.setStyleSheet(u"border:none;\n"
"border-bottom:1px solid white;\n"
"")
        self.f_mesas = QFrame(self.centralwidget)
        self.f_mesas.setObjectName(u"f_mesas")
        self.f_mesas.setGeometry(QRect(5, 90, 1190, 600))
        self.f_mesas.setStyleSheet(u"QFrame{\n"
"background:rgba(0,0,0,0.5);\n"
"border-radius:10px;\n"
"}\n"
"")
        self.f_mesas.setFrameShape(QFrame.StyledPanel)
        self.f_mesas.setFrameShadow(QFrame.Raised)
        self.groupBox_4 = QGroupBox(self.f_mesas)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setGeometry(QRect(10, 10, 1171, 591))
        self.groupBox_4.setStyleSheet(u"QGroupBox{\n"
"background:transparent;\n"
"color:white;\n"
"font-family: Trebuchet MS;\n"
"font-size:20px;\n"
"font-weight: bold;\n"
"}")
        self.groupBox_4.setAlignment(Qt.AlignCenter)
        self.mesa1 = QWidget(self.groupBox_4)
        self.mesa1.setObjectName(u"mesa1")
        self.mesa1.setGeometry(QRect(40, 40, 91, 81))
        self.mesa1.setStyleSheet(u"QWidget{\n"
"background:green;\n"
"border-radius:5px;\n"
"}")
        self.toolButton_4 = QToolButton(self.mesa1)
        self.toolButton_4.setObjectName(u"toolButton_4")
        self.toolButton_4.setGeometry(QRect(10, 30, 71, 51))
        self.toolButton_4.setStyleSheet(u"QToolButton{\n"
"background:transparent;\n"
"color:white;\n"
"}")
        icon13 = QIcon()
        icon13.addFile(u":/menu/table.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_4.setIcon(icon13)
        self.toolButton_4.setIconSize(QSize(64, 64))
        self.label_17 = QLabel(self.mesa1)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(0, 0, 41, 31))
        self.label_17.setStyleSheet(u"font-family: Arial;\n"
"font-size:25px;\n"
"color:white;\n"
"font-weight: bold;\n"
"background:transparent;")
        self.label_17.setAlignment(Qt.AlignCenter)
        self.mesa2 = QWidget(self.groupBox_4)
        self.mesa2.setObjectName(u"mesa2")
        self.mesa2.setGeometry(QRect(150, 40, 91, 81))
        self.mesa2.setStyleSheet(u"QWidget{\n"
"background:green;\n"
"border-radius:5px;\n"
"}")
        self.toolButton_5 = QToolButton(self.mesa2)
        self.toolButton_5.setObjectName(u"toolButton_5")
        self.toolButton_5.setGeometry(QRect(10, 30, 71, 51))
        self.toolButton_5.setStyleSheet(u"QToolButton{\n"
"background:transparent;\n"
"color:white;\n"
"}")
        self.toolButton_5.setIcon(icon13)
        self.toolButton_5.setIconSize(QSize(64, 64))
        self.label_18 = QLabel(self.mesa2)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(0, 0, 41, 31))
        self.label_18.setStyleSheet(u"font-family: Arial;\n"
"font-size:25px;\n"
"color:white;\n"
"font-weight: bold;\n"
"background:transparent;")
        self.label_18.setAlignment(Qt.AlignCenter)
        self.mesa3 = QWidget(self.groupBox_4)
        self.mesa3.setObjectName(u"mesa3")
        self.mesa3.setGeometry(QRect(260, 40, 91, 81))
        self.mesa3.setStyleSheet(u"QWidget{\n"
"background:green;\n"
"border-radius:5px;\n"
"}")
        self.toolButton_6 = QToolButton(self.mesa3)
        self.toolButton_6.setObjectName(u"toolButton_6")
        self.toolButton_6.setGeometry(QRect(10, 30, 71, 51))
        self.toolButton_6.setStyleSheet(u"QToolButton{\n"
"background:transparent;\n"
"color:white;\n"
"}")
        self.toolButton_6.setIcon(icon13)
        self.toolButton_6.setIconSize(QSize(64, 64))
        self.label_19 = QLabel(self.mesa3)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(0, 0, 41, 31))
        self.label_19.setStyleSheet(u"font-family: Arial;\n"
"font-size:25px;\n"
"color:white;\n"
"font-weight: bold;\n"
"background:transparent;")
        self.label_19.setAlignment(Qt.AlignCenter)
        self.mesa4 = QWidget(self.groupBox_4)
        self.mesa4.setObjectName(u"mesa4")
        self.mesa4.setGeometry(QRect(370, 40, 91, 81))
        self.mesa4.setStyleSheet(u"QWidget{\n"
"background:green;\n"
"border-radius:5px;\n"
"}")
        self.toolButton_7 = QToolButton(self.mesa4)
        self.toolButton_7.setObjectName(u"toolButton_7")
        self.toolButton_7.setGeometry(QRect(10, 30, 71, 51))
        self.toolButton_7.setStyleSheet(u"QToolButton{\n"
"background:transparent;\n"
"color:white;\n"
"}")
        self.toolButton_7.setIcon(icon13)
        self.toolButton_7.setIconSize(QSize(64, 64))
        self.label_20 = QLabel(self.mesa4)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(0, 0, 41, 31))
        self.label_20.setStyleSheet(u"font-family: Arial;\n"
"font-size:25px;\n"
"color:white;\n"
"font-weight: bold;\n"
"background:transparent;")
        self.label_20.setAlignment(Qt.AlignCenter)
        self.mesa5 = QWidget(self.groupBox_4)
        self.mesa5.setObjectName(u"mesa5")
        self.mesa5.setGeometry(QRect(480, 40, 91, 81))
        self.mesa5.setStyleSheet(u"QWidget{\n"
"background:green;\n"
"border-radius:5px;\n"
"}")
        self.toolButton_8 = QToolButton(self.mesa5)
        self.toolButton_8.setObjectName(u"toolButton_8")
        self.toolButton_8.setGeometry(QRect(10, 30, 71, 51))
        self.toolButton_8.setStyleSheet(u"QToolButton{\n"
"background:transparent;\n"
"color:white;\n"
"}")
        self.toolButton_8.setIcon(icon13)
        self.toolButton_8.setIconSize(QSize(64, 64))
        self.label_21 = QLabel(self.mesa5)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(0, 0, 41, 31))
        self.label_21.setStyleSheet(u"font-family: Arial;\n"
"font-size:25px;\n"
"color:white;\n"
"font-weight: bold;\n"
"background:transparent;")
        self.label_21.setAlignment(Qt.AlignCenter)
        self.mesa6 = QWidget(self.groupBox_4)
        self.mesa6.setObjectName(u"mesa6")
        self.mesa6.setGeometry(QRect(590, 40, 91, 81))
        self.mesa6.setStyleSheet(u"QWidget{\n"
"background:green;\n"
"border-radius:5px;\n"
"}")
        self.toolButton_9 = QToolButton(self.mesa6)
        self.toolButton_9.setObjectName(u"toolButton_9")
        self.toolButton_9.setGeometry(QRect(10, 30, 71, 51))
        self.toolButton_9.setStyleSheet(u"QToolButton{\n"
"background:transparent;\n"
"color:white;\n"
"}")
        self.toolButton_9.setIcon(icon13)
        self.toolButton_9.setIconSize(QSize(64, 64))
        self.label_22 = QLabel(self.mesa6)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(0, 0, 41, 31))
        self.label_22.setStyleSheet(u"font-family: Arial;\n"
"font-size:25px;\n"
"color:white;\n"
"font-weight: bold;\n"
"background:transparent;")
        self.label_22.setAlignment(Qt.AlignCenter)
        self.mesa7 = QWidget(self.groupBox_4)
        self.mesa7.setObjectName(u"mesa7")
        self.mesa7.setGeometry(QRect(700, 40, 91, 81))
        self.mesa7.setStyleSheet(u"QWidget{\n"
"background:green;\n"
"border-radius:5px;\n"
"}")
        self.toolButton_10 = QToolButton(self.mesa7)
        self.toolButton_10.setObjectName(u"toolButton_10")
        self.toolButton_10.setGeometry(QRect(10, 30, 71, 51))
        self.toolButton_10.setStyleSheet(u"QToolButton{\n"
"background:transparent;\n"
"color:white;\n"
"}")
        self.toolButton_10.setIcon(icon13)
        self.toolButton_10.setIconSize(QSize(64, 64))
        self.label_23 = QLabel(self.mesa7)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(0, 0, 41, 31))
        self.label_23.setStyleSheet(u"font-family: Arial;\n"
"font-size:25px;\n"
"color:white;\n"
"font-weight: bold;\n"
"background:transparent;")
        self.label_23.setAlignment(Qt.AlignCenter)
        self.mesa8 = QWidget(self.groupBox_4)
        self.mesa8.setObjectName(u"mesa8")
        self.mesa8.setGeometry(QRect(810, 40, 91, 81))
        self.mesa8.setStyleSheet(u"QWidget{\n"
"background:green;\n"
"border-radius:5px;\n"
"}")
        self.toolButton_11 = QToolButton(self.mesa8)
        self.toolButton_11.setObjectName(u"toolButton_11")
        self.toolButton_11.setGeometry(QRect(10, 30, 71, 51))
        self.toolButton_11.setStyleSheet(u"QToolButton{\n"
"background:transparent;\n"
"color:white;\n"
"}")
        self.toolButton_11.setIcon(icon13)
        self.toolButton_11.setIconSize(QSize(64, 64))
        self.label_24 = QLabel(self.mesa8)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setGeometry(QRect(0, 0, 41, 31))
        self.label_24.setStyleSheet(u"font-family: Arial;\n"
"font-size:25px;\n"
"color:white;\n"
"font-weight: bold;\n"
"background:transparent;")
        self.label_24.setAlignment(Qt.AlignCenter)
        self.mesa9 = QWidget(self.groupBox_4)
        self.mesa9.setObjectName(u"mesa9")
        self.mesa9.setGeometry(QRect(920, 40, 91, 81))
        self.mesa9.setStyleSheet(u"QWidget{\n"
"background:green;\n"
"border-radius:5px;\n"
"}")
        self.toolButton_12 = QToolButton(self.mesa9)
        self.toolButton_12.setObjectName(u"toolButton_12")
        self.toolButton_12.setGeometry(QRect(10, 30, 71, 51))
        self.toolButton_12.setStyleSheet(u"QToolButton{\n"
"background:transparent;\n"
"color:white;\n"
"}")
        self.toolButton_12.setIcon(icon13)
        self.toolButton_12.setIconSize(QSize(64, 64))
        self.label_25 = QLabel(self.mesa9)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setGeometry(QRect(0, 0, 41, 31))
        self.label_25.setStyleSheet(u"font-family: Arial;\n"
"font-size:25px;\n"
"color:white;\n"
"font-weight: bold;\n"
"background:transparent;")
        self.label_25.setAlignment(Qt.AlignCenter)
        self.mesa10 = QWidget(self.groupBox_4)
        self.mesa10.setObjectName(u"mesa10")
        self.mesa10.setGeometry(QRect(1030, 40, 91, 81))
        self.mesa10.setStyleSheet(u"QWidget{\n"
"background:green;\n"
"border-radius:5px;\n"
"}")
        self.toolButton_13 = QToolButton(self.mesa10)
        self.toolButton_13.setObjectName(u"toolButton_13")
        self.toolButton_13.setGeometry(QRect(10, 30, 71, 51))
        self.toolButton_13.setStyleSheet(u"QToolButton{\n"
"background:transparent;\n"
"color:white;\n"
"}")
        self.toolButton_13.setIcon(icon13)
        self.toolButton_13.setIconSize(QSize(64, 64))
        self.label_26 = QLabel(self.mesa10)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setGeometry(QRect(0, 0, 41, 31))
        self.label_26.setStyleSheet(u"font-family: Arial;\n"
"font-size:25px;\n"
"color:white;\n"
"font-weight: bold;\n"
"background:transparent;")
        self.label_26.setAlignment(Qt.AlignCenter)
        self.mesa11 = QWidget(self.groupBox_4)
        self.mesa11.setObjectName(u"mesa11")
        self.mesa11.setGeometry(QRect(40, 150, 91, 81))
        self.mesa11.setStyleSheet(u"QWidget{\n"
"background:green;\n"
"border-radius:5px;\n"
"}")
        self.toolButton_14 = QToolButton(self.mesa11)
        self.toolButton_14.setObjectName(u"toolButton_14")
        self.toolButton_14.setGeometry(QRect(10, 30, 71, 51))
        self.toolButton_14.setStyleSheet(u"QToolButton{\n"
"background:transparent;\n"
"color:white;\n"
"}")
        self.toolButton_14.setIcon(icon13)
        self.toolButton_14.setIconSize(QSize(64, 64))
        self.label_27 = QLabel(self.mesa11)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setGeometry(QRect(0, 0, 41, 31))
        self.label_27.setStyleSheet(u"font-family: Arial;\n"
"font-size:25px;\n"
"color:white;\n"
"font-weight: bold;\n"
"background:transparent;")
        self.label_27.setAlignment(Qt.AlignCenter)
        self.mesa21 = QWidget(self.groupBox_4)
        self.mesa21.setObjectName(u"mesa21")
        self.mesa21.setGeometry(QRect(40, 260, 91, 81))
        self.mesa21.setStyleSheet(u"QWidget{\n"
"background:green;\n"
"border-radius:5px;\n"
"}")
        self.toolButton_15 = QToolButton(self.mesa21)
        self.toolButton_15.setObjectName(u"toolButton_15")
        self.toolButton_15.setGeometry(QRect(10, 30, 71, 51))
        self.toolButton_15.setStyleSheet(u"QToolButton{\n"
"background:transparent;\n"
"color:white;\n"
"}")
        self.toolButton_15.setIcon(icon13)
        self.toolButton_15.setIconSize(QSize(64, 64))
        self.label_28 = QLabel(self.mesa21)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setGeometry(QRect(0, 0, 41, 31))
        self.label_28.setStyleSheet(u"font-family: Arial;\n"
"font-size:25px;\n"
"color:white;\n"
"font-weight: bold;\n"
"background:transparent;")
        self.label_28.setAlignment(Qt.AlignCenter)
        self.mesa31 = QWidget(self.groupBox_4)
        self.mesa31.setObjectName(u"mesa31")
        self.mesa31.setGeometry(QRect(40, 370, 91, 81))
        self.mesa31.setStyleSheet(u"QWidget{\n"
"background:green;\n"
"border-radius:5px;\n"
"}")
        self.toolButton_16 = QToolButton(self.mesa31)
        self.toolButton_16.setObjectName(u"toolButton_16")
        self.toolButton_16.setGeometry(QRect(10, 30, 71, 51))
        self.toolButton_16.setStyleSheet(u"QToolButton{\n"
"background:transparent;\n"
"color:white;\n"
"}")
        self.toolButton_16.setIcon(icon13)
        self.toolButton_16.setIconSize(QSize(64, 64))
        self.label_29 = QLabel(self.mesa31)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setGeometry(QRect(0, 0, 41, 31))
        self.label_29.setStyleSheet(u"font-family: Arial;\n"
"font-size:25px;\n"
"color:white;\n"
"font-weight: bold;\n"
"background:transparent;")
        self.label_29.setAlignment(Qt.AlignCenter)
        self.mesa41 = QWidget(self.groupBox_4)
        self.mesa41.setObjectName(u"mesa41")
        self.mesa41.setGeometry(QRect(40, 480, 91, 81))
        self.mesa41.setStyleSheet(u"QWidget{\n"
"background:green;\n"
"border-radius:5px;\n"
"}")
        self.toolButton_17 = QToolButton(self.mesa41)
        self.toolButton_17.setObjectName(u"toolButton_17")
        self.toolButton_17.setGeometry(QRect(10, 30, 71, 51))
        self.toolButton_17.setStyleSheet(u"QToolButton{\n"
"background:transparent;\n"
"color:white;\n"
"}")
        self.toolButton_17.setIcon(icon13)
        self.toolButton_17.setIconSize(QSize(64, 64))
        self.label_30 = QLabel(self.mesa41)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setGeometry(QRect(0, 0, 41, 31))
        self.label_30.setStyleSheet(u"font-family: Arial;\n"
"font-size:25px;\n"
"color:white;\n"
"font-weight: bold;\n"
"background:transparent;")
        self.label_30.setAlignment(Qt.AlignCenter)
        self.mesa17 = QWidget(self.groupBox_4)
        self.mesa17.setObjectName(u"mesa17")
        self.mesa17.setGeometry(QRect(700, 150, 91, 81))
        self.mesa17.setStyleSheet(u"QWidget{\n"
"background:green;\n"
"border-radius:5px;\n"
"}")
        self.toolButton_18 = QToolButton(self.mesa17)
        self.toolButton_18.setObjectName(u"toolButton_18")
        self.toolButton_18.setGeometry(QRect(10, 30, 71, 51))
        self.toolButton_18.setStyleSheet(u"QToolButton{\n"
"background:transparent;\n"
"color:white;\n"
"}")
        self.toolButton_18.setIcon(icon13)
        self.toolButton_18.setIconSize(QSize(64, 64))
        self.label_31 = QLabel(self.mesa17)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setGeometry(QRect(0, 0, 41, 31))
        self.label_31.setStyleSheet(u"font-family: Arial;\n"
"font-size:25px;\n"
"color:white;\n"
"font-weight: bold;\n"
"background:transparent;")
        self.label_31.setAlignment(Qt.AlignCenter)
        self.mesa15 = QWidget(self.groupBox_4)
        self.mesa15.setObjectName(u"mesa15")
        self.mesa15.setGeometry(QRect(480, 150, 91, 81))
        self.mesa15.setStyleSheet(u"QWidget{\n"
"background:green;\n"
"border-radius:5px;\n"
"}")
        self.toolButton_19 = QToolButton(self.mesa15)
        self.toolButton_19.setObjectName(u"toolButton_19")
        self.toolButton_19.setGeometry(QRect(10, 30, 71, 51))
        self.toolButton_19.setStyleSheet(u"QToolButton{\n"
"background:transparent;\n"
"color:white;\n"
"}")
        self.toolButton_19.setIcon(icon13)
        self.toolButton_19.setIconSize(QSize(64, 64))
        self.label_32 = QLabel(self.mesa15)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setGeometry(QRect(0, 0, 41, 31))
        self.label_32.setStyleSheet(u"font-family: Arial;\n"
"font-size:25px;\n"
"color:white;\n"
"font-weight: bold;\n"
"background:transparent;")
        self.label_32.setAlignment(Qt.AlignCenter)
        self.mesa19 = QWidget(self.groupBox_4)
        self.mesa19.setObjectName(u"mesa19")
        self.mesa19.setGeometry(QRect(920, 150, 91, 81))
        self.mesa19.setStyleSheet(u"QWidget{\n"
"background:green;\n"
"border-radius:5px;\n"
"}")
        self.toolButton_20 = QToolButton(self.mesa19)
        self.toolButton_20.setObjectName(u"toolButton_20")
        self.toolButton_20.setGeometry(QRect(10, 30, 71, 51))
        self.toolButton_20.setStyleSheet(u"QToolButton{\n"
"background:transparent;\n"
"color:white;\n"
"}")
        self.toolButton_20.setIcon(icon13)
        self.toolButton_20.setIconSize(QSize(64, 64))
        self.label_33 = QLabel(self.mesa19)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setGeometry(QRect(0, 0, 41, 31))
        self.label_33.setStyleSheet(u"font-family: Arial;\n"
"font-size:25px;\n"
"color:white;\n"
"font-weight: bold;\n"
"background:transparent;")
        self.label_33.setAlignment(Qt.AlignCenter)
        self.mesa14 = QWidget(self.groupBox_4)
        self.mesa14.setObjectName(u"mesa14")
        self.mesa14.setGeometry(QRect(370, 150, 91, 81))
        self.mesa14.setStyleSheet(u"QWidget{\n"
"background:green;\n"
"border-radius:5px;\n"
"}")
        self.toolButton_21 = QToolButton(self.mesa14)
        self.toolButton_21.setObjectName(u"toolButton_21")
        self.toolButton_21.setGeometry(QRect(10, 30, 71, 51))
        self.toolButton_21.setStyleSheet(u"QToolButton{\n"
"background:transparent;\n"
"color:white;\n"
"}")
        self.toolButton_21.setIcon(icon13)
        self.toolButton_21.setIconSize(QSize(64, 64))
        self.label_34 = QLabel(self.mesa14)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setGeometry(QRect(0, 0, 41, 31))
        self.label_34.setStyleSheet(u"font-family: Arial;\n"
"font-size:25px;\n"
"color:white;\n"
"font-weight: bold;\n"
"background:transparent;")
        self.label_34.setAlignment(Qt.AlignCenter)
        self.mesa16 = QWidget(self.groupBox_4)
        self.mesa16.setObjectName(u"mesa16")
        self.mesa16.setGeometry(QRect(590, 150, 91, 81))
        self.mesa16.setStyleSheet(u"QWidget{\n"
"background:green;\n"
"border-radius:5px;\n"
"}")
        self.toolButton_22 = QToolButton(self.mesa16)
        self.toolButton_22.setObjectName(u"toolButton_22")
        self.toolButton_22.setGeometry(QRect(10, 30, 71, 51))
        self.toolButton_22.setStyleSheet(u"QToolButton{\n"
"background:transparent;\n"
"color:white;\n"
"}")
        self.toolButton_22.setIcon(icon13)
        self.toolButton_22.setIconSize(QSize(64, 64))
        self.label_35 = QLabel(self.mesa16)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setGeometry(QRect(0, 0, 41, 31))
        self.label_35.setStyleSheet(u"font-family: Arial;\n"
"font-size:25px;\n"
"color:white;\n"
"font-weight: bold;\n"
"background:transparent;")
        self.label_35.setAlignment(Qt.AlignCenter)
        self.mesa18 = QWidget(self.groupBox_4)
        self.mesa18.setObjectName(u"mesa18")
        self.mesa18.setGeometry(QRect(810, 150, 91, 81))
        self.mesa18.setStyleSheet(u"QWidget{\n"
"background:green;\n"
"border-radius:5px;\n"
"}")
        self.toolButton_23 = QToolButton(self.mesa18)
        self.toolButton_23.setObjectName(u"toolButton_23")
        self.toolButton_23.setGeometry(QRect(10, 30, 71, 51))
        self.toolButton_23.setStyleSheet(u"QToolButton{\n"
"background:transparent;\n"
"color:white;\n"
"}")
        self.toolButton_23.setIcon(icon13)
        self.toolButton_23.setIconSize(QSize(64, 64))
        self.label_36 = QLabel(self.mesa18)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setGeometry(QRect(0, 0, 41, 31))
        self.label_36.setStyleSheet(u"font-family: Arial;\n"
"font-size:25px;\n"
"color:white;\n"
"font-weight: bold;\n"
"background:transparent;")
        self.label_36.setAlignment(Qt.AlignCenter)
        self.mesa13 = QWidget(self.groupBox_4)
        self.mesa13.setObjectName(u"mesa13")
        self.mesa13.setGeometry(QRect(260, 150, 91, 81))
        self.mesa13.setStyleSheet(u"QWidget{\n"
"background:green;\n"
"border-radius:5px;\n"
"}")
        self.toolButton_24 = QToolButton(self.mesa13)
        self.toolButton_24.setObjectName(u"toolButton_24")
        self.toolButton_24.setGeometry(QRect(10, 30, 71, 51))
        self.toolButton_24.setStyleSheet(u"QToolButton{\n"
"background:transparent;\n"
"color:white;\n"
"}")
        self.toolButton_24.setIcon(icon13)
        self.toolButton_24.setIconSize(QSize(64, 64))
        self.label_37 = QLabel(self.mesa13)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setGeometry(QRect(0, 0, 41, 31))
        self.label_37.setStyleSheet(u"font-family: Arial;\n"
"font-size:25px;\n"
"color:white;\n"
"font-weight: bold;\n"
"background:transparent;")
        self.label_37.setAlignment(Qt.AlignCenter)
        self.mesa20 = QWidget(self.groupBox_4)
        self.mesa20.setObjectName(u"mesa20")
        self.mesa20.setGeometry(QRect(1030, 150, 91, 81))
        self.mesa20.setStyleSheet(u"QWidget{\n"
"background:green;\n"
"border-radius:5px;\n"
"}")
        self.toolButton_25 = QToolButton(self.mesa20)
        self.toolButton_25.setObjectName(u"toolButton_25")
        self.toolButton_25.setGeometry(QRect(10, 30, 71, 51))
        self.toolButton_25.setStyleSheet(u"QToolButton{\n"
"background:transparent;\n"
"color:white;\n"
"}")
        self.toolButton_25.setIcon(icon13)
        self.toolButton_25.setIconSize(QSize(64, 64))
        self.label_38 = QLabel(self.mesa20)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setGeometry(QRect(0, 0, 41, 31))
        self.label_38.setStyleSheet(u"font-family: Arial;\n"
"font-size:25px;\n"
"color:white;\n"
"font-weight: bold;\n"
"background:transparent;")
        self.label_38.setAlignment(Qt.AlignCenter)
        self.mesa12 = QWidget(self.groupBox_4)
        self.mesa12.setObjectName(u"mesa12")
        self.mesa12.setGeometry(QRect(150, 150, 91, 81))
        self.mesa12.setStyleSheet(u"QWidget{\n"
"background:green;\n"
"border-radius:5px;\n"
"}")
        self.toolButton_26 = QToolButton(self.mesa12)
        self.toolButton_26.setObjectName(u"toolButton_26")
        self.toolButton_26.setGeometry(QRect(10, 30, 71, 51))
        self.toolButton_26.setStyleSheet(u"QToolButton{\n"
"background:transparent;\n"
"color:white;\n"
"}")
        self.toolButton_26.setIcon(icon13)
        self.toolButton_26.setIconSize(QSize(64, 64))
        self.label_39 = QLabel(self.mesa12)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setGeometry(QRect(0, 0, 41, 31))
        self.label_39.setStyleSheet(u"font-family: Arial;\n"
"font-size:25px;\n"
"color:white;\n"
"font-weight: bold;\n"
"background:transparent;")
        self.label_39.setAlignment(Qt.AlignCenter)
        self.mesa27 = QWidget(self.groupBox_4)
        self.mesa27.setObjectName(u"mesa27")
        self.mesa27.setGeometry(QRect(700, 260, 91, 81))
        self.mesa27.setStyleSheet(u"QWidget{\n"
"background:green;\n"
"border-radius:5px;\n"
"}")
        self.toolButton_27 = QToolButton(self.mesa27)
        self.toolButton_27.setObjectName(u"toolButton_27")
        self.toolButton_27.setGeometry(QRect(10, 30, 71, 51))
        self.toolButton_27.setStyleSheet(u"QToolButton{\n"
"background:transparent;\n"
"color:white;\n"
"}")
        self.toolButton_27.setIcon(icon13)
        self.toolButton_27.setIconSize(QSize(64, 64))
        self.label_40 = QLabel(self.mesa27)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setGeometry(QRect(0, 0, 41, 31))
        self.label_40.setStyleSheet(u"font-family: Arial;\n"
"font-size:25px;\n"
"color:white;\n"
"font-weight: bold;\n"
"background:transparent;")
        self.label_40.setAlignment(Qt.AlignCenter)
        self.mesa25 = QWidget(self.groupBox_4)
        self.mesa25.setObjectName(u"mesa25")
        self.mesa25.setGeometry(QRect(480, 260, 91, 81))
        self.mesa25.setStyleSheet(u"QWidget{\n"
"background:green;\n"
"border-radius:5px;\n"
"}")
        self.toolButton_28 = QToolButton(self.mesa25)
        self.toolButton_28.setObjectName(u"toolButton_28")
        self.toolButton_28.setGeometry(QRect(10, 30, 71, 51))
        self.toolButton_28.setStyleSheet(u"QToolButton{\n"
"background:transparent;\n"
"color:white;\n"
"}")
        self.toolButton_28.setIcon(icon13)
        self.toolButton_28.setIconSize(QSize(64, 64))
        self.label_41 = QLabel(self.mesa25)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setGeometry(QRect(0, 0, 41, 31))
        self.label_41.setStyleSheet(u"font-family: Arial;\n"
"font-size:25px;\n"
"color:white;\n"
"font-weight: bold;\n"
"background:transparent;")
        self.label_41.setAlignment(Qt.AlignCenter)
        self.mesa29 = QWidget(self.groupBox_4)
        self.mesa29.setObjectName(u"mesa29")
        self.mesa29.setGeometry(QRect(920, 260, 91, 81))
        self.mesa29.setStyleSheet(u"QWidget{\n"
"background:green;\n"
"border-radius:5px;\n"
"}")
        self.toolButton_29 = QToolButton(self.mesa29)
        self.toolButton_29.setObjectName(u"toolButton_29")
        self.toolButton_29.setGeometry(QRect(10, 30, 71, 51))
        self.toolButton_29.setStyleSheet(u"QToolButton{\n"
"background:transparent;\n"
"color:white;\n"
"}")
        self.toolButton_29.setIcon(icon13)
        self.toolButton_29.setIconSize(QSize(64, 64))
        self.label_42 = QLabel(self.mesa29)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setGeometry(QRect(0, 0, 41, 31))
        self.label_42.setStyleSheet(u"font-family: Arial;\n"
"font-size:25px;\n"
"color:white;\n"
"font-weight: bold;\n"
"background:transparent;")
        self.label_42.setAlignment(Qt.AlignCenter)
        self.mesa24 = QWidget(self.groupBox_4)
        self.mesa24.setObjectName(u"mesa24")
        self.mesa24.setGeometry(QRect(370, 260, 91, 81))
        self.mesa24.setStyleSheet(u"QWidget{\n"
"background:green;\n"
"border-radius:5px;\n"
"}")
        self.toolButton_30 = QToolButton(self.mesa24)
        self.toolButton_30.setObjectName(u"toolButton_30")
        self.toolButton_30.setGeometry(QRect(10, 30, 71, 51))
        self.toolButton_30.setStyleSheet(u"QToolButton{\n"
"background:transparent;\n"
"color:white;\n"
"}")
        self.toolButton_30.setIcon(icon13)
        self.toolButton_30.setIconSize(QSize(64, 64))
        self.label_43 = QLabel(self.mesa24)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setGeometry(QRect(0, 0, 41, 31))
        self.label_43.setStyleSheet(u"font-family: Arial;\n"
"font-size:25px;\n"
"color:white;\n"
"font-weight: bold;\n"
"background:transparent;")
        self.label_43.setAlignment(Qt.AlignCenter)
        self.mesa26 = QWidget(self.groupBox_4)
        self.mesa26.setObjectName(u"mesa26")
        self.mesa26.setGeometry(QRect(590, 260, 91, 81))
        self.mesa26.setStyleSheet(u"QWidget{\n"
"background:green;\n"
"border-radius:5px;\n"
"}")
        self.toolButton_31 = QToolButton(self.mesa26)
        self.toolButton_31.setObjectName(u"toolButton_31")
        self.toolButton_31.setGeometry(QRect(10, 30, 71, 51))
        self.toolButton_31.setStyleSheet(u"QToolButton{\n"
"background:transparent;\n"
"color:white;\n"
"}")
        self.toolButton_31.setIcon(icon13)
        self.toolButton_31.setIconSize(QSize(64, 64))
        self.label_44 = QLabel(self.mesa26)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setGeometry(QRect(0, 0, 41, 31))
        self.label_44.setStyleSheet(u"font-family: Arial;\n"
"font-size:25px;\n"
"color:white;\n"
"font-weight: bold;\n"
"background:transparent;")
        self.label_44.setAlignment(Qt.AlignCenter)
        self.mesa28 = QWidget(self.groupBox_4)
        self.mesa28.setObjectName(u"mesa28")
        self.mesa28.setGeometry(QRect(810, 260, 91, 81))
        self.mesa28.setStyleSheet(u"QWidget{\n"
"background:green;\n"
"border-radius:5px;\n"
"}")
        self.toolButton_32 = QToolButton(self.mesa28)
        self.toolButton_32.setObjectName(u"toolButton_32")
        self.toolButton_32.setGeometry(QRect(10, 30, 71, 51))
        self.toolButton_32.setStyleSheet(u"QToolButton{\n"
"background:transparent;\n"
"color:white;\n"
"}")
        self.toolButton_32.setIcon(icon13)
        self.toolButton_32.setIconSize(QSize(64, 64))
        self.label_45 = QLabel(self.mesa28)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setGeometry(QRect(0, 0, 41, 31))
        self.label_45.setStyleSheet(u"font-family: Arial;\n"
"font-size:25px;\n"
"color:white;\n"
"font-weight: bold;\n"
"background:transparent;")
        self.label_45.setAlignment(Qt.AlignCenter)
        self.mesa23 = QWidget(self.groupBox_4)
        self.mesa23.setObjectName(u"mesa23")
        self.mesa23.setGeometry(QRect(260, 260, 91, 81))
        self.mesa23.setStyleSheet(u"QWidget{\n"
"background:green;\n"
"border-radius:5px;\n"
"}")
        self.toolButton_33 = QToolButton(self.mesa23)
        self.toolButton_33.setObjectName(u"toolButton_33")
        self.toolButton_33.setGeometry(QRect(10, 30, 71, 51))
        self.toolButton_33.setStyleSheet(u"QToolButton{\n"
"background:transparent;\n"
"color:white;\n"
"}")
        self.toolButton_33.setIcon(icon13)
        self.toolButton_33.setIconSize(QSize(64, 64))
        self.label_46 = QLabel(self.mesa23)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setGeometry(QRect(0, 0, 41, 31))
        self.label_46.setStyleSheet(u"font-family: Arial;\n"
"font-size:25px;\n"
"color:white;\n"
"font-weight: bold;\n"
"background:transparent;")
        self.label_46.setAlignment(Qt.AlignCenter)
        self.mesa30 = QWidget(self.groupBox_4)
        self.mesa30.setObjectName(u"mesa30")
        self.mesa30.setGeometry(QRect(1030, 260, 91, 81))
        self.mesa30.setStyleSheet(u"QWidget{\n"
"background:green;\n"
"border-radius:5px;\n"
"}")
        self.toolButton_34 = QToolButton(self.mesa30)
        self.toolButton_34.setObjectName(u"toolButton_34")
        self.toolButton_34.setGeometry(QRect(10, 30, 71, 51))
        self.toolButton_34.setStyleSheet(u"QToolButton{\n"
"background:transparent;\n"
"color:white;\n"
"}")
        self.toolButton_34.setIcon(icon13)
        self.toolButton_34.setIconSize(QSize(64, 64))
        self.label_47 = QLabel(self.mesa30)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setGeometry(QRect(0, 0, 41, 31))
        self.label_47.setStyleSheet(u"font-family: Arial;\n"
"font-size:25px;\n"
"color:white;\n"
"font-weight: bold;\n"
"background:transparent;")
        self.label_47.setAlignment(Qt.AlignCenter)
        self.mesa22 = QWidget(self.groupBox_4)
        self.mesa22.setObjectName(u"mesa22")
        self.mesa22.setGeometry(QRect(150, 260, 91, 81))
        self.mesa22.setStyleSheet(u"QWidget{\n"
"background:green;\n"
"border-radius:5px;\n"
"}")
        self.toolButton_35 = QToolButton(self.mesa22)
        self.toolButton_35.setObjectName(u"toolButton_35")
        self.toolButton_35.setGeometry(QRect(10, 30, 71, 51))
        self.toolButton_35.setStyleSheet(u"QToolButton{\n"
"background:transparent;\n"
"color:white;\n"
"}")
        self.toolButton_35.setIcon(icon13)
        self.toolButton_35.setIconSize(QSize(64, 64))
        self.label_48 = QLabel(self.mesa22)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setGeometry(QRect(0, 0, 41, 31))
        self.label_48.setStyleSheet(u"font-family: Arial;\n"
"font-size:25px;\n"
"color:white;\n"
"font-weight: bold;\n"
"background:transparent;")
        self.label_48.setAlignment(Qt.AlignCenter)
        self.mesa37 = QWidget(self.groupBox_4)
        self.mesa37.setObjectName(u"mesa37")
        self.mesa37.setGeometry(QRect(700, 370, 91, 81))
        self.mesa37.setStyleSheet(u"QWidget{\n"
"background:green;\n"
"border-radius:5px;\n"
"}")
        self.toolButton_36 = QToolButton(self.mesa37)
        self.toolButton_36.setObjectName(u"toolButton_36")
        self.toolButton_36.setGeometry(QRect(10, 30, 71, 51))
        self.toolButton_36.setStyleSheet(u"QToolButton{\n"
"background:transparent;\n"
"color:white;\n"
"}")
        self.toolButton_36.setIcon(icon13)
        self.toolButton_36.setIconSize(QSize(64, 64))
        self.label_49 = QLabel(self.mesa37)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setGeometry(QRect(0, 0, 41, 31))
        self.label_49.setStyleSheet(u"font-family: Arial;\n"
"font-size:25px;\n"
"color:white;\n"
"font-weight: bold;\n"
"background:transparent;")
        self.label_49.setAlignment(Qt.AlignCenter)
        self.mesa35 = QWidget(self.groupBox_4)
        self.mesa35.setObjectName(u"mesa35")
        self.mesa35.setGeometry(QRect(480, 370, 91, 81))
        self.mesa35.setStyleSheet(u"QWidget{\n"
"background:green;\n"
"border-radius:5px;\n"
"}")
        self.toolButton_37 = QToolButton(self.mesa35)
        self.toolButton_37.setObjectName(u"toolButton_37")
        self.toolButton_37.setGeometry(QRect(10, 30, 71, 51))
        self.toolButton_37.setStyleSheet(u"QToolButton{\n"
"background:transparent;\n"
"color:white;\n"
"}")
        self.toolButton_37.setIcon(icon13)
        self.toolButton_37.setIconSize(QSize(64, 64))
        self.label_50 = QLabel(self.mesa35)
        self.label_50.setObjectName(u"label_50")
        self.label_50.setGeometry(QRect(0, 0, 41, 31))
        self.label_50.setStyleSheet(u"font-family: Arial;\n"
"font-size:25px;\n"
"color:white;\n"
"font-weight: bold;\n"
"background:transparent;")
        self.label_50.setAlignment(Qt.AlignCenter)
        self.mesa39 = QWidget(self.groupBox_4)
        self.mesa39.setObjectName(u"mesa39")
        self.mesa39.setGeometry(QRect(920, 370, 91, 81))
        self.mesa39.setStyleSheet(u"QWidget{\n"
"background:green;\n"
"border-radius:5px;\n"
"}")
        self.toolButton_38 = QToolButton(self.mesa39)
        self.toolButton_38.setObjectName(u"toolButton_38")
        self.toolButton_38.setGeometry(QRect(10, 30, 71, 51))
        self.toolButton_38.setStyleSheet(u"QToolButton{\n"
"background:transparent;\n"
"color:white;\n"
"}")
        self.toolButton_38.setIcon(icon13)
        self.toolButton_38.setIconSize(QSize(64, 64))
        self.label_51 = QLabel(self.mesa39)
        self.label_51.setObjectName(u"label_51")
        self.label_51.setGeometry(QRect(0, 0, 41, 31))
        self.label_51.setStyleSheet(u"font-family: Arial;\n"
"font-size:25px;\n"
"color:white;\n"
"font-weight: bold;\n"
"background:transparent;")
        self.label_51.setAlignment(Qt.AlignCenter)
        self.mesa34 = QWidget(self.groupBox_4)
        self.mesa34.setObjectName(u"mesa34")
        self.mesa34.setGeometry(QRect(370, 370, 91, 81))
        self.mesa34.setStyleSheet(u"QWidget{\n"
"background:green;\n"
"border-radius:5px;\n"
"}")
        self.toolButton_39 = QToolButton(self.mesa34)
        self.toolButton_39.setObjectName(u"toolButton_39")
        self.toolButton_39.setGeometry(QRect(10, 30, 71, 51))
        self.toolButton_39.setStyleSheet(u"QToolButton{\n"
"background:transparent;\n"
"color:white;\n"
"}")
        self.toolButton_39.setIcon(icon13)
        self.toolButton_39.setIconSize(QSize(64, 64))
        self.label_52 = QLabel(self.mesa34)
        self.label_52.setObjectName(u"label_52")
        self.label_52.setGeometry(QRect(0, 0, 41, 31))
        self.label_52.setStyleSheet(u"font-family: Arial;\n"
"font-size:25px;\n"
"color:white;\n"
"font-weight: bold;\n"
"background:transparent;")
        self.label_52.setAlignment(Qt.AlignCenter)
        self.mesa36 = QWidget(self.groupBox_4)
        self.mesa36.setObjectName(u"mesa36")
        self.mesa36.setGeometry(QRect(590, 370, 91, 81))
        self.mesa36.setStyleSheet(u"QWidget{\n"
"background:green;\n"
"border-radius:5px;\n"
"}")
        self.toolButton_40 = QToolButton(self.mesa36)
        self.toolButton_40.setObjectName(u"toolButton_40")
        self.toolButton_40.setGeometry(QRect(10, 30, 71, 51))
        self.toolButton_40.setStyleSheet(u"QToolButton{\n"
"background:transparent;\n"
"color:white;\n"
"}")
        self.toolButton_40.setIcon(icon13)
        self.toolButton_40.setIconSize(QSize(64, 64))
        self.label_53 = QLabel(self.mesa36)
        self.label_53.setObjectName(u"label_53")
        self.label_53.setGeometry(QRect(0, 0, 41, 31))
        self.label_53.setStyleSheet(u"font-family: Arial;\n"
"font-size:25px;\n"
"color:white;\n"
"font-weight: bold;\n"
"background:transparent;")
        self.label_53.setAlignment(Qt.AlignCenter)
        self.mesa38 = QWidget(self.groupBox_4)
        self.mesa38.setObjectName(u"mesa38")
        self.mesa38.setGeometry(QRect(810, 370, 91, 81))
        self.mesa38.setStyleSheet(u"QWidget{\n"
"background:green;\n"
"border-radius:5px;\n"
"}")
        self.toolButton_41 = QToolButton(self.mesa38)
        self.toolButton_41.setObjectName(u"toolButton_41")
        self.toolButton_41.setGeometry(QRect(10, 30, 71, 51))
        self.toolButton_41.setStyleSheet(u"QToolButton{\n"
"background:transparent;\n"
"color:white;\n"
"}")
        self.toolButton_41.setIcon(icon13)
        self.toolButton_41.setIconSize(QSize(64, 64))
        self.label_54 = QLabel(self.mesa38)
        self.label_54.setObjectName(u"label_54")
        self.label_54.setGeometry(QRect(0, 0, 41, 31))
        self.label_54.setStyleSheet(u"font-family: Arial;\n"
"font-size:25px;\n"
"color:white;\n"
"font-weight: bold;\n"
"background:transparent;")
        self.label_54.setAlignment(Qt.AlignCenter)
        self.mesa33 = QWidget(self.groupBox_4)
        self.mesa33.setObjectName(u"mesa33")
        self.mesa33.setGeometry(QRect(260, 370, 91, 81))
        self.mesa33.setStyleSheet(u"QWidget{\n"
"background:green;\n"
"border-radius:5px;\n"
"}")
        self.toolButton_42 = QToolButton(self.mesa33)
        self.toolButton_42.setObjectName(u"toolButton_42")
        self.toolButton_42.setGeometry(QRect(10, 30, 71, 51))
        self.toolButton_42.setStyleSheet(u"QToolButton{\n"
"background:transparent;\n"
"color:white;\n"
"}")
        self.toolButton_42.setIcon(icon13)
        self.toolButton_42.setIconSize(QSize(64, 64))
        self.label_55 = QLabel(self.mesa33)
        self.label_55.setObjectName(u"label_55")
        self.label_55.setGeometry(QRect(0, 0, 41, 31))
        self.label_55.setStyleSheet(u"font-family: Arial;\n"
"font-size:25px;\n"
"color:white;\n"
"font-weight: bold;\n"
"background:transparent;")
        self.label_55.setAlignment(Qt.AlignCenter)
        self.mesa40 = QWidget(self.groupBox_4)
        self.mesa40.setObjectName(u"mesa40")
        self.mesa40.setGeometry(QRect(1030, 370, 91, 81))
        self.mesa40.setStyleSheet(u"QWidget{\n"
"background:green;\n"
"border-radius:5px;\n"
"}")
        self.toolButton_43 = QToolButton(self.mesa40)
        self.toolButton_43.setObjectName(u"toolButton_43")
        self.toolButton_43.setGeometry(QRect(10, 30, 71, 51))
        self.toolButton_43.setStyleSheet(u"QToolButton{\n"
"background:transparent;\n"
"color:white;\n"
"}")
        self.toolButton_43.setIcon(icon13)
        self.toolButton_43.setIconSize(QSize(64, 64))
        self.label_56 = QLabel(self.mesa40)
        self.label_56.setObjectName(u"label_56")
        self.label_56.setGeometry(QRect(0, 0, 41, 31))
        self.label_56.setStyleSheet(u"font-family: Arial;\n"
"font-size:25px;\n"
"color:white;\n"
"font-weight: bold;\n"
"background:transparent;")
        self.label_56.setAlignment(Qt.AlignCenter)
        self.mesa32 = QWidget(self.groupBox_4)
        self.mesa32.setObjectName(u"mesa32")
        self.mesa32.setGeometry(QRect(150, 370, 91, 81))
        self.mesa32.setStyleSheet(u"QWidget{\n"
"background:green;\n"
"border-radius:5px;\n"
"}")
        self.toolButton_44 = QToolButton(self.mesa32)
        self.toolButton_44.setObjectName(u"toolButton_44")
        self.toolButton_44.setGeometry(QRect(10, 30, 71, 51))
        self.toolButton_44.setStyleSheet(u"QToolButton{\n"
"background:transparent;\n"
"color:white;\n"
"}")
        self.toolButton_44.setIcon(icon13)
        self.toolButton_44.setIconSize(QSize(64, 64))
        self.label_57 = QLabel(self.mesa32)
        self.label_57.setObjectName(u"label_57")
        self.label_57.setGeometry(QRect(0, 0, 41, 31))
        self.label_57.setStyleSheet(u"font-family: Arial;\n"
"font-size:25px;\n"
"color:white;\n"
"font-weight: bold;\n"
"background:transparent;")
        self.label_57.setAlignment(Qt.AlignCenter)
        self.mesa47 = QWidget(self.groupBox_4)
        self.mesa47.setObjectName(u"mesa47")
        self.mesa47.setGeometry(QRect(700, 480, 91, 81))
        self.mesa47.setStyleSheet(u"QWidget{\n"
"background:green;\n"
"border-radius:5px;\n"
"}")
        self.toolButton_45 = QToolButton(self.mesa47)
        self.toolButton_45.setObjectName(u"toolButton_45")
        self.toolButton_45.setGeometry(QRect(10, 30, 71, 51))
        self.toolButton_45.setStyleSheet(u"QToolButton{\n"
"background:transparent;\n"
"color:white;\n"
"}")
        self.toolButton_45.setIcon(icon13)
        self.toolButton_45.setIconSize(QSize(64, 64))
        self.label_58 = QLabel(self.mesa47)
        self.label_58.setObjectName(u"label_58")
        self.label_58.setGeometry(QRect(0, 0, 41, 31))
        self.label_58.setStyleSheet(u"font-family: Arial;\n"
"font-size:25px;\n"
"color:white;\n"
"font-weight: bold;\n"
"background:transparent;")
        self.label_58.setAlignment(Qt.AlignCenter)
        self.mesa45 = QWidget(self.groupBox_4)
        self.mesa45.setObjectName(u"mesa45")
        self.mesa45.setGeometry(QRect(480, 480, 91, 81))
        self.mesa45.setStyleSheet(u"QWidget{\n"
"background:green;\n"
"border-radius:5px;\n"
"}")
        self.toolButton_46 = QToolButton(self.mesa45)
        self.toolButton_46.setObjectName(u"toolButton_46")
        self.toolButton_46.setGeometry(QRect(10, 30, 71, 51))
        self.toolButton_46.setStyleSheet(u"QToolButton{\n"
"background:transparent;\n"
"color:white;\n"
"}")
        self.toolButton_46.setIcon(icon13)
        self.toolButton_46.setIconSize(QSize(64, 64))
        self.label_59 = QLabel(self.mesa45)
        self.label_59.setObjectName(u"label_59")
        self.label_59.setGeometry(QRect(0, 0, 41, 31))
        self.label_59.setStyleSheet(u"font-family: Arial;\n"
"font-size:25px;\n"
"color:white;\n"
"font-weight: bold;\n"
"background:transparent;")
        self.label_59.setAlignment(Qt.AlignCenter)
        self.mesa49 = QWidget(self.groupBox_4)
        self.mesa49.setObjectName(u"mesa49")
        self.mesa49.setGeometry(QRect(920, 480, 91, 81))
        self.mesa49.setStyleSheet(u"QWidget{\n"
"background:green;\n"
"border-radius:5px;\n"
"}")
        self.toolButton_47 = QToolButton(self.mesa49)
        self.toolButton_47.setObjectName(u"toolButton_47")
        self.toolButton_47.setGeometry(QRect(10, 30, 71, 51))
        self.toolButton_47.setStyleSheet(u"QToolButton{\n"
"background:transparent;\n"
"color:white;\n"
"}")
        self.toolButton_47.setIcon(icon13)
        self.toolButton_47.setIconSize(QSize(64, 64))
        self.label_60 = QLabel(self.mesa49)
        self.label_60.setObjectName(u"label_60")
        self.label_60.setGeometry(QRect(0, 0, 41, 31))
        self.label_60.setStyleSheet(u"font-family: Arial;\n"
"font-size:25px;\n"
"color:white;\n"
"font-weight: bold;\n"
"background:transparent;")
        self.label_60.setAlignment(Qt.AlignCenter)
        self.mesa44 = QWidget(self.groupBox_4)
        self.mesa44.setObjectName(u"mesa44")
        self.mesa44.setGeometry(QRect(370, 480, 91, 81))
        self.mesa44.setStyleSheet(u"QWidget{\n"
"background:green;\n"
"border-radius:5px;\n"
"}")
        self.toolButton_48 = QToolButton(self.mesa44)
        self.toolButton_48.setObjectName(u"toolButton_48")
        self.toolButton_48.setGeometry(QRect(10, 30, 71, 51))
        self.toolButton_48.setStyleSheet(u"QToolButton{\n"
"background:transparent;\n"
"color:white;\n"
"}")
        self.toolButton_48.setIcon(icon13)
        self.toolButton_48.setIconSize(QSize(64, 64))
        self.label_61 = QLabel(self.mesa44)
        self.label_61.setObjectName(u"label_61")
        self.label_61.setGeometry(QRect(0, 0, 41, 31))
        self.label_61.setStyleSheet(u"font-family: Arial;\n"
"font-size:25px;\n"
"color:white;\n"
"font-weight: bold;\n"
"background:transparent;")
        self.label_61.setAlignment(Qt.AlignCenter)
        self.mesa46 = QWidget(self.groupBox_4)
        self.mesa46.setObjectName(u"mesa46")
        self.mesa46.setGeometry(QRect(590, 480, 91, 81))
        self.mesa46.setStyleSheet(u"QWidget{\n"
"background:green;\n"
"border-radius:5px;\n"
"}")
        self.toolButton_49 = QToolButton(self.mesa46)
        self.toolButton_49.setObjectName(u"toolButton_49")
        self.toolButton_49.setGeometry(QRect(10, 30, 71, 51))
        self.toolButton_49.setStyleSheet(u"QToolButton{\n"
"background:transparent;\n"
"color:white;\n"
"}")
        self.toolButton_49.setIcon(icon13)
        self.toolButton_49.setIconSize(QSize(64, 64))
        self.label_62 = QLabel(self.mesa46)
        self.label_62.setObjectName(u"label_62")
        self.label_62.setGeometry(QRect(0, 0, 41, 31))
        self.label_62.setStyleSheet(u"font-family: Arial;\n"
"font-size:25px;\n"
"color:white;\n"
"font-weight: bold;\n"
"background:transparent;")
        self.label_62.setAlignment(Qt.AlignCenter)
        self.mesa48 = QWidget(self.groupBox_4)
        self.mesa48.setObjectName(u"mesa48")
        self.mesa48.setGeometry(QRect(810, 480, 91, 81))
        self.mesa48.setStyleSheet(u"QWidget{\n"
"background:green;\n"
"border-radius:5px;\n"
"}")
        self.toolButton_50 = QToolButton(self.mesa48)
        self.toolButton_50.setObjectName(u"toolButton_50")
        self.toolButton_50.setGeometry(QRect(10, 30, 71, 51))
        self.toolButton_50.setStyleSheet(u"QToolButton{\n"
"background:transparent;\n"
"color:white;\n"
"}")
        self.toolButton_50.setIcon(icon13)
        self.toolButton_50.setIconSize(QSize(64, 64))
        self.label_63 = QLabel(self.mesa48)
        self.label_63.setObjectName(u"label_63")
        self.label_63.setGeometry(QRect(0, 0, 41, 31))
        self.label_63.setStyleSheet(u"font-family: Arial;\n"
"font-size:25px;\n"
"color:white;\n"
"font-weight: bold;\n"
"background:transparent;")
        self.label_63.setAlignment(Qt.AlignCenter)
        self.mesa43 = QWidget(self.groupBox_4)
        self.mesa43.setObjectName(u"mesa43")
        self.mesa43.setGeometry(QRect(260, 480, 91, 81))
        self.mesa43.setStyleSheet(u"QWidget{\n"
"background:green;\n"
"border-radius:5px;\n"
"}")
        self.toolButton_51 = QToolButton(self.mesa43)
        self.toolButton_51.setObjectName(u"toolButton_51")
        self.toolButton_51.setGeometry(QRect(10, 30, 71, 51))
        self.toolButton_51.setStyleSheet(u"QToolButton{\n"
"background:transparent;\n"
"color:white;\n"
"}")
        self.toolButton_51.setIcon(icon13)
        self.toolButton_51.setIconSize(QSize(64, 64))
        self.label_64 = QLabel(self.mesa43)
        self.label_64.setObjectName(u"label_64")
        self.label_64.setGeometry(QRect(0, 0, 41, 31))
        self.label_64.setStyleSheet(u"font-family: Arial;\n"
"font-size:25px;\n"
"color:white;\n"
"font-weight: bold;\n"
"background:transparent;")
        self.label_64.setAlignment(Qt.AlignCenter)
        self.mesa50 = QWidget(self.groupBox_4)
        self.mesa50.setObjectName(u"mesa50")
        self.mesa50.setGeometry(QRect(1030, 480, 91, 81))
        self.mesa50.setStyleSheet(u"QWidget{\n"
"background:green;\n"
"border-radius:5px;\n"
"}")
        self.toolButton_52 = QToolButton(self.mesa50)
        self.toolButton_52.setObjectName(u"toolButton_52")
        self.toolButton_52.setGeometry(QRect(10, 30, 71, 51))
        self.toolButton_52.setStyleSheet(u"QToolButton{\n"
"background:transparent;\n"
"color:white;\n"
"}")
        self.toolButton_52.setIcon(icon13)
        self.toolButton_52.setIconSize(QSize(64, 64))
        self.label_65 = QLabel(self.mesa50)
        self.label_65.setObjectName(u"label_65")
        self.label_65.setGeometry(QRect(0, 0, 41, 31))
        self.label_65.setStyleSheet(u"font-family: Arial;\n"
"font-size:25px;\n"
"color:white;\n"
"font-weight: bold;\n"
"background:transparent;")
        self.label_65.setAlignment(Qt.AlignCenter)
        self.mesa42 = QWidget(self.groupBox_4)
        self.mesa42.setObjectName(u"mesa42")
        self.mesa42.setGeometry(QRect(150, 480, 91, 81))
        self.mesa42.setStyleSheet(u"QWidget{\n"
"background:green;\n"
"border-radius:5px;\n"
"}")
        self.toolButton_53 = QToolButton(self.mesa42)
        self.toolButton_53.setObjectName(u"toolButton_53")
        self.toolButton_53.setGeometry(QRect(10, 30, 71, 51))
        self.toolButton_53.setStyleSheet(u"QToolButton{\n"
"background:transparent;\n"
"color:white;\n"
"}")
        self.toolButton_53.setIcon(icon13)
        self.toolButton_53.setIconSize(QSize(64, 64))
        self.label_66 = QLabel(self.mesa42)
        self.label_66.setObjectName(u"label_66")
        self.label_66.setGeometry(QRect(0, 0, 41, 31))
        self.label_66.setStyleSheet(u"font-family: Arial;\n"
"font-size:25px;\n"
"color:white;\n"
"font-weight: bold;\n"
"background:transparent;")
        self.label_66.setAlignment(Qt.AlignCenter)
        self.f_produtos = QFrame(self.centralwidget)
        self.f_produtos.setObjectName(u"f_produtos")
        self.f_produtos.setEnabled(True)
        self.f_produtos.setGeometry(QRect(5, 90, 1190, 600))
        self.f_produtos.setStyleSheet(u"QFrame{\n"
"background:rgba(0,0,0,0.5);\n"
"border-radius:10px;\n"
"}\n"
"QGroupBox{\n"
"font-family: Trebuchet MS;\n"
"font-size: 20px;\n"
"font-weight: bold;\n"
"color:white;\n"
"background:transparent;\n"
"}\n"
"")
        self.f_produtos.setFrameShape(QFrame.StyledPanel)
        self.f_produtos.setFrameShadow(QFrame.Raised)
        self.groupBox_5 = QGroupBox(self.f_produtos)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setGeometry(QRect(30, 20, 351, 541))
        self.label_67 = QLabel(self.groupBox_5)
        self.label_67.setObjectName(u"label_67")
        self.label_67.setGeometry(QRect(20, 80, 81, 21))
        self.label_67.setStyleSheet(u"font-family:Trebuchet MS;\n"
"font-size:16px;\n"
"font-weight:bold;\n"
"color:white;\n"
"background:transparent;\n"
"border:none;")
        self.label_68 = QLabel(self.groupBox_5)
        self.label_68.setObjectName(u"label_68")
        self.label_68.setGeometry(QRect(20, 120, 81, 21))
        self.label_68.setStyleSheet(u"font-family:Trebuchet MS;\n"
"font-size:16px;\n"
"font-weight:bold;\n"
"color:white;\n"
"background:transparent;\n"
"border:none;")
        self.label_69 = QLabel(self.groupBox_5)
        self.label_69.setObjectName(u"label_69")
        self.label_69.setGeometry(QRect(20, 160, 91, 21))
        self.label_69.setStyleSheet(u"font-family:Trebuchet MS;\n"
"font-size:16px;\n"
"font-weight:bold;\n"
"color:white;\n"
"background:transparent;\n"
"border:none;")
        self.label_70 = QLabel(self.groupBox_5)
        self.label_70.setObjectName(u"label_70")
        self.label_70.setGeometry(QRect(20, 200, 81, 21))
        self.label_70.setStyleSheet(u"font-family:Trebuchet MS;\n"
"font-size:16px;\n"
"font-weight:bold;\n"
"color:white;\n"
"background:transparent;\n"
"border:none;")
        self.label_71 = QLabel(self.groupBox_5)
        self.label_71.setObjectName(u"label_71")
        self.label_71.setGeometry(QRect(20, 240, 81, 21))
        self.label_71.setStyleSheet(u"font-family:Trebuchet MS;\n"
"font-size:16px;\n"
"font-weight:bold;\n"
"color:white;\n"
"background:transparent;\n"
"border:none;")
        self.label_72 = QLabel(self.groupBox_5)
        self.label_72.setObjectName(u"label_72")
        self.label_72.setGeometry(QRect(20, 280, 81, 21))
        self.label_72.setStyleSheet(u"font-family:Trebuchet MS;\n"
"font-size:16px;\n"
"font-weight:bold;\n"
"color:white;\n"
"background:transparent;\n"
"border:none;")
        self.novo_prod_nome = QLineEdit(self.groupBox_5)
        self.novo_prod_nome.setObjectName(u"novo_prod_nome")
        self.novo_prod_nome.setGeometry(QRect(120, 80, 221, 20))
        self.novo_prod_nome.setStyleSheet(u"background:transparent;\n"
"font-family: Trebuchet MS;\n"
"font-size:16px;\n"
"color:white;\n"
"border:none;\n"
"border-bottom: 1px solid white;")
        self.novo_prod_marca = QLineEdit(self.groupBox_5)
        self.novo_prod_marca.setObjectName(u"novo_prod_marca")
        self.novo_prod_marca.setGeometry(QRect(120, 120, 221, 20))
        self.novo_prod_marca.setStyleSheet(u"background:transparent;\n"
"font-family: Trebuchet MS;\n"
"font-size:16px;\n"
"color:white;\n"
"border:none;\n"
"border-bottom: 1px solid white;")
        self.novo_prod_qtd = QLineEdit(self.groupBox_5)
        self.novo_prod_qtd.setObjectName(u"novo_prod_qtd")
        self.novo_prod_qtd.setGeometry(QRect(120, 160, 221, 20))
        self.novo_prod_qtd.setStyleSheet(u"background:transparent;\n"
"font-family: Trebuchet MS;\n"
"font-size:16px;\n"
"color:white;\n"
"border:none;\n"
"border-bottom: 1px solid white;")
        self.novo_prod_valor = QLineEdit(self.groupBox_5)
        self.novo_prod_valor.setObjectName(u"novo_prod_valor")
        self.novo_prod_valor.setGeometry(QRect(120, 200, 221, 20))
        self.novo_prod_valor.setStyleSheet(u"background:transparent;\n"
"font-family: Trebuchet MS;\n"
"font-size:16px;\n"
"color:white;\n"
"border:none;\n"
"border-bottom: 1px solid white;")
        self.novo_prod_categ = QComboBox(self.groupBox_5)
        self.novo_prod_categ.addItem("")
        self.novo_prod_categ.addItem("")
        self.novo_prod_categ.addItem("")
        self.novo_prod_categ.addItem("")
        self.novo_prod_categ.addItem("")
        self.novo_prod_categ.addItem("")
        self.novo_prod_categ.setObjectName(u"novo_prod_categ")
        self.novo_prod_categ.setGeometry(QRect(120, 240, 221, 22))
        self.novo_prod_categ.setStyleSheet(u"font-family:Trebuchet MS;\n"
"font-size:14px;\n"
"font-weight:bold;")
        self.novo_prod_descri = QTextEdit(self.groupBox_5)
        self.novo_prod_descri.setObjectName(u"novo_prod_descri")
        self.novo_prod_descri.setGeometry(QRect(120, 280, 221, 151))
        self.novo_prod_descri.setStyleSheet(u"background:white;\n"
"color:black;\n"
"font-size:16px;\n"
"font-family: Trebuchet MS;\n"
"font-weight: bold;")
        self.novo_prod_cadastrar = QPushButton(self.groupBox_5)
        self.novo_prod_cadastrar.setObjectName(u"novo_prod_cadastrar")
        self.novo_prod_cadastrar.setGeometry(QRect(120, 490, 111, 41))
        self.novo_prod_cadastrar.setCursor(QCursor(Qt.OpenHandCursor))
        self.novo_prod_cadastrar.setStyleSheet(u"QPushButton{\n"
"border:none;\n"
"border-radius:5px;\n"
"color:white;\n"
"background:#1C86EE;\n"
"font-family:Trebuchet MS;\n"
"font-weight:bold;\n"
"font-size:16px;\n"
"}\n"
"QPushButton:hover{\n"
"text-decoration:underline;\n"
"}\n"
"")
        self.groupBox_6 = QGroupBox(self.f_produtos)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.groupBox_6.setGeometry(QRect(420, 20, 351, 541))
        self.label_73 = QLabel(self.groupBox_6)
        self.label_73.setObjectName(u"label_73")
        self.label_73.setGeometry(QRect(0, 30, 351, 21))
        self.label_73.setStyleSheet(u"font-family:Trebuchet MS;\n"
"font-size:16px;\n"
"font-weight:bold;\n"
"color:white;\n"
"background:transparent;\n"
"border:none;")
        self.label_73.setAlignment(Qt.AlignCenter)
        self.edit_prod_nome_input = QLineEdit(self.groupBox_6)
        self.edit_prod_nome_input.setObjectName(u"edit_prod_nome_input")
        self.edit_prod_nome_input.setGeometry(QRect(70, 60, 221, 20))
        self.edit_prod_nome_input.setStyleSheet(u"background:transparent;\n"
"font-family: Trebuchet MS;\n"
"font-size:16px;\n"
"color:white;\n"
"border:none;\n"
"border-bottom: 1px solid white;")
        self.edit_prod_buscar = QPushButton(self.groupBox_6)
        self.edit_prod_buscar.setObjectName(u"edit_prod_buscar")
        self.edit_prod_buscar.setGeometry(QRect(120, 90, 101, 31))
        self.edit_prod_buscar.setCursor(QCursor(Qt.OpenHandCursor))
        self.edit_prod_buscar.setStyleSheet(u"QPushButton{\n"
"border:none;\n"
"border-radius:5px;\n"
"color:white;\n"
"background:#1C86EE;\n"
"font-family:Trebuchet MS;\n"
"font-weight:bold;\n"
"font-size:16px;\n"
"}\n"
"QPushButton:hover{\n"
"text-decoration:underline;\n"
"}\n"
"")
        self.label_74 = QLabel(self.groupBox_6)
        self.label_74.setObjectName(u"label_74")
        self.label_74.setGeometry(QRect(20, 210, 91, 21))
        self.label_74.setStyleSheet(u"font-family:Trebuchet MS;\n"
"font-size:16px;\n"
"font-weight:bold;\n"
"color:white;\n"
"background:transparent;\n"
"border:none;")
        self.edit_prod_marca = QLineEdit(self.groupBox_6)
        self.edit_prod_marca.setObjectName(u"edit_prod_marca")
        self.edit_prod_marca.setGeometry(QRect(120, 170, 221, 20))
        self.edit_prod_marca.setStyleSheet(u"background:transparent;\n"
"font-family: Trebuchet MS;\n"
"font-size:16px;\n"
"color:white;\n"
"border:none;\n"
"border-bottom: 1px solid white;")
        self.label_75 = QLabel(self.groupBox_6)
        self.label_75.setObjectName(u"label_75")
        self.label_75.setGeometry(QRect(20, 290, 81, 21))
        self.label_75.setStyleSheet(u"font-family:Trebuchet MS;\n"
"font-size:16px;\n"
"font-weight:bold;\n"
"color:white;\n"
"background:transparent;\n"
"border:none;")
        self.label_76 = QLabel(self.groupBox_6)
        self.label_76.setObjectName(u"label_76")
        self.label_76.setGeometry(QRect(20, 170, 81, 21))
        self.label_76.setStyleSheet(u"font-family:Trebuchet MS;\n"
"font-size:16px;\n"
"font-weight:bold;\n"
"color:white;\n"
"background:transparent;\n"
"border:none;")
        self.edit_prod_nome = QLineEdit(self.groupBox_6)
        self.edit_prod_nome.setObjectName(u"edit_prod_nome")
        self.edit_prod_nome.setGeometry(QRect(120, 130, 221, 20))
        self.edit_prod_nome.setStyleSheet(u"background:transparent;\n"
"font-family: Trebuchet MS;\n"
"font-size:16px;\n"
"color:white;\n"
"border:none;\n"
"border-bottom: 1px solid white;")
        self.edit_prod_categ = QComboBox(self.groupBox_6)
        self.edit_prod_categ.addItem("")
        self.edit_prod_categ.addItem("")
        self.edit_prod_categ.addItem("")
        self.edit_prod_categ.addItem("")
        self.edit_prod_categ.addItem("")
        self.edit_prod_categ.addItem("")
        self.edit_prod_categ.setObjectName(u"edit_prod_categ")
        self.edit_prod_categ.setGeometry(QRect(120, 290, 221, 22))
        self.edit_prod_categ.setStyleSheet(u"font-family:Trebuchet MS;\n"
"font-size:14px;\n"
"font-weight:bold;")
        self.edit_prod_descri = QTextEdit(self.groupBox_6)
        self.edit_prod_descri.setObjectName(u"edit_prod_descri")
        self.edit_prod_descri.setGeometry(QRect(120, 330, 221, 151))
        self.edit_prod_descri.setStyleSheet(u"background:white;\n"
"color:black;\n"
"font-size:16px;\n"
"font-family: Trebuchet MS;\n"
"font-weight: bold;")
        self.label_77 = QLabel(self.groupBox_6)
        self.label_77.setObjectName(u"label_77")
        self.label_77.setGeometry(QRect(20, 130, 81, 21))
        self.label_77.setStyleSheet(u"font-family:Trebuchet MS;\n"
"font-size:16px;\n"
"font-weight:bold;\n"
"color:white;\n"
"background:transparent;\n"
"border:none;")
        self.label_78 = QLabel(self.groupBox_6)
        self.label_78.setObjectName(u"label_78")
        self.label_78.setGeometry(QRect(20, 330, 81, 21))
        self.label_78.setStyleSheet(u"font-family:Trebuchet MS;\n"
"font-size:16px;\n"
"font-weight:bold;\n"
"color:white;\n"
"background:transparent;\n"
"border:none;")
        self.label_79 = QLabel(self.groupBox_6)
        self.label_79.setObjectName(u"label_79")
        self.label_79.setGeometry(QRect(20, 250, 81, 21))
        self.label_79.setStyleSheet(u"font-family:Trebuchet MS;\n"
"font-size:16px;\n"
"font-weight:bold;\n"
"color:white;\n"
"background:transparent;\n"
"border:none;")
        self.edit_prod_valor = QLineEdit(self.groupBox_6)
        self.edit_prod_valor.setObjectName(u"edit_prod_valor")
        self.edit_prod_valor.setGeometry(QRect(120, 250, 221, 20))
        self.edit_prod_valor.setStyleSheet(u"background:transparent;\n"
"font-family: Trebuchet MS;\n"
"font-size:16px;\n"
"color:white;\n"
"border:none;\n"
"border-bottom: 1px solid white;")
        self.edit_prod_qtd = QLineEdit(self.groupBox_6)
        self.edit_prod_qtd.setObjectName(u"edit_prod_qtd")
        self.edit_prod_qtd.setGeometry(QRect(120, 210, 221, 20))
        self.edit_prod_qtd.setStyleSheet(u"background:transparent;\n"
"font-family: Trebuchet MS;\n"
"font-size:16px;\n"
"color:white;\n"
"border:none;\n"
"border-bottom: 1px solid white;")
        self.edit_prod_salvar = QPushButton(self.groupBox_6)
        self.edit_prod_salvar.setObjectName(u"edit_prod_salvar")
        self.edit_prod_salvar.setGeometry(QRect(120, 490, 111, 41))
        self.edit_prod_salvar.setCursor(QCursor(Qt.OpenHandCursor))
        self.edit_prod_salvar.setStyleSheet(u"QPushButton{\n"
"border:none;\n"
"border-radius:5px;\n"
"color:white;\n"
"background:#1C86EE;\n"
"font-family:Trebuchet MS;\n"
"font-weight:bold;\n"
"font-size:16px;\n"
"}\n"
"QPushButton:hover{\n"
"text-decoration:underline;\n"
"}\n"
"")
        self.groupBox_7 = QGroupBox(self.f_produtos)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.groupBox_7.setGeometry(QRect(810, 20, 351, 541))
        self.delete_prod_nome = QLineEdit(self.groupBox_7)
        self.delete_prod_nome.setObjectName(u"delete_prod_nome")
        self.delete_prod_nome.setGeometry(QRect(120, 130, 221, 20))
        self.delete_prod_nome.setStyleSheet(u"background:transparent;\n"
"font-family: Trebuchet MS;\n"
"font-size:16px;\n"
"color:white;\n"
"border:none;\n"
"border-bottom: 1px solid white;")
        self.delete_prod_nome.setReadOnly(True)
        self.delete_prod_valor = QLineEdit(self.groupBox_7)
        self.delete_prod_valor.setObjectName(u"delete_prod_valor")
        self.delete_prod_valor.setGeometry(QRect(120, 250, 221, 20))
        self.delete_prod_valor.setStyleSheet(u"background:transparent;\n"
"font-family: Trebuchet MS;\n"
"font-size:16px;\n"
"color:white;\n"
"border:none;\n"
"border-bottom: 1px solid white;")
        self.delete_prod_valor.setReadOnly(True)
        self.delete_prod_nome_input = QLineEdit(self.groupBox_7)
        self.delete_prod_nome_input.setObjectName(u"delete_prod_nome_input")
        self.delete_prod_nome_input.setGeometry(QRect(70, 60, 221, 20))
        self.delete_prod_nome_input.setStyleSheet(u"background:transparent;\n"
"font-family: Trebuchet MS;\n"
"font-size:16px;\n"
"color:white;\n"
"border:none;\n"
"border-bottom: 1px solid white;")
        self.label_80 = QLabel(self.groupBox_7)
        self.label_80.setObjectName(u"label_80")
        self.label_80.setGeometry(QRect(20, 130, 81, 21))
        self.label_80.setStyleSheet(u"font-family:Trebuchet MS;\n"
"font-size:16px;\n"
"font-weight:bold;\n"
"color:white;\n"
"background:transparent;\n"
"border:none;")
        self.label_81 = QLabel(self.groupBox_7)
        self.label_81.setObjectName(u"label_81")
        self.label_81.setGeometry(QRect(20, 170, 81, 21))
        self.label_81.setStyleSheet(u"font-family:Trebuchet MS;\n"
"font-size:16px;\n"
"font-weight:bold;\n"
"color:white;\n"
"background:transparent;\n"
"border:none;")
        self.delete_prod_deletar = QPushButton(self.groupBox_7)
        self.delete_prod_deletar.setObjectName(u"delete_prod_deletar")
        self.delete_prod_deletar.setGeometry(QRect(120, 490, 111, 41))
        self.delete_prod_deletar.setCursor(QCursor(Qt.OpenHandCursor))
        self.delete_prod_deletar.setStyleSheet(u"QPushButton{\n"
"border:none;\n"
"border-radius:5px;\n"
"color:white;\n"
"background:#1C86EE;\n"
"font-family:Trebuchet MS;\n"
"font-weight:bold;\n"
"font-size:16px;\n"
"}\n"
"QPushButton:hover{\n"
"text-decoration:underline;\n"
"}\n"
"")
        self.label_82 = QLabel(self.groupBox_7)
        self.label_82.setObjectName(u"label_82")
        self.label_82.setGeometry(QRect(20, 330, 81, 21))
        self.label_82.setStyleSheet(u"font-family:Trebuchet MS;\n"
"font-size:16px;\n"
"font-weight:bold;\n"
"color:white;\n"
"background:transparent;\n"
"border:none;")
        self.label_83 = QLabel(self.groupBox_7)
        self.label_83.setObjectName(u"label_83")
        self.label_83.setGeometry(QRect(20, 210, 91, 21))
        self.label_83.setStyleSheet(u"font-family:Trebuchet MS;\n"
"font-size:16px;\n"
"font-weight:bold;\n"
"color:white;\n"
"background:transparent;\n"
"border:none;")
        self.delete_prod_descri = QTextEdit(self.groupBox_7)
        self.delete_prod_descri.setObjectName(u"delete_prod_descri")
        self.delete_prod_descri.setGeometry(QRect(120, 330, 221, 151))
        self.delete_prod_descri.setStyleSheet(u"background:white;\n"
"color:black;\n"
"font-size:16px;\n"
"font-family: Trebuchet MS;\n"
"font-weight: bold;")
        self.delete_prod_descri.setReadOnly(True)
        self.label_84 = QLabel(self.groupBox_7)
        self.label_84.setObjectName(u"label_84")
        self.label_84.setGeometry(QRect(20, 290, 81, 21))
        self.label_84.setStyleSheet(u"font-family:Trebuchet MS;\n"
"font-size:16px;\n"
"font-weight:bold;\n"
"color:white;\n"
"background:transparent;\n"
"border:none;")
        self.label_85 = QLabel(self.groupBox_7)
        self.label_85.setObjectName(u"label_85")
        self.label_85.setGeometry(QRect(0, 30, 351, 21))
        self.label_85.setStyleSheet(u"font-family:Trebuchet MS;\n"
"font-size:16px;\n"
"font-weight:bold;\n"
"color:white;\n"
"background:transparent;\n"
"border:none;")
        self.label_85.setAlignment(Qt.AlignCenter)
        self.delete_prod_buscar = QPushButton(self.groupBox_7)
        self.delete_prod_buscar.setObjectName(u"delete_prod_buscar")
        self.delete_prod_buscar.setGeometry(QRect(120, 90, 101, 31))
        self.delete_prod_buscar.setCursor(QCursor(Qt.OpenHandCursor))
        self.delete_prod_buscar.setStyleSheet(u"QPushButton{\n"
"border:none;\n"
"border-radius:5px;\n"
"color:white;\n"
"background:#1C86EE;\n"
"font-family:Trebuchet MS;\n"
"font-weight:bold;\n"
"font-size:16px;\n"
"}\n"
"QPushButton:hover{\n"
"text-decoration:underline;\n"
"}\n"
"")
        self.delete_prod_marca = QLineEdit(self.groupBox_7)
        self.delete_prod_marca.setObjectName(u"delete_prod_marca")
        self.delete_prod_marca.setGeometry(QRect(120, 170, 221, 20))
        self.delete_prod_marca.setStyleSheet(u"background:transparent;\n"
"font-family: Trebuchet MS;\n"
"font-size:16px;\n"
"color:white;\n"
"border:none;\n"
"border-bottom: 1px solid white;")
        self.delete_prod_marca.setReadOnly(True)
        self.label_86 = QLabel(self.groupBox_7)
        self.label_86.setObjectName(u"label_86")
        self.label_86.setGeometry(QRect(20, 250, 81, 21))
        self.label_86.setStyleSheet(u"font-family:Trebuchet MS;\n"
"font-size:16px;\n"
"font-weight:bold;\n"
"color:white;\n"
"background:transparent;\n"
"border:none;")
        self.delete_prod_qtd = QLineEdit(self.groupBox_7)
        self.delete_prod_qtd.setObjectName(u"delete_prod_qtd")
        self.delete_prod_qtd.setGeometry(QRect(120, 210, 221, 20))
        self.delete_prod_qtd.setStyleSheet(u"background:transparent;\n"
"font-family: Trebuchet MS;\n"
"font-size:16px;\n"
"color:white;\n"
"border:none;\n"
"border-bottom: 1px solid white;")
        self.delete_prod_qtd.setReadOnly(True)
        self.delete_prod_categ = QComboBox(self.groupBox_7)
        self.delete_prod_categ.addItem("")
        self.delete_prod_categ.addItem("")
        self.delete_prod_categ.addItem("")
        self.delete_prod_categ.addItem("")
        self.delete_prod_categ.addItem("")
        self.delete_prod_categ.addItem("")
        self.delete_prod_categ.setObjectName(u"delete_prod_categ")
        self.delete_prod_categ.setGeometry(QRect(120, 290, 221, 22))
        self.delete_prod_categ.setStyleSheet(u"font-family:Trebuchet MS;\n"
"font-size:14px;\n"
"font-weight:bold;")
        self.f_relatorios = QFrame(self.centralwidget)
        self.f_relatorios.setObjectName(u"f_relatorios")
        self.f_relatorios.setGeometry(QRect(5, 90, 1190, 600))
        self.f_relatorios.setStyleSheet(u"QFrame{\n"
"background:rgba(0,0,0,0.5);\n"
"border-radius:10px;\n"
"}")
        self.f_relatorios.setFrameShape(QFrame.StyledPanel)
        self.f_relatorios.setFrameShadow(QFrame.Raised)
        self.label_87 = QLabel(self.f_relatorios)
        self.label_87.setObjectName(u"label_87")
        self.label_87.setGeometry(QRect(10, 10, 171, 21))
        self.label_87.setStyleSheet(u"font-family:Trebuchet MS;\n"
"font-size:16px;\n"
"font-weight:bold;\n"
"color:white;\n"
"background:transparent;\n"
"border:none;")
        self.rel_dia_data = QDateEdit(self.f_relatorios)
        self.rel_dia_data.setObjectName(u"rel_dia_data")
        self.rel_dia_data.setGeometry(QRect(200, 10, 101, 22))
        self.rel_dia_data.setStyleSheet(u"background:transparent;\n"
"border:none;\n"
"font-family:Trebuchet MS;\n"
"font-size:14px;\n"
"color:white;\n"
"font-weight:bold;\n"
"text-decoration:underline;")
        self.rel_dia_buscar = QPushButton(self.f_relatorios)
        self.rel_dia_buscar.setObjectName(u"rel_dia_buscar")
        self.rel_dia_buscar.setGeometry(QRect(80, 50, 101, 31))
        self.rel_dia_buscar.setCursor(QCursor(Qt.OpenHandCursor))
        self.rel_dia_buscar.setStyleSheet(u"QPushButton{\n"
"border:none;\n"
"border-radius:5px;\n"
"color:white;\n"
"background:#1C86EE;\n"
"font-family:Trebuchet MS;\n"
"font-weight:bold;\n"
"font-size:16px;\n"
"}\n"
"QPushButton:hover{\n"
"text-decoration:underline;\n"
"}\n"
"")
        self.label_88 = QLabel(self.f_relatorios)
        self.label_88.setObjectName(u"label_88")
        self.label_88.setGeometry(QRect(430, 10, 181, 21))
        self.label_88.setStyleSheet(u"font-family:Trebuchet MS;\n"
"font-size:16px;\n"
"font-weight:bold;\n"
"color:white;\n"
"background:transparent;\n"
"border:none;")
        self.rel_mes = QComboBox(self.f_relatorios)
        self.rel_mes.addItem("")
        self.rel_mes.addItem("")
        self.rel_mes.addItem("")
        self.rel_mes.addItem("")
        self.rel_mes.addItem("")
        self.rel_mes.addItem("")
        self.rel_mes.addItem("")
        self.rel_mes.addItem("")
        self.rel_mes.addItem("")
        self.rel_mes.addItem("")
        self.rel_mes.addItem("")
        self.rel_mes.addItem("")
        self.rel_mes.setObjectName(u"rel_mes")
        self.rel_mes.setGeometry(QRect(620, 10, 69, 22))
        self.rel_mes.setStyleSheet(u"background:transparent;\n"
"border:none;\n"
"font-family:Trebuchet MS;\n"
"font-size:14px;\n"
"color:white;\n"
"font-weight:bold;\n"
"text-decoration:underline;")
        self.rel_buscar_mes = QPushButton(self.f_relatorios)
        self.rel_buscar_mes.setObjectName(u"rel_buscar_mes")
        self.rel_buscar_mes.setGeometry(QRect(500, 50, 101, 31))
        self.rel_buscar_mes.setCursor(QCursor(Qt.OpenHandCursor))
        self.rel_buscar_mes.setStyleSheet(u"QPushButton{\n"
"border:none;\n"
"border-radius:5px;\n"
"color:white;\n"
"background:#1C86EE;\n"
"font-family:Trebuchet MS;\n"
"font-weight:bold;\n"
"font-size:16px;\n"
"}\n"
"QPushButton:hover{\n"
"text-decoration:underline;\n"
"}\n"
"")
        self.label_89 = QLabel(self.f_relatorios)
        self.label_89.setObjectName(u"label_89")
        self.label_89.setGeometry(QRect(810, 10, 181, 21))
        self.label_89.setStyleSheet(u"font-family:Trebuchet MS;\n"
"font-size:16px;\n"
"font-weight:bold;\n"
"color:white;\n"
"background:transparent;\n"
"border:none;")
        self.rel_ano = QLineEdit(self.f_relatorios)
        self.rel_ano.setObjectName(u"rel_ano")
        self.rel_ano.setGeometry(QRect(1000, 10, 131, 20))
        self.rel_ano.setStyleSheet(u"background:transparent;\n"
"font-family: Trebuchet MS;\n"
"font-size:16px;\n"
"color:white;\n"
"border:none;\n"
"border-bottom: 1px solid white;\n"
"border-radius:0px;")
        self.rel_ano.setReadOnly(True)
        self.rel_buscar_ano = QPushButton(self.f_relatorios)
        self.rel_buscar_ano.setObjectName(u"rel_buscar_ano")
        self.rel_buscar_ano.setGeometry(QRect(940, 50, 101, 31))
        self.rel_buscar_ano.setCursor(QCursor(Qt.OpenHandCursor))
        self.rel_buscar_ano.setStyleSheet(u"QPushButton{\n"
"border:none;\n"
"border-radius:5px;\n"
"color:white;\n"
"background:#1C86EE;\n"
"font-family:Trebuchet MS;\n"
"font-weight:bold;\n"
"font-size:16px;\n"
"}\n"
"QPushButton:hover{\n"
"text-decoration:underline;\n"
"}\n"
"")
        self.groupBox_8 = QGroupBox(self.f_relatorios)
        self.groupBox_8.setObjectName(u"groupBox_8")
        self.groupBox_8.setGeometry(QRect(10, 90, 1171, 501))
        self.groupBox_8.setStyleSheet(u"background:transparent;\n"
"color:white;\n"
"font-family:Trebuchet MS;\n"
"font-size: 20px;\n"
"font-weight: bold;")
        self.rel_busca_resultado = QListView(self.groupBox_8)
        self.rel_busca_resultado.setObjectName(u"rel_busca_resultado")
        self.rel_busca_resultado.setGeometry(QRect(10, 30, 1151, 461))
        self.rel_busca_resultado.setStyleSheet(u"background:#1C86EE;\n"
"color:white;\n"
"font-family: Trebuchet MS;\n"
"font-size: 16px;\n"
"font-weight:bold;")
        self.f_estoque = QFrame(self.centralwidget)
        self.f_estoque.setObjectName(u"f_estoque")
        self.f_estoque.setGeometry(QRect(5, 90, 1190, 600))
        self.f_estoque.setStyleSheet(u"QFrame{\n"
"background:rgba(0,0,0,0.5);\n"
"border-radius:10px;\n"
"}")
        self.f_estoque.setFrameShape(QFrame.StyledPanel)
        self.f_estoque.setFrameShadow(QFrame.Raised)
        self.label_90 = QLabel(self.f_estoque)
        self.label_90.setObjectName(u"label_90")
        self.label_90.setGeometry(QRect(100, 20, 221, 21))
        self.label_90.setStyleSheet(u"font-family:Trebuchet MS;\n"
"font-size:16px;\n"
"font-weight:bold;\n"
"color:white;\n"
"background:transparent;\n"
"border:none;")
        self.estoque_nome_produto = QLineEdit(self.f_estoque)
        self.estoque_nome_produto.setObjectName(u"estoque_nome_produto")
        self.estoque_nome_produto.setGeometry(QRect(330, 20, 221, 20))
        self.estoque_nome_produto.setStyleSheet(u"border:none;\n"
"border-radius:0px;\n"
"border-bottom:1px solid white;\n"
"background:transparent;\n"
"color:white;\n"
"font-size:18px;\n"
"font-family: Trebuchet MS;")
        self.label_91 = QLabel(self.f_estoque)
        self.label_91.setObjectName(u"label_91")
        self.label_91.setGeometry(QRect(600, 20, 231, 21))
        self.label_91.setStyleSheet(u"font-family:Trebuchet MS;\n"
"font-size:16px;\n"
"font-weight:bold;\n"
"color:white;\n"
"background:transparent;\n"
"border:none;")
        self.estoque_categoria = QComboBox(self.f_estoque)
        self.estoque_categoria.addItem("")
        self.estoque_categoria.addItem("")
        self.estoque_categoria.addItem("")
        self.estoque_categoria.addItem("")
        self.estoque_categoria.addItem("")
        self.estoque_categoria.addItem("")
        self.estoque_categoria.setObjectName(u"estoque_categoria")
        self.estoque_categoria.setGeometry(QRect(840, 20, 221, 21))
        self.estoque_categoria.setStyleSheet(u"font-family:Trebuchet MS;\n"
"font-size:14px;\n"
"font-weight:bold;")
        self.estoque_buscar_produto = QPushButton(self.f_estoque)
        self.estoque_buscar_produto.setObjectName(u"estoque_buscar_produto")
        self.estoque_buscar_produto.setGeometry(QRect(270, 60, 101, 31))
        self.estoque_buscar_produto.setCursor(QCursor(Qt.OpenHandCursor))
        self.estoque_buscar_produto.setStyleSheet(u"QPushButton{\n"
"border:none;\n"
"border-radius:5px;\n"
"color:white;\n"
"background:#1C86EE;\n"
"font-family:Trebuchet MS;\n"
"font-weight:bold;\n"
"font-size:16px;\n"
"}\n"
"QPushButton:hover{\n"
"text-decoration:underline;\n"
"}\n"
"")
        self.estoque_buscar_categoria = QPushButton(self.f_estoque)
        self.estoque_buscar_categoria.setObjectName(u"estoque_buscar_categoria")
        self.estoque_buscar_categoria.setGeometry(QRect(780, 60, 101, 31))
        self.estoque_buscar_categoria.setCursor(QCursor(Qt.OpenHandCursor))
        self.estoque_buscar_categoria.setStyleSheet(u"QPushButton{\n"
"border:none;\n"
"border-radius:5px;\n"
"color:white;\n"
"background:#1C86EE;\n"
"font-family:Trebuchet MS;\n"
"font-weight:bold;\n"
"font-size:16px;\n"
"}\n"
"QPushButton:hover{\n"
"text-decoration:underline;\n"
"}\n"
"")
        self.groupBox_9 = QGroupBox(self.f_estoque)
        self.groupBox_9.setObjectName(u"groupBox_9")
        self.groupBox_9.setGeometry(QRect(10, 100, 1171, 491))
        self.groupBox_9.setStyleSheet(u"background:transparent;\n"
"color:white;\n"
"font-size:18px;\n"
"font-family: Trebuchet MS;\n"
"")
        self.estoque_produtos = QListView(self.groupBox_9)
        self.estoque_produtos.setObjectName(u"estoque_produtos")
        self.estoque_produtos.setGeometry(QRect(10, 20, 1151, 461))
        self.estoque_produtos.setStyleSheet(u"background:#1C86EE;\n"
"color:white;\n"
"font-family: Trebuchet MS;\n"
"font-size: 16px;\n"
"font-weight:bold;")
        self.f_developer = QFrame(self.centralwidget)
        self.f_developer.setObjectName(u"f_developer")
        self.f_developer.setGeometry(QRect(5, 90, 1190, 600))
        self.f_developer.setStyleSheet(u"background:rgba(0,0,0,0.5);\n"
"border-radius:10px;")
        self.f_developer.setFrameShape(QFrame.StyledPanel)
        self.f_developer.setFrameShadow(QFrame.Raised)
        self.toolButton = QToolButton(self.f_developer)
        self.toolButton.setObjectName(u"toolButton")
        self.toolButton.setGeometry(QRect(10, 20, 321, 171))
        self.toolButton.setStyleSheet(u"background:transparent;\n"
"")
        icon14 = QIcon()
        icon14.addFile(u":/menu/developer2.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton.setIcon(icon14)
        self.toolButton.setIconSize(QSize(256, 256))
        self.label_92 = QLabel(self.f_developer)
        self.label_92.setObjectName(u"label_92")
        self.label_92.setGeometry(QRect(240, 90, 681, 91))
        self.label_92.setStyleSheet(u"color:white;\n"
"font-family:Trebuchet MS;\n"
"font-size:30px;\n"
"font-weight:bold;\n"
"background:transparent;")
        self.label_92.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.label_93 = QLabel(self.f_developer)
        self.label_93.setObjectName(u"label_93")
        self.label_93.setGeometry(QRect(100, 210, 301, 41))
        self.label_93.setStyleSheet(u"color:white;\n"
"font-family:Trebuchet MS;\n"
"font-size:30px;\n"
"font-weight:bold;\n"
"background:transparent;")
        self.label_93.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.label_94 = QLabel(self.f_developer)
        self.label_94.setObjectName(u"label_94")
        self.label_94.setGeometry(QRect(100, 260, 391, 41))
        self.label_94.setStyleSheet(u"color:white;\n"
"font-family:Trebuchet MS;\n"
"font-size:30px;\n"
"font-weight:bold;\n"
"background:transparent;")
        self.label_94.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.label_95 = QLabel(self.f_developer)
        self.label_95.setObjectName(u"label_95")
        self.label_95.setGeometry(QRect(100, 320, 691, 41))
        self.label_95.setStyleSheet(u"color:white;\n"
"font-family:Trebuchet MS;\n"
"font-size:30px;\n"
"font-weight:bold;\n"
"background:transparent;")
        self.label_95.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.label_96 = QLabel(self.f_developer)
        self.label_96.setObjectName(u"label_96")
        self.label_96.setGeometry(QRect(100, 370, 931, 41))
        self.label_96.setStyleSheet(u"color:white;\n"
"font-family:Trebuchet MS;\n"
"font-size:30px;\n"
"font-weight:bold;\n"
"background:transparent;")
        self.label_96.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.groupBox_10 = QGroupBox(self.f_developer)
        self.groupBox_10.setObjectName(u"groupBox_10")
        self.groupBox_10.setGeometry(QRect(100, 419, 1041, 181))
        self.groupBox_10.setStyleSheet(u"color:white;\n"
"font-size:18px;\n"
"")
        self.toolButton_2 = QToolButton(self.groupBox_10)
        self.toolButton_2.setObjectName(u"toolButton_2")
        self.toolButton_2.setGeometry(QRect(280, 10, 51, 51))
        self.toolButton_2.setStyleSheet(u"background:transparent;")
        icon15 = QIcon()
        icon15.addFile(u":/menu/facebook_button.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_2.setIcon(icon15)
        self.toolButton_2.setIconSize(QSize(64, 64))
        self.label_97 = QLabel(self.groupBox_10)
        self.label_97.setObjectName(u"label_97")
        self.label_97.setGeometry(QRect(370, 40, 421, 16))
        self.label_97.setStyleSheet(u"background:transparent;")
        self.toolButton_3 = QToolButton(self.groupBox_10)
        self.toolButton_3.setObjectName(u"toolButton_3")
        self.toolButton_3.setGeometry(QRect(280, 70, 51, 41))
        self.toolButton_3.setStyleSheet(u"background:white;")
        icon16 = QIcon()
        icon16.addFile(u":/menu/github_button.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_3.setIcon(icon16)
        self.toolButton_3.setIconSize(QSize(64, 64))
        self.label_98 = QLabel(self.groupBox_10)
        self.label_98.setObjectName(u"label_98")
        self.label_98.setGeometry(QRect(370, 90, 421, 21))
        self.label_98.setStyleSheet(u"background:transparent;")
        self.toolButton_54 = QToolButton(self.groupBox_10)
        self.toolButton_54.setObjectName(u"toolButton_54")
        self.toolButton_54.setGeometry(QRect(280, 120, 51, 51))
        self.toolButton_54.setStyleSheet(u"background:transparent;")
        icon17 = QIcon()
        icon17.addFile(u":/menu/youtube_button.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_54.setIcon(icon17)
        self.toolButton_54.setIconSize(QSize(64, 64))
        self.label_99 = QLabel(self.groupBox_10)
        self.label_99.setObjectName(u"label_99")
        self.label_99.setGeometry(QRect(370, 140, 531, 21))
        self.label_99.setStyleSheet(u"background:transparent;")
        menu_window.setCentralWidget(self.centralwidget)
        self.f_pedidos.raise_()
        self.f_inicio.raise_()
        self.frame_bar.raise_()
        self.f_caixa.raise_()
        self.f_mesas.raise_()
        self.f_produtos.raise_()
        self.f_relatorios.raise_()
        self.f_estoque.raise_()
        self.f_developer.raise_()

        self.retranslateUi(menu_window)

        QMetaObject.connectSlotsByName(menu_window)
    # setupUi

    def retranslateUi(self, menu_window):
        menu_window.setWindowTitle(QCoreApplication.translate("menu_window", u"Restaurante Requinte - MENU", None))
        self.label_welcome.setText(QCoreApplication.translate("menu_window", u"Bem vindo Usuario.", None))
        self.button_pedido.setText(QCoreApplication.translate("menu_window", u" Pedidos", None))
        self.button_caixa.setText(QCoreApplication.translate("menu_window", u" Caixa", None))
        self.button_mesas.setText(QCoreApplication.translate("menu_window", u" Mesas", None))
        self.button_produtos.setText(QCoreApplication.translate("menu_window", u" Produtos", None))
        self.button_relatorio.setText(QCoreApplication.translate("menu_window", u" Relat\u00f3rios", None))
        self.button_cliente.setText(QCoreApplication.translate("menu_window", u" Estoque", None))
        self.button_usuario.setText(QCoreApplication.translate("menu_window", u" Developer", None))
        self.label.setText(QCoreApplication.translate("menu_window", u"SELECIONE A MESA:", None))
        self.box_mesas.setItemText(0, QCoreApplication.translate("menu_window", u"Balc\u00e3o", None))
        self.box_mesas.setItemText(1, QCoreApplication.translate("menu_window", u"Entrega", None))
        self.box_mesas.setItemText(2, QCoreApplication.translate("menu_window", u"01", None))
        self.box_mesas.setItemText(3, QCoreApplication.translate("menu_window", u"02", None))
        self.box_mesas.setItemText(4, QCoreApplication.translate("menu_window", u"03", None))
        self.box_mesas.setItemText(5, QCoreApplication.translate("menu_window", u"04", None))
        self.box_mesas.setItemText(6, QCoreApplication.translate("menu_window", u"05", None))
        self.box_mesas.setItemText(7, QCoreApplication.translate("menu_window", u"06", None))
        self.box_mesas.setItemText(8, QCoreApplication.translate("menu_window", u"07", None))
        self.box_mesas.setItemText(9, QCoreApplication.translate("menu_window", u"08", None))
        self.box_mesas.setItemText(10, QCoreApplication.translate("menu_window", u"09", None))
        self.box_mesas.setItemText(11, QCoreApplication.translate("menu_window", u"10", None))
        self.box_mesas.setItemText(12, QCoreApplication.translate("menu_window", u"11", None))
        self.box_mesas.setItemText(13, QCoreApplication.translate("menu_window", u"12", None))
        self.box_mesas.setItemText(14, QCoreApplication.translate("menu_window", u"13", None))
        self.box_mesas.setItemText(15, QCoreApplication.translate("menu_window", u"14", None))
        self.box_mesas.setItemText(16, QCoreApplication.translate("menu_window", u"15", None))
        self.box_mesas.setItemText(17, QCoreApplication.translate("menu_window", u"16", None))
        self.box_mesas.setItemText(18, QCoreApplication.translate("menu_window", u"17", None))
        self.box_mesas.setItemText(19, QCoreApplication.translate("menu_window", u"18", None))
        self.box_mesas.setItemText(20, QCoreApplication.translate("menu_window", u"19", None))
        self.box_mesas.setItemText(21, QCoreApplication.translate("menu_window", u"20", None))
        self.box_mesas.setItemText(22, QCoreApplication.translate("menu_window", u"21", None))
        self.box_mesas.setItemText(23, QCoreApplication.translate("menu_window", u"22", None))
        self.box_mesas.setItemText(24, QCoreApplication.translate("menu_window", u"23", None))
        self.box_mesas.setItemText(25, QCoreApplication.translate("menu_window", u"24", None))
        self.box_mesas.setItemText(26, QCoreApplication.translate("menu_window", u"25", None))
        self.box_mesas.setItemText(27, QCoreApplication.translate("menu_window", u"26", None))
        self.box_mesas.setItemText(28, QCoreApplication.translate("menu_window", u"27", None))
        self.box_mesas.setItemText(29, QCoreApplication.translate("menu_window", u"28", None))
        self.box_mesas.setItemText(30, QCoreApplication.translate("menu_window", u"29", None))
        self.box_mesas.setItemText(31, QCoreApplication.translate("menu_window", u"30", None))
        self.box_mesas.setItemText(32, QCoreApplication.translate("menu_window", u"31", None))
        self.box_mesas.setItemText(33, QCoreApplication.translate("menu_window", u"32", None))
        self.box_mesas.setItemText(34, QCoreApplication.translate("menu_window", u"33", None))
        self.box_mesas.setItemText(35, QCoreApplication.translate("menu_window", u"34", None))
        self.box_mesas.setItemText(36, QCoreApplication.translate("menu_window", u"35", None))
        self.box_mesas.setItemText(37, QCoreApplication.translate("menu_window", u"36", None))
        self.box_mesas.setItemText(38, QCoreApplication.translate("menu_window", u"37", None))
        self.box_mesas.setItemText(39, QCoreApplication.translate("menu_window", u"38", None))
        self.box_mesas.setItemText(40, QCoreApplication.translate("menu_window", u"39", None))
        self.box_mesas.setItemText(41, QCoreApplication.translate("menu_window", u"40", None))
        self.box_mesas.setItemText(42, QCoreApplication.translate("menu_window", u"41", None))
        self.box_mesas.setItemText(43, QCoreApplication.translate("menu_window", u"42", None))
        self.box_mesas.setItemText(44, QCoreApplication.translate("menu_window", u"43", None))
        self.box_mesas.setItemText(45, QCoreApplication.translate("menu_window", u"44", None))
        self.box_mesas.setItemText(46, QCoreApplication.translate("menu_window", u"45", None))
        self.box_mesas.setItemText(47, QCoreApplication.translate("menu_window", u"46", None))
        self.box_mesas.setItemText(48, QCoreApplication.translate("menu_window", u"47", None))
        self.box_mesas.setItemText(49, QCoreApplication.translate("menu_window", u"48", None))
        self.box_mesas.setItemText(50, QCoreApplication.translate("menu_window", u"49", None))
        self.box_mesas.setItemText(51, QCoreApplication.translate("menu_window", u"50", None))

        self.adicionar_button.setText("")
        self.editar_button.setText("")
        self.delete_button.setText("")
        self.table_button.setText("")
        self.table_button_2.setText("")
        self.label_2.setText(QCoreApplication.translate("menu_window", u"PRODUTOS ADQUIRIDOS:", None))
        self.groupBox.setTitle(QCoreApplication.translate("menu_window", u"Observa\u00e7\u00f5es", None))
        self.produto_confirmar.setText(QCoreApplication.translate("menu_window", u"CONFIRMAR", None))
        self.produto_limpar.setText(QCoreApplication.translate("menu_window", u"LIMPAR", None))
        self.endereco_box.setTitle(QCoreApplication.translate("menu_window", u"Endere\u00e7o para entrega", None))
        self.label_3.setText(QCoreApplication.translate("menu_window", u"CEP:", None))
        self.label_4.setText(QCoreApplication.translate("menu_window", u"ENDERE\u00c7O:", None))
        self.label_5.setText(QCoreApplication.translate("menu_window", u"NUMERO:", None))
        self.label_6.setText(QCoreApplication.translate("menu_window", u"BAIRRO:", None))
        self.label_7.setText(QCoreApplication.translate("menu_window", u"COMPLEMENTO:", None))
        self.label_8.setText("")
        self.label_9.setText("")
        self.label_10.setText("")
        self.label_11.setText("")
        self.produto_buscar.setText(QCoreApplication.translate("menu_window", u"BUSCAR", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("menu_window", u"CADASTRO DE ABERTURA DE CAIXA", None))
        self.label_12.setText(QCoreApplication.translate("menu_window", u"Valor:", None))
        self.label_13.setText(QCoreApplication.translate("menu_window", u"Data:", None))
        self.confirmar_abertura.setText(QCoreApplication.translate("menu_window", u"CONFIRMAR", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("menu_window", u"FECHAMENTO DE CAIXA", None))
        self.label_14.setText(QCoreApplication.translate("menu_window", u"Selecione uma data para o fechamento:", None))
        self.fecha_buscar.setText(QCoreApplication.translate("menu_window", u"BUSCAR", None))
        self.label_15.setText(QCoreApplication.translate("menu_window", u"Valor do caixa:", None))
        self.label_16.setText(QCoreApplication.translate("menu_window", u"Status:", None))
        self.fecha_confirmar.setText(QCoreApplication.translate("menu_window", u"CONFIRMAR", None))
        self.fecha_status.setText("")
        self.fecha_valor.setText("")
        self.groupBox_4.setTitle(QCoreApplication.translate("menu_window", u"LISTA DE MESAS", None))
        self.toolButton_4.setText("")
        self.label_17.setText(QCoreApplication.translate("menu_window", u"01", None))
        self.toolButton_5.setText("")
        self.label_18.setText(QCoreApplication.translate("menu_window", u"02", None))
        self.toolButton_6.setText("")
        self.label_19.setText(QCoreApplication.translate("menu_window", u"03", None))
        self.toolButton_7.setText("")
        self.label_20.setText(QCoreApplication.translate("menu_window", u"04", None))
        self.toolButton_8.setText("")
        self.label_21.setText(QCoreApplication.translate("menu_window", u"05", None))
        self.toolButton_9.setText("")
        self.label_22.setText(QCoreApplication.translate("menu_window", u"06", None))
        self.toolButton_10.setText("")
        self.label_23.setText(QCoreApplication.translate("menu_window", u"07", None))
        self.toolButton_11.setText("")
        self.label_24.setText(QCoreApplication.translate("menu_window", u"08", None))
        self.toolButton_12.setText("")
        self.label_25.setText(QCoreApplication.translate("menu_window", u"09", None))
        self.toolButton_13.setText("")
        self.label_26.setText(QCoreApplication.translate("menu_window", u"10", None))
        self.toolButton_14.setText("")
        self.label_27.setText(QCoreApplication.translate("menu_window", u"11", None))
        self.toolButton_15.setText("")
        self.label_28.setText(QCoreApplication.translate("menu_window", u"21", None))
        self.toolButton_16.setText("")
        self.label_29.setText(QCoreApplication.translate("menu_window", u"31", None))
        self.toolButton_17.setText("")
        self.label_30.setText(QCoreApplication.translate("menu_window", u"41", None))
        self.toolButton_18.setText("")
        self.label_31.setText(QCoreApplication.translate("menu_window", u"17", None))
        self.toolButton_19.setText("")
        self.label_32.setText(QCoreApplication.translate("menu_window", u"15", None))
        self.toolButton_20.setText("")
        self.label_33.setText(QCoreApplication.translate("menu_window", u"19", None))
        self.toolButton_21.setText("")
        self.label_34.setText(QCoreApplication.translate("menu_window", u"14", None))
        self.toolButton_22.setText("")
        self.label_35.setText(QCoreApplication.translate("menu_window", u"16", None))
        self.toolButton_23.setText("")
        self.label_36.setText(QCoreApplication.translate("menu_window", u"18", None))
        self.toolButton_24.setText("")
        self.label_37.setText(QCoreApplication.translate("menu_window", u"13", None))
        self.toolButton_25.setText("")
        self.label_38.setText(QCoreApplication.translate("menu_window", u"20", None))
        self.toolButton_26.setText("")
        self.label_39.setText(QCoreApplication.translate("menu_window", u"12", None))
        self.toolButton_27.setText("")
        self.label_40.setText(QCoreApplication.translate("menu_window", u"27", None))
        self.toolButton_28.setText("")
        self.label_41.setText(QCoreApplication.translate("menu_window", u"25", None))
        self.toolButton_29.setText("")
        self.label_42.setText(QCoreApplication.translate("menu_window", u"29", None))
        self.toolButton_30.setText("")
        self.label_43.setText(QCoreApplication.translate("menu_window", u"24", None))
        self.toolButton_31.setText("")
        self.label_44.setText(QCoreApplication.translate("menu_window", u"26", None))
        self.toolButton_32.setText("")
        self.label_45.setText(QCoreApplication.translate("menu_window", u"28", None))
        self.toolButton_33.setText("")
        self.label_46.setText(QCoreApplication.translate("menu_window", u"23", None))
        self.toolButton_34.setText("")
        self.label_47.setText(QCoreApplication.translate("menu_window", u"30", None))
        self.toolButton_35.setText("")
        self.label_48.setText(QCoreApplication.translate("menu_window", u"22", None))
        self.toolButton_36.setText("")
        self.label_49.setText(QCoreApplication.translate("menu_window", u"37", None))
        self.toolButton_37.setText("")
        self.label_50.setText(QCoreApplication.translate("menu_window", u"35", None))
        self.toolButton_38.setText("")
        self.label_51.setText(QCoreApplication.translate("menu_window", u"39", None))
        self.toolButton_39.setText("")
        self.label_52.setText(QCoreApplication.translate("menu_window", u"34", None))
        self.toolButton_40.setText("")
        self.label_53.setText(QCoreApplication.translate("menu_window", u"36", None))
        self.toolButton_41.setText("")
        self.label_54.setText(QCoreApplication.translate("menu_window", u"38", None))
        self.toolButton_42.setText("")
        self.label_55.setText(QCoreApplication.translate("menu_window", u"33", None))
        self.toolButton_43.setText("")
        self.label_56.setText(QCoreApplication.translate("menu_window", u"40", None))
        self.toolButton_44.setText("")
        self.label_57.setText(QCoreApplication.translate("menu_window", u"32", None))
        self.toolButton_45.setText("")
        self.label_58.setText(QCoreApplication.translate("menu_window", u"47", None))
        self.toolButton_46.setText("")
        self.label_59.setText(QCoreApplication.translate("menu_window", u"45", None))
        self.toolButton_47.setText("")
        self.label_60.setText(QCoreApplication.translate("menu_window", u"49", None))
        self.toolButton_48.setText("")
        self.label_61.setText(QCoreApplication.translate("menu_window", u"44", None))
        self.toolButton_49.setText("")
        self.label_62.setText(QCoreApplication.translate("menu_window", u"46", None))
        self.toolButton_50.setText("")
        self.label_63.setText(QCoreApplication.translate("menu_window", u"48", None))
        self.toolButton_51.setText("")
        self.label_64.setText(QCoreApplication.translate("menu_window", u"43", None))
        self.toolButton_52.setText("")
        self.label_65.setText(QCoreApplication.translate("menu_window", u"50", None))
        self.toolButton_53.setText("")
        self.label_66.setText(QCoreApplication.translate("menu_window", u"42", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("menu_window", u"CADASTRAR PRODUTOS", None))
        self.label_67.setText(QCoreApplication.translate("menu_window", u"Nome:", None))
        self.label_68.setText(QCoreApplication.translate("menu_window", u"Marca:", None))
        self.label_69.setText(QCoreApplication.translate("menu_window", u"Quantidade:", None))
        self.label_70.setText(QCoreApplication.translate("menu_window", u"Valor:", None))
        self.label_71.setText(QCoreApplication.translate("menu_window", u"Categoria:", None))
        self.label_72.setText(QCoreApplication.translate("menu_window", u"Descri\u00e7\u00e3o:", None))
        self.novo_prod_categ.setItemText(0, QCoreApplication.translate("menu_window", u"Bebidas", None))
        self.novo_prod_categ.setItemText(1, QCoreApplication.translate("menu_window", u"Lanches", None))
        self.novo_prod_categ.setItemText(2, QCoreApplication.translate("menu_window", u"Refei\u00e7\u00f5es", None))
        self.novo_prod_categ.setItemText(3, QCoreApplication.translate("menu_window", u"Por\u00e7\u00f5es", None))
        self.novo_prod_categ.setItemText(4, QCoreApplication.translate("menu_window", u"Diversos", None))
        self.novo_prod_categ.setItemText(5, QCoreApplication.translate("menu_window", u"Sobremesas", None))

        self.novo_prod_cadastrar.setText(QCoreApplication.translate("menu_window", u"CADASTRAR", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("menu_window", u"EDITAR PRODUTOS", None))
        self.label_73.setText(QCoreApplication.translate("menu_window", u"Busca pelo nome do produto:", None))
        self.edit_prod_nome_input.setInputMask("")
        self.edit_prod_nome_input.setPlaceholderText(QCoreApplication.translate("menu_window", u"Digite o nome do produto", None))
        self.edit_prod_buscar.setText(QCoreApplication.translate("menu_window", u"BUSCAR", None))
        self.label_74.setText(QCoreApplication.translate("menu_window", u"Quantidade:", None))
        self.label_75.setText(QCoreApplication.translate("menu_window", u"Categoria:", None))
        self.label_76.setText(QCoreApplication.translate("menu_window", u"Marca:", None))
        self.edit_prod_categ.setItemText(0, QCoreApplication.translate("menu_window", u"Bebidas", None))
        self.edit_prod_categ.setItemText(1, QCoreApplication.translate("menu_window", u"Lanches", None))
        self.edit_prod_categ.setItemText(2, QCoreApplication.translate("menu_window", u"Refei\u00e7\u00f5es", None))
        self.edit_prod_categ.setItemText(3, QCoreApplication.translate("menu_window", u"Por\u00e7\u00f5es", None))
        self.edit_prod_categ.setItemText(4, QCoreApplication.translate("menu_window", u"Diversos", None))
        self.edit_prod_categ.setItemText(5, QCoreApplication.translate("menu_window", u"Sobremesas", None))

        self.label_77.setText(QCoreApplication.translate("menu_window", u"Nome:", None))
        self.label_78.setText(QCoreApplication.translate("menu_window", u"Descri\u00e7\u00e3o:", None))
        self.label_79.setText(QCoreApplication.translate("menu_window", u"Valor:", None))
        self.edit_prod_salvar.setText(QCoreApplication.translate("menu_window", u"SALVAR", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("menu_window", u"DELETAR PRODUTO", None))
        self.delete_prod_nome_input.setInputMask("")
        self.delete_prod_nome_input.setPlaceholderText(QCoreApplication.translate("menu_window", u"Digite o nome do produto", None))
        self.label_80.setText(QCoreApplication.translate("menu_window", u"Nome:", None))
        self.label_81.setText(QCoreApplication.translate("menu_window", u"Marca:", None))
        self.delete_prod_deletar.setText(QCoreApplication.translate("menu_window", u"DELETAR", None))
        self.label_82.setText(QCoreApplication.translate("menu_window", u"Descri\u00e7\u00e3o:", None))
        self.label_83.setText(QCoreApplication.translate("menu_window", u"Quantidade:", None))
        self.label_84.setText(QCoreApplication.translate("menu_window", u"Categoria:", None))
        self.label_85.setText(QCoreApplication.translate("menu_window", u"Busca pelo nome do produto:", None))
        self.delete_prod_buscar.setText(QCoreApplication.translate("menu_window", u"BUSCAR", None))
        self.label_86.setText(QCoreApplication.translate("menu_window", u"Valor:", None))
        self.delete_prod_categ.setItemText(0, QCoreApplication.translate("menu_window", u"Bebidas", None))
        self.delete_prod_categ.setItemText(1, QCoreApplication.translate("menu_window", u"Lanches", None))
        self.delete_prod_categ.setItemText(2, QCoreApplication.translate("menu_window", u"Refei\u00e7\u00f5es", None))
        self.delete_prod_categ.setItemText(3, QCoreApplication.translate("menu_window", u"Por\u00e7\u00f5es", None))
        self.delete_prod_categ.setItemText(4, QCoreApplication.translate("menu_window", u"Diversos", None))
        self.delete_prod_categ.setItemText(5, QCoreApplication.translate("menu_window", u"Sobremesas", None))

        self.label_87.setText(QCoreApplication.translate("menu_window", u"Buscar vendas por dia:", None))
        self.rel_dia_buscar.setText(QCoreApplication.translate("menu_window", u"BUSCAR", None))
        self.label_88.setText(QCoreApplication.translate("menu_window", u"Buscar vendas por m\u00eas:", None))
        self.rel_mes.setItemText(0, QCoreApplication.translate("menu_window", u"01", None))
        self.rel_mes.setItemText(1, QCoreApplication.translate("menu_window", u"02", None))
        self.rel_mes.setItemText(2, QCoreApplication.translate("menu_window", u"03", None))
        self.rel_mes.setItemText(3, QCoreApplication.translate("menu_window", u"04", None))
        self.rel_mes.setItemText(4, QCoreApplication.translate("menu_window", u"05", None))
        self.rel_mes.setItemText(5, QCoreApplication.translate("menu_window", u"06", None))
        self.rel_mes.setItemText(6, QCoreApplication.translate("menu_window", u"07", None))
        self.rel_mes.setItemText(7, QCoreApplication.translate("menu_window", u"08", None))
        self.rel_mes.setItemText(8, QCoreApplication.translate("menu_window", u"09", None))
        self.rel_mes.setItemText(9, QCoreApplication.translate("menu_window", u"10", None))
        self.rel_mes.setItemText(10, QCoreApplication.translate("menu_window", u"11", None))
        self.rel_mes.setItemText(11, QCoreApplication.translate("menu_window", u"112", None))

        self.rel_buscar_mes.setText(QCoreApplication.translate("menu_window", u"BUSCAR", None))
        self.label_89.setText(QCoreApplication.translate("menu_window", u"Buscar vendas por ano:", None))
        self.rel_buscar_ano.setText(QCoreApplication.translate("menu_window", u"BUSCAR", None))
        self.groupBox_8.setTitle(QCoreApplication.translate("menu_window", u"Vendas", None))
        self.label_90.setText(QCoreApplication.translate("menu_window", u"Buscar estoque por produto:", None))
        self.label_91.setText(QCoreApplication.translate("menu_window", u"Buscar estoque por categoria:", None))
        self.estoque_categoria.setItemText(0, QCoreApplication.translate("menu_window", u"Bebidas", None))
        self.estoque_categoria.setItemText(1, QCoreApplication.translate("menu_window", u"Lanches", None))
        self.estoque_categoria.setItemText(2, QCoreApplication.translate("menu_window", u"Refei\u00e7\u00f5es", None))
        self.estoque_categoria.setItemText(3, QCoreApplication.translate("menu_window", u"Por\u00e7\u00f5es", None))
        self.estoque_categoria.setItemText(4, QCoreApplication.translate("menu_window", u"Diversos", None))
        self.estoque_categoria.setItemText(5, QCoreApplication.translate("menu_window", u"Sobremesas", None))

        self.estoque_buscar_produto.setText(QCoreApplication.translate("menu_window", u"BUSCAR", None))
        self.estoque_buscar_categoria.setText(QCoreApplication.translate("menu_window", u"BUSCAR", None))
        self.groupBox_9.setTitle(QCoreApplication.translate("menu_window", u"Produtos", None))
        self.toolButton.setText("")
        self.label_92.setText(QCoreApplication.translate("menu_window", u"Developer:Wendell santos", None))
        self.label_93.setText(QCoreApplication.translate("menu_window", u"Age: 22 Anos", None))
        self.label_94.setText(QCoreApplication.translate("menu_window", u".", None))
        self.label_95.setText(QCoreApplication.translate("menu_window", u"Skills: Python 3 , Html 5 , Css 3 and JavaScript.", None))
        self.label_96.setText(QCoreApplication.translate("menu_window", u"Frameworks: Tkinter, Pyqt5, Flask, Django, PHP, java,javascript and Bootstrap.", None))
        self.groupBox_10.setTitle(QCoreApplication.translate("menu_window", u"Social Networks", None))
        self.toolButton_2.setText("")
        self.label_98.setText(QCoreApplication.translate("menu_window", u"https://github.com/wendellsantos2", None))
    # retranslateUi

