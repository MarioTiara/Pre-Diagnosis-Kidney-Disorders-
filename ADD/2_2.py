# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '2_2.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_GUI_2(object):
    def setupUi(self, GUI_2):
        GUI_2.setObjectName("GUI_2")
        GUI_2.resize(1024, 768)
        GUI_2.setAutoFillBackground(False)
        GUI_2.setStyleSheet("#GUI_2\n"
"{\n"
"    background:#FFFFFF;\n"
"}")
        self.frame = QtWidgets.QFrame(GUI_2)
        self.frame.setGeometry(QtCore.QRect(0, 0, 161, 771))
        self.frame.setStyleSheet("QFrame\n"
"{\n"
"    background:#0A414A;\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.pushButton_2_1 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2_1.setGeometry(QtCore.QRect(30, 90, 71, 61))
        self.pushButton_2_1.setStyleSheet("QPushButton\n"
"{\n"
"background:rgb(255, 255, 255);\n"
"border-radius:20px;\n"
"}")
        self.pushButton_2_1.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/icon/clock-1 - Copy.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2_1.setIcon(icon)
        self.pushButton_2_1.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_2_1.setObjectName("pushButton_2_1")
        self.pushButton_2_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2_2.setGeometry(QtCore.QRect(30, 580, 71, 61))
        self.pushButton_2_2.setStyleSheet("QPushButton\n"
"{\n"
"background:rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"}")
        self.pushButton_2_2.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images/icon/notes.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2_2.setIcon(icon1)
        self.pushButton_2_2.setIconSize(QtCore.QSize(16, 30))
        self.pushButton_2_2.setObjectName("pushButton_2_2")
        self.label_2_1 = QtWidgets.QLabel(self.frame)
        self.label_2_1.setGeometry(QtCore.QRect(20, 160, 81, 16))
        font = QtGui.QFont()
        font.setFamily("Geometr706 BlkCn BT")
        font.setPointSize(8)
        self.label_2_1.setFont(font)
        self.label_2_1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_2_1.setStyleSheet("QLabel\n"
"{\n"
"color:rgb(255, 255, 255);\n"
"}")
        self.label_2_1.setObjectName("label_2_1")
        self.label_2_16 = QtWidgets.QLabel(self.frame)
        self.label_2_16.setGeometry(QtCore.QRect(40, 650, 61, 20))
        font = QtGui.QFont()
        font.setFamily("GeoSlab703 MdCn BT")
        font.setPointSize(12)
        self.label_2_16.setFont(font)
        self.label_2_16.setStyleSheet("QLabel\n"
"{\n"
"color:rgb(255, 255, 255);\n"
"}")
        self.label_2_16.setObjectName("label_2_16")
        self.frame_2 = QtWidgets.QFrame(GUI_2)
        self.frame_2.setGeometry(QtCore.QRect(860, 0, 161, 771))
        self.frame_2.setStyleSheet("QFrame\n"
"{\n"
"    background:#0A414A;\n"
"}")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.pushButton_2_5 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_2_5.setGeometry(QtCore.QRect(40, 80, 61, 51))
        self.pushButton_2_5.setStyleSheet("QPushButton\n"
"{\n"
"background:rgb(255, 255, 255);\n"
"border-radius:20px;\n"
"}")
        self.pushButton_2_5.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("images/icon/cursor.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2_5.setIcon(icon2)
        self.pushButton_2_5.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_2_5.setObjectName("pushButton_2_5")
        self.groupBox_2 = QtWidgets.QGroupBox(self.frame_2)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 460, 111, 81))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(12)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setStyleSheet("QGroupBox\n"
"{\n"
"color:rgb(255, 255, 255);\n"
"}")
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_2_5 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2_5.setGeometry(QtCore.QRect(10, 30, 31, 16))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(8)
        self.label_2_5.setFont(font)
        self.label_2_5.setStyleSheet("QLabel\n"
"{\n"
"color:rgb(255, 255, 255);\n"
"}")
        self.label_2_5.setObjectName("label_2_5")
        self.label_2_6 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2_6.setGeometry(QtCore.QRect(70, 30, 31, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(8)
        self.label_2_6.setFont(font)
        self.label_2_6.setStyleSheet("QLabel\n"
"{\n"
"color:rgb(255, 255, 255);\n"
"}")
        self.label_2_6.setObjectName("label_2_6")
        self.groupBox_3 = QtWidgets.QGroupBox(self.frame_2)
        self.groupBox_3.setGeometry(QtCore.QRect(20, 180, 112, 111))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(12)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setStyleSheet("QGroupBox\n"
"{\n"
"color:rgb(255, 255, 255);\n"
"}\n"
"")
        self.groupBox_3.setObjectName("groupBox_3")
        self.label_2_9 = QtWidgets.QLabel(self.groupBox_3)
        self.label_2_9.setGeometry(QtCore.QRect(10, 30, 21, 16))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(8)
        self.label_2_9.setFont(font)
        self.label_2_9.setStyleSheet("QLabel\n"
"{\n"
"color:rgb(255, 255, 255);\n"
"}")
        self.label_2_9.setObjectName("label_2_9")
        self.label_2_8 = QtWidgets.QLabel(self.groupBox_3)
        self.label_2_8.setGeometry(QtCore.QRect(10, 50, 21, 16))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(8)
        self.label_2_8.setFont(font)
        self.label_2_8.setStyleSheet("QLabel\n"
"{\n"
"color:rgb(255, 255, 255);\n"
"}")
        self.label_2_8.setObjectName("label_2_8")
        self.label_2_7 = QtWidgets.QLabel(self.groupBox_3)
        self.label_2_7.setGeometry(QtCore.QRect(10, 70, 21, 16))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(8)
        self.label_2_7.setFont(font)
        self.label_2_7.setStyleSheet("QLabel\n"
"{\n"
"color:rgb(255, 255, 255);\n"
"}")
        self.label_2_7.setObjectName("label_2_7")
        self.groupBox_4 = QtWidgets.QGroupBox(self.frame_2)
        self.groupBox_4.setGeometry(QtCore.QRect(20, 330, 112, 81))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(12)
        self.groupBox_4.setFont(font)
        self.groupBox_4.setStyleSheet("QGroupBox\n"
"{\n"
"color:rgb(255, 255, 255);\n"
"}")
        self.groupBox_4.setObjectName("groupBox_4")
        self.label_2_10 = QtWidgets.QLabel(self.groupBox_4)
        self.label_2_10.setGeometry(QtCore.QRect(10, 30, 31, 16))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(8)
        self.label_2_10.setFont(font)
        self.label_2_10.setStyleSheet("QLabel\n"
"{\n"
"color:rgb(255, 255, 255);\n"
"}")
        self.label_2_10.setObjectName("label_2_10")
        self.label_2_11 = QtWidgets.QLabel(self.groupBox_4)
        self.label_2_11.setGeometry(QtCore.QRect(70, 30, 31, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(8)
        self.label_2_11.setFont(font)
        self.label_2_11.setStyleSheet("QLabel\n"
"{\n"
"color:rgb(255, 255, 255);\n"
"}")
        self.label_2_11.setObjectName("label_2_11")
        self.groupBox = QtWidgets.QGroupBox(self.frame_2)
        self.groupBox.setGeometry(QtCore.QRect(20, 580, 112, 81))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(12)
        self.groupBox.setFont(font)
        self.groupBox.setStyleSheet("QGroupBox\n"
"{\n"
"color:rgb(255, 255, 255);\n"
"}")
        self.groupBox.setObjectName("groupBox")
        self.label_2_12 = QtWidgets.QLabel(self.groupBox)
        self.label_2_12.setGeometry(QtCore.QRect(10, 30, 31, 16))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(8)
        self.label_2_12.setFont(font)
        self.label_2_12.setStyleSheet("QLabel\n"
"{\n"
"color:rgb(255, 255, 255);\n"
"}")
        self.label_2_12.setObjectName("label_2_12")
        self.label_2_13 = QtWidgets.QLabel(self.groupBox)
        self.label_2_13.setGeometry(QtCore.QRect(80, 30, 31, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(8)
        self.label_2_13.setFont(font)
        self.label_2_13.setStyleSheet("QLabel\n"
"{\n"
"color:rgb(255, 255, 255);\n"
"}")
        self.label_2_13.setObjectName("label_2_13")
        self.label_2_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2_2.setGeometry(QtCore.QRect(50, 140, 51, 20))
        font = QtGui.QFont()
        font.setFamily("Geometr706 BlkCn BT")
        font.setPointSize(10)
        self.label_2_2.setFont(font)
        self.label_2_2.setStyleSheet("QLabel\n"
"{\n"
"color:rgb(255, 255, 255);\n"
"}")
        self.label_2_2.setObjectName("label_2_2")
        self.comboBox_2_1 = QtWidgets.QComboBox(GUI_2)
        self.comboBox_2_1.setGeometry(QtCore.QRect(360, 40, 311, 21))
        self.comboBox_2_1.setStyleSheet("QComboBox\n"
"{\n"
"background:rgb(163, 163, 122);\n"
"color:rgb(0, 0, 0);\n"
"\n"
"}")
        self.comboBox_2_1.setObjectName("comboBox_2_1")
        self.label_2_3 = QtWidgets.QLabel(GUI_2)
        self.label_2_3.setGeometry(QtCore.QRect(460, 10, 81, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2_3.setFont(font)
        self.label_2_3.setObjectName("label_2_3")
        self.horizontalSlider_2_1 = QtWidgets.QSlider(GUI_2)
        self.horizontalSlider_2_1.setGeometry(QtCore.QRect(170, 629, 221, 31))
        self.horizontalSlider_2_1.setStyleSheet("QSlider\n"
"{\n"
"color: rgb(0, 0, 0);\n"
"}")
        self.horizontalSlider_2_1.setMinimum(30)
        self.horizontalSlider_2_1.setMaximum(300)
        self.horizontalSlider_2_1.setPageStep(1)
        self.horizontalSlider_2_1.setProperty("value", 80)
        self.horizontalSlider_2_1.setSliderPosition(80)
        self.horizontalSlider_2_1.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_2_1.setInvertedAppearance(False)
        self.horizontalSlider_2_1.setObjectName("horizontalSlider_2_1")
        self.horizontalSlider_2_2 = QtWidgets.QSlider(GUI_2)
        self.horizontalSlider_2_2.setGeometry(QtCore.QRect(590, 630, 221, 31))
        self.horizontalSlider_2_2.setMinimum(150)
        self.horizontalSlider_2_2.setMaximum(550)
        self.horizontalSlider_2_2.setPageStep(1)
        self.horizontalSlider_2_2.setProperty("value", 370)
        self.horizontalSlider_2_2.setSliderPosition(370)
        self.horizontalSlider_2_2.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_2_2.setInvertedAppearance(True)
        self.horizontalSlider_2_2.setObjectName("horizontalSlider_2_2")
        self.verticalSlider_2_1 = QtWidgets.QSlider(GUI_2)
        self.verticalSlider_2_1.setGeometry(QtCore.QRect(810, 380, 31, 221))
        self.verticalSlider_2_1.setMinimum(10)
        self.verticalSlider_2_1.setMaximum(310)
        self.verticalSlider_2_1.setPageStep(1)
        self.verticalSlider_2_1.setSliderPosition(160)
        self.verticalSlider_2_1.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_2_1.setInvertedAppearance(False)
        self.verticalSlider_2_1.setInvertedControls(False)
        self.verticalSlider_2_1.setObjectName("verticalSlider_2_1")
        self.label_2_19 = QtWidgets.QLabel(GUI_2)
        self.label_2_19.setGeometry(QtCore.QRect(180, 670, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2_19.setFont(font)
        self.label_2_19.setStyleSheet("QLabel\n"
"{\n"
"color: rgb(0, 0, 0);\n"
"}")
        self.label_2_19.setObjectName("label_2_19")
        self.label_2_20 = QtWidgets.QLabel(GUI_2)
        self.label_2_20.setGeometry(QtCore.QRect(660, 670, 71, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2_20.setFont(font)
        self.label_2_20.setStyleSheet("QLabel\n"
"{\n"
"color: rgb(0, 0, 0);\n"
"}")
        self.label_2_20.setObjectName("label_2_20")
        self.label_2_21 = QtWidgets.QLabel(GUI_2)
        self.label_2_21.setGeometry(QtCore.QRect(800, 340, 81, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2_21.setFont(font)
        self.label_2_21.setStyleSheet("QLabel\n"
"{\n"
"color: rgb(0, 0, 0);\n"
"}")
        self.label_2_21.setObjectName("label_2_21")
        self.label_2_14 = QtWidgets.QLabel(GUI_2)
        self.label_2_14.setGeometry(QtCore.QRect(90, 20, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.label_2_14.setFont(font)
        self.label_2_14.setStyleSheet("QLabel\n"
"{\n"
"background: rgb(166, 21, 11);\n"
"border-radius:10px;\n"
"}")
        self.label_2_14.setText("")
        self.label_2_14.setObjectName("label_2_14")
        self.radioButton_2_1 = QtWidgets.QRadioButton(GUI_2)
        self.radioButton_2_1.setGeometry(QtCore.QRect(110, 30, 141, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_2_1.setFont(font)
        self.radioButton_2_1.setStyleSheet("QRadioButton\n"
"{\n"
"color:rgb(255, 255, 255);\n"
"}")
        self.radioButton_2_1.setCheckable(True)
        self.radioButton_2_1.setChecked(True)
        self.radioButton_2_1.setObjectName("radioButton_2_1")
        self.label_2_15 = QtWidgets.QLabel(GUI_2)
        self.label_2_15.setGeometry(QtCore.QRect(740, 10, 191, 41))
        self.label_2_15.setStyleSheet("QLabel\n"
"{\n"
"background: rgb(166, 21, 11);\n"
"border-radius:10px;\n"
"}")
        self.label_2_15.setText("")
        self.label_2_15.setObjectName("label_2_15")
        self.radioButton_2_2 = QtWidgets.QRadioButton(GUI_2)
        self.radioButton_2_2.setGeometry(QtCore.QRect(760, 20, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_2_2.setFont(font)
        self.radioButton_2_2.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.radioButton_2_2.setStyleSheet("QRadioButton\n"
"{\n"
"color:rgb(255, 255, 255);\n"
"}")
        self.radioButton_2_2.setCheckable(True)
        self.radioButton_2_2.setChecked(False)
        self.radioButton_2_2.setAutoRepeat(False)
        self.radioButton_2_2.setObjectName("radioButton_2_2")
        self.label_2_4 = QtWidgets.QLabel(GUI_2)
        self.label_2_4.setGeometry(QtCore.QRect(190, 100, 600, 481))
        self.label_2_4.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2_4.setFont(font)
        self.label_2_4.setFrameShape(QtWidgets.QFrame.Box)
        self.label_2_4.setText("")
        self.label_2_4.setObjectName("label_2_4")
        self.frame.raise_()
        self.frame_2.raise_()
        self.horizontalSlider_2_1.raise_()
        self.horizontalSlider_2_2.raise_()
        self.verticalSlider_2_1.raise_()
        self.label_2_3.raise_()
        self.comboBox_2_1.raise_()
        self.label_2_19.raise_()
        self.label_2_20.raise_()
        self.label_2_21.raise_()
        self.label_2_14.raise_()
        self.radioButton_2_1.raise_()
        self.label_2_15.raise_()
        self.radioButton_2_2.raise_()
        self.label_2_4.raise_()

        self.retranslateUi(GUI_2)
        QtCore.QMetaObject.connectSlotsByName(GUI_2)

    def retranslateUi(self, GUI_2):
        _translate = QtCore.QCoreApplication.translate
        GUI_2.setWindowTitle(_translate("GUI_2", "GUI_2"))
        self.label_2_1.setText(_translate("GUI_2", "Proses Diagnosis"))
        self.label_2_16.setText(_translate("GUI_2", "Buka File"))
        self.groupBox_2.setTitle(_translate("GUI_2", "Channel 3"))
        self.label_2_5.setText(_translate("GUI_2", "B_2"))
        self.label_2_6.setText(_translate("GUI_2", "B_3"))
        self.groupBox_3.setTitle(_translate("GUI_2", "Channel 1"))
        self.label_2_9.setText(_translate("GUI_2", "E"))
        self.label_2_8.setText(_translate("GUI_2", "F"))
        self.label_2_7.setText(_translate("GUI_2", "H"))
        self.groupBox_4.setTitle(_translate("GUI_2", "Channel 2"))
        self.label_2_10.setText(_translate("GUI_2", "B_4"))
        self.label_2_11.setText(_translate("GUI_2", "B_5"))
        self.groupBox.setTitle(_translate("GUI_2", "Channel 4"))
        self.label_2_12.setText(_translate("GUI_2", "B_6"))
        self.label_2_13.setText(_translate("GUI_2", "B_7"))
        self.label_2_2.setText(_translate("GUI_2", "Kamera"))
        self.label_2_3.setText(_translate("GUI_2", "Gangguan"))
        self.label_2_19.setText(_translate("GUI_2", "Perbesar"))
        self.label_2_20.setText(_translate("GUI_2", "Posis X"))
        self.label_2_21.setText(_translate("GUI_2", "Posisi y"))
        self.radioButton_2_1.setText(_translate("GUI_2", "Mata Kanan"))
        self.radioButton_2_2.setText(_translate("GUI_2", "Mata Kiri"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    GUI_2 = QtWidgets.QWidget()
    ui = Ui_GUI_2()
    ui.setupUi(GUI_2)
    GUI_2.show()
    sys.exit(app.exec_())
