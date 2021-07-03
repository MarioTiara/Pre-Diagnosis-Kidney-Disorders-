
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_GUI_3(object):
    def setupUi(self, GUI_3):
        GUI_3.setObjectName("GUI_3")
        GUI_3.resize(1024, 768)
        GUI_3.setAutoFillBackground(False)
        GUI_3.setStyleSheet("#GUI_3\n"
"{\n"
"    background:rgb(255, 255, 255);\n"
"}")
        self.pushButton_3_1 = QtWidgets.QPushButton(GUI_3)
        self.pushButton_3_1.setGeometry(QtCore.QRect(470, 560, 541, 41))
        self.pushButton_3_1.setStyleSheet("QPushButton\n"
"{\n"
"background:rgb(0, 0, 0);\n"
"border-radius:10px;\n"
"}")
        self.pushButton_3_1.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/icon/screen-1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3_1.setIcon(icon)
        self.pushButton_3_1.setIconSize(QtCore.QSize(15, 30))
        self.pushButton_3_1.setObjectName("pushButton_3_1")
        self.pushButton_3_2 = QtWidgets.QPushButton(GUI_3)
        self.pushButton_3_2.setGeometry(QtCore.QRect(470, 620, 541, 61))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3_2.setFont(font)
        self.pushButton_3_2.setStyleSheet("QPushButton\n"
"{\n"
"background:rgb(0, 0, 0);\n"
"border-radius:10px;\n"
"color:rgb(255, 255, 255);\n"
"}")
        self.pushButton_3_2.setObjectName("pushButton_3_2")
        self.frame_3_1 = QtWidgets.QFrame(GUI_3)
        self.frame_3_1.setGeometry(QtCore.QRect(470, 10, 541, 441))
        self.frame_3_1.setStyleSheet("QFrame\n"
"{\n"
"background:rgba(0, 0, 0, 0.7);\n"
"border-radius:10px;\n"
"}")
        self.frame_3_1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3_1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3_1.setObjectName("frame_3_1")
        self.label_3_1 = QtWidgets.QLabel(self.frame_3_1)
        self.label_3_1.setGeometry(QtCore.QRect(10, 30, 521, 401))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_3_1.setFont(font)
        self.label_3_1.setStyleSheet("QLabel\n"
"{\n"
"\n"
"border-radius:10px;\n"
"}")
        self.label_3_1.setText("")
        self.label_3_1.setObjectName("label_3_1")
        self.label_3_5 = QtWidgets.QLabel(self.frame_3_1)
        self.label_3_5.setGeometry(QtCore.QRect(230, 0, 151, 21))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Heavy")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_3_5.setFont(font)
        self.label_3_5.setStyleSheet("QLabel\n"
"{\n"
"background:rgba(0, 0, 0, 0.0);\n"
"border-radius:10px;\n"
"color:rgb(255, 255, 255);\n"
"}")
        self.label_3_5.setObjectName("label_3_5")
        self.frame_3_2 = QtWidgets.QFrame(GUI_3)
        self.frame_3_2.setGeometry(QtCore.QRect(470, 480, 541, 61))
        self.frame_3_2.setStyleSheet("QFrame\n"
"{\n"
"background:rgb(167, 27, 3);\n"
"border-radius:10px;\n"
"}\n"
"")
        self.frame_3_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3_2.setObjectName("frame_3_2")
        self.label_3_2 = QtWidgets.QLabel(self.frame_3_2)
        self.label_3_2.setGeometry(QtCore.QRect(0, 0, 541, 61))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Heavy")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_3_2.setFont(font)
        self.label_3_2.setStyleSheet("QLabel\n"
"{\n"
"background:rgba(0, 0, 0, 0.7);\n"
"border-radius:10px;\n"
"color:rgb(255, 255, 255);\n"
"}")
        self.label_3_2.setObjectName("label_3_2")
        self.pushButton_3_4 = QtWidgets.QPushButton(GUI_3)
        self.pushButton_3_4.setGeometry(QtCore.QRect(20, 630, 421, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3_4.setFont(font)
        self.pushButton_3_4.setStyleSheet("QPushButton\n"
"{\n"
"background:rgb(0, 0, 0);\n"
"border-radius:10px;\n"
"color:rgb(255, 255, 255);\n"
"}")
        self.pushButton_3_4.setObjectName("pushButton_3_4")
        self.frame_3_3 = QtWidgets.QFrame(GUI_3)
        self.frame_3_3.setGeometry(QtCore.QRect(10, 10, 431, 441))
        self.frame_3_3.setStyleSheet("QFrame\n"
"{\n"
"background:rgba(0, 0, 0, 0.7);\n"
"border-radius:10px;\n"
"}")
        self.frame_3_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3_3.setObjectName("frame_3_3")
        self.label_3_3 = QtWidgets.QLabel(self.frame_3_3)
        self.label_3_3.setGeometry(QtCore.QRect(10, 30, 411, 401))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_3_3.setFont(font)
        self.label_3_3.setStyleSheet("QLabel\n"
"{\n"
"background:rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"}")
        self.label_3_3.setText("")
        self.label_3_3.setObjectName("label_3_3")
        self.label_3_6 = QtWidgets.QLabel(self.frame_3_3)
        self.label_3_6.setGeometry(QtCore.QRect(150, 0, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Heavy")
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.label_3_6.setFont(font)
        self.label_3_6.setStyleSheet("QLabel\n"
"{\n"
"background:rgba(0, 0, 0, 0.0);\n"
"border-radius:10px;\n"
"color:rgb(255, 255, 255);\n"
"}")
        self.label_3_6.setObjectName("label_3_6")
        self.horizontalSlider_3_1 = QtWidgets.QSlider(self.frame_3_3)
        self.horizontalSlider_3_1.setGeometry(QtCore.QRect(90, 380, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(6)
        self.horizontalSlider_3_1.setFont(font)
        self.horizontalSlider_3_1.setMinimum(0)
        self.horizontalSlider_3_1.setMaximum(160)
        self.horizontalSlider_3_1.setPageStep(1)
        self.horizontalSlider_3_1.setProperty("value", 80)
        self.horizontalSlider_3_1.setSliderPosition(80)
        self.horizontalSlider_3_1.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_3_1.setInvertedAppearance(False)
        self.horizontalSlider_3_1.setObjectName("horizontalSlider_3_1")
        self.verticalSlider_3_1 = QtWidgets.QSlider(self.frame_3_3)
        self.verticalSlider_3_1.setGeometry(QtCore.QRect(20, 80, 31, 251))
        self.verticalSlider_3_1.setMinimum(0)
        self.verticalSlider_3_1.setMaximum(160)
        self.verticalSlider_3_1.setPageStep(1)
        self.verticalSlider_3_1.setProperty("value", 80)
        self.verticalSlider_3_1.setSliderPosition(80)
        self.verticalSlider_3_1.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_3_1.setInvertedAppearance(True)
        self.verticalSlider_3_1.setInvertedControls(False)
        self.verticalSlider_3_1.setObjectName("verticalSlider_3_1")
        self.label_3_7 = QtWidgets.QLabel(self.frame_3_3)
        self.label_3_7.setGeometry(QtCore.QRect(200, 350, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Heavy")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_3_7.setFont(font)
        self.label_3_7.setStyleSheet("QLabel\n"
"{\n"
"background:rgba(0, 0, 0, 0.0);\n"
"border-radius:10px;\n"
"color:rgb(0, 0, 0);\n"
"}")
        self.label_3_7.setObjectName("label_3_7")
        self.label_3_8 = QtWidgets.QLabel(self.frame_3_3)
        self.label_3_8.setGeometry(QtCore.QRect(70, 200, 51, 21))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Heavy")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_3_8.setFont(font)
        self.label_3_8.setStyleSheet("QLabel\n"
"{\n"
"background:rgba(0, 0, 0, 0.0);\n"
"border-radius:10px;\n"
"color:rgb(0, 0, 0);\n"
"}")
        self.label_3_8.setObjectName("label_3_8")
        self.frame_3_4 = QtWidgets.QFrame(GUI_3)
        self.frame_3_4.setGeometry(QtCore.QRect(20, 480, 421, 61))
        self.frame_3_4.setStyleSheet("QFrame\n"
"{\n"
"background:rgb(167, 27, 3);\n"
"border-radius:10px;\n"
"}\n"
"")
        self.frame_3_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3_4.setObjectName("frame_3_4")
        self.label_3_4 = QtWidgets.QLabel(self.frame_3_4)
        self.label_3_4.setGeometry(QtCore.QRect(0, 0, 421, 61))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Heavy")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_3_4.setFont(font)
        self.label_3_4.setStyleSheet("QLabel\n"
"{\n"
"background:rgba(0, 0, 0, 0.7);\n"
"border-radius:10px;\n"
"color:rgb(255, 255, 255);\n"
"}")
        self.label_3_4.setObjectName("label_3_4")
        self.horizontalSlider_3_2 = QtWidgets.QSlider(GUI_3)
        self.horizontalSlider_3_2.setGeometry(QtCore.QRect(70, 580, 331, 31))
        self.horizontalSlider_3_2.setStyleSheet("QSlider\n"
"{\n"
"color: rgb(0, 0, 0);\n"
"}")
        self.horizontalSlider_3_2.setMinimum(0)
        self.horizontalSlider_3_2.setMaximum(60)
        self.horizontalSlider_3_2.setPageStep(1)
        self.horizontalSlider_3_2.setProperty("value", 30)
        self.horizontalSlider_3_2.setSliderPosition(30)
        self.horizontalSlider_3_2.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_3_2.setInvertedAppearance(False)
        self.horizontalSlider_3_2.setObjectName("horizontalSlider_3_2")
        self.label_3_9 = QtWidgets.QLabel(GUI_3)
        self.label_3_9.setGeometry(QtCore.QRect(210, 550, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Heavy")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_3_9.setFont(font)
        self.label_3_9.setStyleSheet("QLabel\n"
"{\n"
"background:rgba(0, 0, 0, 0.0);\n"
"border-radius:10px;\n"
"color:rgb(0, 0, 0);\n"
"}")
        self.label_3_9.setObjectName("label_3_9")
        self.label_3_10 = QtWidgets.QLabel(GUI_3)
        self.label_3_10.setGeometry(QtCore.QRect(50, 580, 21, 21))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Heavy")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.label_3_10.setFont(font)
        self.label_3_10.setStyleSheet("QLabel\n"
"{\n"
"background:rgba(0, 0, 0, 0.0);\n"
"border-radius:10px;\n"
"color:rgb(0, 0, 0);\n"
"}")
        self.label_3_10.setObjectName("label_3_10")
        self.label_3_11 = QtWidgets.QLabel(GUI_3)
        self.label_3_11.setGeometry(QtCore.QRect(410, 580, 31, 21))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Heavy")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.label_3_11.setFont(font)
        self.label_3_11.setStyleSheet("QLabel\n"
"{\n"
"background:rgba(0, 0, 0, 0.0);\n"
"border-radius:10px;\n"
"color:rgb(0, 0, 0);\n"
"}")
        self.label_3_11.setObjectName("label_3_11")

        self.retranslateUi(GUI_3)
        QtCore.QMetaObject.connectSlotsByName(GUI_3)

    def retranslateUi(self, GUI_3):
        _translate = QtCore.QCoreApplication.translate
        GUI_3.setWindowTitle(_translate("GUI_3", "GUI_3"))
        self.pushButton_3_2.setText(_translate("GUI_3", "Deteksi Kembali"))
        self.label_3_5.setText(_translate("GUI_3", "Segmentasi Iris"))
        self.label_3_2.setText(_translate("GUI_3", "HASIL"))
        self.pushButton_3_4.setText(_translate("GUI_3", "Ukuran Pupil"))
        self.label_3_6.setText(_translate("GUI_3", "Ukuran Pupil"))
        self.label_3_7.setText(_translate("GUI_3", "Posis X"))
        self.label_3_8.setText(_translate("GUI_3", "Posis Y"))
        self.label_3_4.setText(_translate("GUI_3", "HASIL"))
        self.label_3_9.setText(_translate("GUI_3", "Perbesar"))
        self.label_3_10.setText(_translate("GUI_3", "-"))
        self.label_3_11.setText(_translate("GUI_3", "+"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    GUI_3 = QtWidgets.QWidget()
    ui = Ui_GUI_3()
    ui.setupUi(GUI_3)
    GUI_3.show()
    sys.exit(app.exec_())
