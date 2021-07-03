import numpy
import numpy as np
import cv2
import sys
import logo
import os
import time
#import RPi.GPIO as GPIO

from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QMainWindow, QLabel, QSlider, QApplication, QWidget, QPushButton, QFileDialog
from PyQt5.QtCore import QSize, Qt, pyqtSlot, pyqtSignal, QTimer
from PyQt5.QtGui import QImage
from PyQt5.QtGui import QPixmap

from keras.preprocessing.image import ImageDataGenerator, load_img, img_to_array
from keras.models import Sequential, load_model

from GUI1 import *
from GUI2 import *
from GUI3 import *

"""
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)
"""
########################################################################################
#################################   GUI Control   ######################################
########################################################################################

class Controller:
    def __init__(self):
        pass

    '''''''''''''''
     GUI 1 Control
    '''''''''''''''
    def Show_GUI_1(self):
        self.GUI_1 = QtWidgets.QMainWindow()
        self.ui = Ui_GUI_1()
        self.ui.setupUi(self.GUI_1)
        self.GUI_1.show()
        self.ui.comboBox_1_1.currentTextChanged.connect(self.comboChanged_1_1)
        
    '''''''''''''''
     GUI 2 Control
    '''''''''''''''  
    def Show_GUI_2(self):
        self.GUI_2 = QtWidgets.QMainWindow()
        self.ui = Ui_GUI_2()
        self.ui.setupUi(self.GUI_2)
        self.GUI_1.close()
        self.GUI_2.show()

        self.ui.pushButton_2_1.clicked.connect(self.Show_GUI_3)

        self.ui.pushButton_2_2.clicked.connect(self.openImage)

        self.ui.comboBox_2_1.currentTextChanged.connect(self.comboChanged_2_1)

        #//Slider Zoom dan Menggeser menggambar Circle
        self.ui.horizontalSlider_2_1.valueChanged.connect(self.valueUpdating_1)
        self.ui.horizontalSlider_2_2.valueChanged.connect(self.valueUpdating_2)
        self.ui.verticalSlider_2_1.valueChanged.connect(self.valueUpdating_3)

        #//Timer Untuk Kamera
        self.ui.timer = QTimer()
        self.ui.timer.timeout.connect(self.viewCam)
        self.ui.pushButton_2_5.clicked.connect(self.controlTimer)

        #//Fungsi Radio Button (Nilai crop & Lokasi DIR)
        self.ui.radioButton_2_1.toggled.connect(self.dir_crop)
        self.ui.radioButton_2_2.toggled.connect(self.dir_crop)

        #//Nilai Lokasi Iris YY
        location_crop_image_Yawal=76
        location_crop_image_Yakhir=140
        self.ui.label_2_5.setText(str(location_crop_image_Yawal))
        self.ui.label_2_6.setText(str(location_crop_image_Yakhir))

        #//Nilai Lokasi Iris XX
        location_crop_image_Xawal=46
        location_crop_image_Xakhir=110
        self.ui.label_2_10.setText(str(location_crop_image_Xawal))
        self.ui.label_2_11.setText(str(location_crop_image_Xakhir))

        #Lokasi Awal
        DIR_1='Kanan'
        self.ui.label_2_12.setText(DIR_1)
        DIR_2='Ginjal'
        self.ui.label_2_13.setText(DIR_2)
        

    #####Fungsi Slider Nilai to Lable 
    def valueUpdating_1(self):
        SH1 = str(self.ui.horizontalSlider_2_1.value())
        self.ui.label_2_9.setText(SH1)

    def valueUpdating_2(self):
        SH2 = str(self.ui.horizontalSlider_2_2.value())
        self.ui.label_2_8.setText(SH2)

    def valueUpdating_3(self):
        SV1 = str(self.ui.verticalSlider_2_1.value())
        self.ui.label_2_7.setText(SV1)

    #####RB (Nilai crop & Lokasi DIR)
    def dir_crop(self):
        if self.ui.radioButton_2_1.isChecked()==True:
            location_crop_image_Yawal=76
            location_crop_image_Yakhir=140
            DIR_1='Kanan'
            #self.ui.label_2_2.setBackground('Green')
        if self.ui.radioButton_2_2.isChecked()==True:
            location_crop_image_Yawal=86
            location_crop_image_Yakhir=150
            DIR_1='Kiri'
        self.ui.label_2_5.setText(str(location_crop_image_Yawal))
        self.ui.label_2_6.setText(str(location_crop_image_Yakhir))
        #Lokasi DIR Folder Kiri atau Kanan
        self.ui.label_2_12.setText(DIR_1)

    #####Fungsi Kamera
    def viewCam(self):
        ##### read image in BGR format
        ret, image = self.cap.read()

        Z = int(self.ui.horizontalSlider_2_1.value())
        X = int(self.ui.horizontalSlider_2_2.value())
        Y = int(self.ui.verticalSlider_2_1.value())

        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        #####Fungsi Draw Circle
        cv2.circle(image,(X+Z*1, Y+Z*1), Z, (255,0,0), 1)
        
        height, width, channel = image.shape
        step = channel * width
        qImg = QImage(image.data, width, height, step, QImage.Format_RGB888)

        #Rotasi Image
        img = image
        h,w = img.shape[:2]
        center = (w/2,h/2)
        rotate = cv2.getRotationMatrix2D(center,180,1)
        rotatingImg = cv2.warpAffine(img,rotate,(w,h))
        qImg = QImage(rotatingImg.data, width, height, step, QImage.Format_RGB888)

        self.ui.label_2_4.setPixmap(QPixmap.fromImage(qImg))


        #####Fungsi Crop Circle
        img = image
        
        x=X
        y=Y
        r=Z

        img = img[y:y+r*2, x:x+r*2]
        mask = np.full((img.shape[0], img.shape[1]), 1, dtype=np.uint8) 
        cv2.circle(mask,(r,r), r, (255,255,255),-1)
        fg = cv2.bitwise_or(img, img, mask=mask)
        mask = cv2.bitwise_not(mask)
        background = np.full(img.shape, 255, dtype=np.uint8)
        bk = cv2.bitwise_or(background, background, mask=mask)
        final = cv2.bitwise_or(fg, bk)

        #####Menyipan Gambar Final
        cv2.imwrite('./Lokasi_DIR_Frame/final.jpg', final)

        ##### Fungsi TransFormasi Polar to Carensian
        source = final
        img = source.astype(np.float32)
        value = np.sqrt(((img.shape[0]/2.0)**2.0)+((img.shape[1]/2.0)**2.0))
        polar_image = cv2.linearPolar(img,(img.shape[0]/2, img.shape[1]/2), value, cv2.WARP_FILL_OUTLIERS)
        polar_image = polar_image.astype(np.uint8)

        ##### Memotong gambar hasil Tranformasi
        croppedImg = polar_image[0:(Z+70), 0:(Z+30)] # Yawal-Yakhir, Xawal-Xakhir 

        '''
        ##### Canny Adge
        edges = cv2.Canny(croppedImg,150,200) #Nilai minVal dan maxVal yang di ubah (semakin besar nilai semakain diperjelas)
        '''
        
        ##### Grayscale Adge
        edges= cv2.cvtColor(croppedImg, cv2.COLOR_BGR2GRAY)
                
        ##// Pembacaan Lokasi iris yang dipilih YY
        Yawal= int(self.ui.label_2_5.text())
        Yakhir= int(self.ui.label_2_6.text())

        ##// Pembacaan Lokasi iris yang dipilih XX
        Xawal= int(self.ui.label_2_10.text())
        Xakhir= int(self.ui.label_2_11.text())

        ##### Memotong Iris
        croppedIris = edges[Yawal:Yakhir, Xawal:Xakhir] # Yawal-Yakhir, Xawal-Xakhir 
        
        ##### Lokasi DIR Folder Kiri/Kanan
        DIR_1= (self.ui.label_2_12.text())
        DIR_2= (self.ui.label_2_13.text())   

        ##### Logika Penyimpanan Direktori
        if DIR_1 == 'Kiri' and DIR_2 == 'Ginjal':
            ##### Menyimpan sementara image crop
            cv2.imwrite('./CNN/data/data_recognition/Kiri/ginjal/HasilKondisi.jpg', croppedIris)
            cv2.imwrite('./CNN/data/data_recognition/Kiri/ginjalb/Hasil.jpg', edges)
            #DIRRecog 
            file='./CNN/data/data_recognition/Kiri/ginjal'
            file_tulis = open("Lokasi_DIR/recognition.txt", "w")
            file_tulis.write(file)
            #DIROpen
            file_2='./CNN/data/data_recognition/Kiri/ginjal/HasilKondisi.jpg'
            file_tulis_2 = open("Lokasi_DIR/DIROpen.txt", "w")
            file_tulis_2.write(file_2)

            #cv2.imshow('Output', croppedIris)
            
        if DIR_1 == 'Kanan' and DIR_2 == 'Ginjal':
            ##### Menyimpan sementara image crop
            cv2.imwrite('./CNN/data/data_recognition/Kanan/ginjal/HasilKondisi.jpg', croppedIris)
            cv2.imwrite('./CNN/data/data_recognition/Kanan/ginjalb/Hasil.jpg', edges)
            #DIRRecog
            file='./CNN/data/data_recognition/Kanan/ginjal'
            file_tulis = open("Lokasi_DIR/recognition.txt", "w")
            file_tulis.write(file)
            #DIROpen
            file_2='./CNN/data/data_recognition/Kanan/ginjal/HasilKondisi.jpg'
            file_tulis_2 = open("Lokasi_DIR/DIROpen.txt", "w")
            file_tulis_2.write(file_2)

    ######start/stop timer Kamera
    def controlTimer(self):
        if not self.ui.timer.isActive():
            self.cap = cv2.VideoCapture(0)
            self.ui.timer.start(20)
            self.ui.label_2_2.setText("Stop")
            self.ui.pushButton_2_5.setStyleSheet("QPushButton\n"
"{\n"
"background:red;\n"
"border-radius:30px;\n"
"}")
        else:
            self.ui.timer.stop()
            self.cap.release()
            self.ui.label_2_2.setText("Start")
            self.ui.pushButton_2_5.setStyleSheet("QPushButton\n"
"{\n"
"background:green;\n"
"border-radius:30px;\n"
"}")


    #####Fungsi Memilih pada GUI_1
    def comboChanged_1_1(self):
        text_1 = self.ui.comboBox_1_1.currentText()
        if text_1 == 'Login Diagnosis':
            print("Pra Diagnosis")
            self.ui.pushButton_1_7.clicked.connect(self.Show_GUI_2)
        else:
            print("Login Diagnosis")
            self.ui.pushButton_1_7.clicked.connect(self.Show_GUI_2)

    def comboChanged_2_1(self):
        text_2 = self.ui.comboBox_2_1.currentText()
        if text_2 == 'Diagnosis Ginjal':
            print("Ginjal")
            location_crop_image_Xawal=46
            location_crop_image_Xakhir=110
            DIR_2='Ginjal'

        self.ui.label_2_10.setText(str(location_crop_image_Xawal))
        self.ui.label_2_11.setText(str(location_crop_image_Xakhir))
        self.ui.label_2_13.setText(DIR_2)

    ######Fungsi Buka Folder manual
    def openImage(self):
        imagePath, _ = QFileDialog.getOpenFileName()
        pixmap = QPixmap(imagePath)
        self.ui.label_2_4.setPixmap(pixmap)
        self.ui.resize(pixmap.size())
        self.ui.adjustSize()

    
    '''''''''''''''
     GUI 3 Control
    '''''''''''''''
    def Show_GUI_3(self):
        self.GUI_3 = QtWidgets.QMainWindow()
        self.ui = Ui_GUI_3()
        self.ui.setupUi(self.GUI_3)
        self.GUI_2.close()
        self.GUI_3.show()

        
        # PushButton Circle update image
        self.ui.pushButton_3_4.clicked.connect(self.circle)

       
        # PushButton GUI
        self.ui.pushButton_3_1.clicked.connect(self.Show_GUI_1)
        self.ui.pushButton_3_2.clicked.connect(self.Show_GUI_2)
        
        
        #//Slider Menggeser menggambar Circle
        self.ui.horizontalSlider_3_2.valueChanged.connect(self.valueUpdating_3_3)
        self.ui.horizontalSlider_3_1.valueChanged.connect(self.valueUpdating_3_1)
        self.ui.verticalSlider_3_1.valueChanged.connect(self.valueUpdating_3_2)

        #GPIO.output(18,GPIO.LOW)
        #Define Path
        model_path = '/LCD/CNN/models/model.h5'
        model_weights_path = '/LCD/CNN/models/weights.h5'
        file_tulis = open("Lokasi_DIR/recognition.txt", "r")
        test_path =(file_tulis.read())
        print(test_path)

        
        file_tulis_2 = open("Lokasi_DIR/DIROpen.txt", "r")
        #Membuka Image Segmentasi Iris Menggunakan Motode Pertama Buka Frame
        fileName = QPixmap(file_tulis_2.read())
        pixmap = QtGui.QPixmap(fileName) # Setup pixmap with the provided image
        pixmap = pixmap.scaled(self.ui.label_3_1.width(), self.ui.label_3_1.height(), QtCore.Qt.KeepAspectRatio) # Scale pixmap
        self.ui.label_3_1.setPixmap(pixmap) # Set the pixmap onto the label
        self.ui.label_3_1.setAlignment(QtCore.Qt.AlignCenter) # Align the label to center

        model = load_model(model_path)
        print(model.summary)
        model.load_weights(model_weights_path)
        
        img_width, img_height = 150, 150
        
        #prediksi CNN
        def predict(file):
            x = load_img(file, target_size=(img_width,img_height))
            x = img_to_array(x)
            x = np.expand_dims(x, axis=0)
            array = model.predict(x)
            result = array[0]
            print(result)
            answer = np.argmax(result)
            print(answer)
            if answer == 0:
                print("Predicted: gangguan")
                self.ui.label_3_2.setText("Ada Gangguan")
            elif answer == 1:
                print("Predicted: normal")
                self.ui.label_3_2.setText("Normal")
            return answer

        #Walk the directory for every image
        for i, ret in enumerate(os.walk(test_path)):
            for i, filename in enumerate(ret[2]):
                if filename.startswith("."):
                    continue
    
                print(ret[0] + '/' + filename)
                result = predict(ret[0] + '/' + filename)
                print(" ")
                
    def circle(self):
        #Membuka Image Ukuran Pupil  
        Z = int(self.ui.horizontalSlider_3_2.value())
        X = int(self.ui.horizontalSlider_3_1.value())
        Y = int(self.ui.verticalSlider_3_1.value())
        #Menggunakan Frame_model 2
        image = cv2.imread('Lokasi_DIR_Frame/final.jpg')
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        cv2.circle(image,(X, Y), Z, (255,0,0), 2)
        height, width, channel = image.shape
        step = channel * width
        qImg = QImage(image.data, width, height, step, QImage.Format_RGB888)
        self.ui.label_3_3.setPixmap(QPixmap.fromImage(qImg))
        self.ui.label_3_3.setAlignment(QtCore.Qt.AlignCenter)

    
    def valueUpdating_3_3(self):
        update_pupil = int(self.ui.horizontalSlider_3_2.value())
        diameter_pupil = str(update_pupil/10)
        self.ui.label_3_4.setText('Diameter = ' + diameter_pupil +' mm')   

    def valueUpdating_3_1(self):
        SH1 = str(self.ui.horizontalSlider_3_1.value())
        self.ui.label_3_7.setText(SH1)

    def valueUpdating_3_2(self):
        SH2 = str(self.ui.verticalSlider_3_1.value())
        self.ui.label_3_8.setText(SH2)

    
########################################################################################
###################################   Set GUI  #########################################
########################################################################################

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    controller = Controller()
    controller.Show_GUI_1()
    sys.exit(app.exec_())
