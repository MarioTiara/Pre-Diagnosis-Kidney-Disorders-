from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_GUI_1(object):
    def setupUi(self, GUI_1):
        GUI_1.setObjectName("GUI_1")
        GUI_1.resize(1024, 768)
        GUI_1.setAutoFillBackground(False)
        GUI_1.setStyleSheet("#GUI_1\n"
"{\n"
"    background:rgb(255, 255, 255);\n"
"}")
        self.pushButton_1_2 = QtWidgets.QPushButton(GUI_1)
        self.pushButton_1_2.setGeometry(QtCore.QRect(0, 10, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(6)
        self.pushButton_1_2.setFont(font)
        self.pushButton_1_2.setStyleSheet("QPushButton\n"
"{\n"
"background:rgb(255, 255, 255);\n"
"border-radius:20px;\n"
"}\n"
"    ")
        self.pushButton_1_2.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/icon/light-bulb.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_1_2.setIcon(icon)
        self.pushButton_1_2.setIconSize(QtCore.QSize(15, 30))
        self.pushButton_1_2.setObjectName("pushButton_1_2")
        self.frame_1_1 = QtWidgets.QFrame(GUI_1)
        self.frame_1_1.setGeometry(QtCore.QRect(20, 450, 961, 271))
        self.frame_1_1.setStyleSheet("QFrame\n"
"{\n"
"background:rgba(0, 0, 0, 0.7);\n"
"border-radius:50px;\n"
" \n"
"}")
        self.frame_1_1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_1_1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_1_1.setObjectName("frame_1_1")
        self.groupBox_1_1 = QtWidgets.QGroupBox(self.frame_1_1)
        self.groupBox_1_1.setGeometry(QtCore.QRect(40, 40, 891, 191))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_1_1.setFont(font)
        self.groupBox_1_1.setStyleSheet("QGroupBox\n"
"{\n"
"color:rgb(255, 255, 255);\n"
"}")
        self.groupBox_1_1.setObjectName("groupBox_1_1")
        self.pushButton_1_4 = QtWidgets.QPushButton(self.groupBox_1_1)
        self.pushButton_1_4.setGeometry(QtCore.QRect(20, 70, 61, 51))
        font = QtGui.QFont()
        font.setPointSize(6)
        self.pushButton_1_4.setFont(font)
        self.pushButton_1_4.setStyleSheet("QPushButton\n"
"{\n"
"background:rgb(255, 255, 255);\n"
"border-radius:15px;\n"
"}")
        self.pushButton_1_4.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images/icon/settings.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_1_4.setIcon(icon1)
        self.pushButton_1_4.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_1_4.setObjectName("pushButton_1_4")
        self.pushButton_1_7 = QtWidgets.QPushButton(self.groupBox_1_1)
        self.pushButton_1_7.setGeometry(QtCore.QRect(800, 60, 51, 41))
        self.pushButton_1_7.setStyleSheet("QPushButton\n"
"{\n"
"background:rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"}")
        self.pushButton_1_7.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("images/icon/clock - Copy.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_1_7.setIcon(icon2)
        self.pushButton_1_7.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_1_7.setObjectName("pushButton_1_7")
        self.label_1_4 = QtWidgets.QLabel(self.groupBox_1_1)
        self.label_1_4.setGeometry(QtCore.QRect(20, 120, 131, 61))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_1_4.setFont(font)
        self.label_1_4.setStyleSheet("QLabel\n"
"{\n"
"background:transparent;\n"
"color:rgb(255, 255, 255);\n"
"}")
        self.label_1_4.setObjectName("label_1_4")
        self.label_1_7 = QtWidgets.QLabel(self.groupBox_1_1)
        self.label_1_7.setGeometry(QtCore.QRect(770, 130, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_1_7.setFont(font)
        self.label_1_7.setStyleSheet("QLabel\n"
"{\n"
"background:transparent;\n"
"color:rgb(255, 255, 255);\n"
"}")
        self.label_1_7.setObjectName("label_1_7")
        self.label = QtWidgets.QLabel(GUI_1)
        self.label.setGeometry(QtCore.QRect(320, 90, 331, 221))
        self.label.setStyleSheet("image: url(:/newPrefix/thumb-300x300.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_1_8 = QtWidgets.QLabel(GUI_1)
        self.label_1_8.setGeometry(QtCore.QRect(110, 20, 831, 61))
        font = QtGui.QFont()
        font.setFamily("Century751 No2 BT")
        font.setPointSize(32)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_1_8.setFont(font)
        self.label_1_8.setStyleSheet("QLabel\n"
"{\n"
"background:transparent;\n"
"color:rgb(170, 0, 0);\n"
"}")
        self.label_1_8.setObjectName("label_1_8")
        self.comboBox_1_1 = QtWidgets.QComboBox(GUI_1)
        self.comboBox_1_1.setGeometry(QtCore.QRect(280, 315, 401, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.comboBox_1_1.setFont(font)
        self.comboBox_1_1.setStyleSheet("QComboBox\n"
"{\n"
"background:rgb(255, 255, 255);\n"
"border-radius:5px;\n"
"color:rgb(182, 5, 5);\n"
"}")
        self.comboBox_1_1.setObjectName("comboBox_1_1")
        self.label_1_2 = QtWidgets.QLabel(GUI_1)
        self.label_1_2.setGeometry(QtCore.QRect(920, 0, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Britannic Bold")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_1_2.setFont(font)
        self.label_1_2.setStyleSheet("QLabel\n"
"{\n"
"background:transparent;\n"
"color:rgb(255, 255, 255);\n"
"}")
        self.label_1_2.setObjectName("label_1_2")
        self.toolButton_1_1 = QtWidgets.QToolButton(GUI_1)
        self.toolButton_1_1.setGeometry(QtCore.QRect(440, 380, 131, 101))
        self.toolButton_1_1.setStyleSheet("QToolButton\n"
"{\n"
"background:rgb(167, 27, 3);\n"
"border-radius:20px;\n"
" \n"
"}")
        self.toolButton_1_1.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("images/icon/document-2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_1_1.setIcon(icon3)
        self.toolButton_1_1.setIconSize(QtCore.QSize(150, 250))
        self.toolButton_1_1.setObjectName("toolButton_1_1")
        self.label.raise_()
        self.frame_1_1.raise_()
        self.pushButton_1_2.raise_()
        self.label_1_8.raise_()
        self.comboBox_1_1.raise_()
        self.label_1_2.raise_()
        self.toolButton_1_1.raise_()

        self.retranslateUi(GUI_1)
        QtCore.QMetaObject.connectSlotsByName(GUI_1)

    def retranslateUi(self, GUI_1):
        _translate = QtCore.QCoreApplication.translate
        GUI_1.setWindowTitle(_translate("GUI_1", "GUI_1"))
        self.groupBox_1_1.setTitle(_translate("GUI_1", "File Exstention"))
        self.label_1_4.setText(_translate("GUI_1", "Setting Up"))
        self.label_1_7.setText(_translate("GUI_1", "Proses Klik"))
        self.label_1_8.setText(_translate("GUI_1", "PRE-DIAGNOSIS GANGGUAN GINJAL"))
        self.label_1_2.setText(_translate("GUI_1", "Login"))
        self.comboBox_1_1.addItem("Login Diagnosis")
        self.comboBox_1_1.addItem("Login Diagnosis")

