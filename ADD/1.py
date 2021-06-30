# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '1.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_GUI_1(object):
    def setupUi(self, GUI_1):
        GUI_1.setObjectName("GUI_1")
        GUI_1.resize(470, 290)
        GUI_1.setAutoFillBackground(False)
        GUI_1.setStyleSheet("#GUI_1\n"
"{\n"
"    background:rgb(255, 255, 255);\n"
"}")
        self.label_1_1 = QtWidgets.QLabel(GUI_1)
        self.label_1_1.setGeometry(QtCore.QRect(440, 20, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(6)
        self.label_1_1.setFont(font)
        self.label_1_1.setObjectName("label_1_1")
        self.pushButton_1_2 = QtWidgets.QPushButton(GUI_1)
        self.pushButton_1_2.setGeometry(QtCore.QRect(430, 0, 41, 31))
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
        self.frame_1_1.setGeometry(QtCore.QRect(-20, 110, 511, 191))
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
        self.groupBox_1_1.setGeometry(QtCore.QRect(30, 110, 451, 61))
        font = QtGui.QFont()
        font.setPointSize(6)
        self.groupBox_1_1.setFont(font)
        self.groupBox_1_1.setStyleSheet("QGroupBox\n"
"{\n"
"color:rgb(255, 255, 255);\n"
"}")
        self.groupBox_1_1.setObjectName("groupBox_1_1")
        self.pushButton_1_4 = QtWidgets.QPushButton(self.groupBox_1_1)
        self.pushButton_1_4.setGeometry(QtCore.QRect(10, 10, 31, 31))
        self.pushButton_1_4.setStyleSheet("QPushButton\n"
"{\n"
"background:rgb(255, 255, 255);\n"
"border-radius:15px;\n"
"}")
        self.pushButton_1_4.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images/icon/settings.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_1_4.setIcon(icon1)
        self.pushButton_1_4.setIconSize(QtCore.QSize(20, 40))
        self.pushButton_1_4.setObjectName("pushButton_1_4")
        self.pushButton_1_7 = QtWidgets.QPushButton(self.groupBox_1_1)
        self.pushButton_1_7.setGeometry(QtCore.QRect(330, 10, 101, 31))
        self.pushButton_1_7.setStyleSheet("QPushButton\n"
"{\n"
"background:rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"}")
        self.pushButton_1_7.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("images/icon/clock - Copy.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_1_7.setIcon(icon2)
        self.pushButton_1_7.setIconSize(QtCore.QSize(50, 30))
        self.pushButton_1_7.setObjectName("pushButton_1_7")
        self.label_1_4 = QtWidgets.QLabel(self.groupBox_1_1)
        self.label_1_4.setGeometry(QtCore.QRect(10, 30, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(7)
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
        self.label_1_7.setGeometry(QtCore.QRect(350, 30, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_1_7.setFont(font)
        self.label_1_7.setStyleSheet("QLabel\n"
"{\n"
"background:transparent;\n"
"color:rgb(255, 255, 255);\n"
"}")
        self.label_1_7.setObjectName("label_1_7")
        self.label_1_2 = QtWidgets.QLabel(self.frame_1_1)
        self.label_1_2.setGeometry(QtCore.QRect(230, 30, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
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
        self.comboBox_1_1 = QtWidgets.QComboBox(self.frame_1_1)
        self.comboBox_1_1.setGeometry(QtCore.QRect(160, 70, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
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
        self.toolButton_1_1 = QtWidgets.QToolButton(GUI_1)
        self.toolButton_1_1.setGeometry(QtCore.QRect(170, 70, 141, 71))
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
        self.toolButton_1_1.setIconSize(QtCore.QSize(100, 200))
        self.toolButton_1_1.setObjectName("toolButton_1_1")
        self.label_1_3 = QtWidgets.QLabel(GUI_1)
        self.label_1_3.setGeometry(QtCore.QRect(140, 40, 311, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_1_3.setFont(font)
        self.label_1_3.setStyleSheet("QLabel\n"
"{\n"
"background:transparent;\n"
"color:rgb(0, 0, 0);\n"
"}")
        self.label_1_3.setObjectName("label_1_3")
        self.label_1_6 = QtWidgets.QLabel(GUI_1)
        self.label_1_6.setGeometry(QtCore.QRect(180, 0, 131, 51))
        font = QtGui.QFont()
        font.setFamily("Kristen ITC")
        font.setPointSize(26)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_1_6.setFont(font)
        self.label_1_6.setStyleSheet("QLabel\n"
"{\n"
"background:transparent;\n"
"color:rgb(170, 0, 0);\n"
"}")
        self.label_1_6.setObjectName("label_1_6")
        self.frame_1_1.raise_()
        self.pushButton_1_2.raise_()
        self.toolButton_1_1.raise_()
        self.label_1_3.raise_()
        self.label_1_6.raise_()
        self.label_1_1.raise_()

        self.retranslateUi(GUI_1)
        QtCore.QMetaObject.connectSlotsByName(GUI_1)

    def retranslateUi(self, GUI_1):
        _translate = QtCore.QCoreApplication.translate
        GUI_1.setWindowTitle(_translate("GUI_1", "GUI_1"))
        self.label_1_1.setText(_translate("GUI_1", "Created"))
        self.groupBox_1_1.setTitle(_translate("GUI_1", "File Exstention"))
        self.label_1_4.setText(_translate("GUI_1", "Setting Up"))
        self.label_1_7.setText(_translate("GUI_1", "Proses Klik"))
        self.label_1_2.setText(_translate("GUI_1", "Login"))
        self.label_1_3.setText(_translate("GUI_1", "Disusun Oleh : Ludi Juliansyah (G1D015036)"))
        self.label_1_6.setText(_translate("GUI_1", "Skripsi "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    GUI_1 = QtWidgets.QWidget()
    ui = Ui_GUI_1()
    ui.setupUi(GUI_1)
    GUI_1.show()
    sys.exit(app.exec_())

