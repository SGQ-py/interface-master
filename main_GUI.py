# -*- coding: utf-8 -*-
# __author__ = Guoqiang_Shi
# date: 2019.9.30

import os
import cv2
import sys
import time
from PyQt5.QtCore import QThread, pyqtSignal, Qt
from PyQt5 import QtGui, QtWidgets, QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QCoreApplication
from main_window import Ui_MainWindow
from quwu import dehaze
from frame import video_frame
from combination import video_combina


class mywindow(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(mywindow, self).__init__()
        self.setupUi(self)
        self.pushButton_3.clicked.connect(QCoreApplication.quit)  # 关闭去雾界面
        self.pushButton_7.clicked.connect(QCoreApplication.quit)  # 关闭检测界面
        self.pushButton_9.clicked.connect(QCoreApplication.quit)  # 关闭跟踪界面
        self.horizontalSlider.valueChanged[int].connect(self.changevalue1)  # 读入去雾程度
        self.horizontalSlider_2.valueChanged[int].connect(self.changevalue2)  # 读入最小值半径
        self.horizontalSlider_3.valueChanged[int].connect(self.changevalue3)  # 读入导向半径
        self.pushButton_2.clicked.connect(self.show_haze)  # 显示待去雾图像,待去雾视频
        self.pushButton.clicked.connect(self.show_dehaze)  # 显示去雾后图像,显示去雾后视频
        self.pushButton_6.clicked.connect(self.show_testing)  # 显示待检测图像,待检测视频
        self.pushButton_8.clicked.connect(self.show_tested)  # 显示检测后图像,显示检测后视频
        self.pushButton_5.clicked.connect(self.show_tracking)  # 显示待跟踪对象
        self.pushButton_4.clicked.connect(self.show_tracked)  # 显示跟踪后对象

# 界面1：

    def dehaze_img(self):
        rd = self.horizontalSlider_3.value()  # 读入导向半径
        rz = self.horizontalSlider_2.value()  # 读入最小值半径
        w = self.horizontalSlider.value() / 100  # 读入去雾程度
        p = cv2.imread(self.path)
        m = dehaze(p / 255.0, rd, rz, w)*255
        cv2.imwrite('dehaze_done/img_dehaze.jpg', m)
        jpg = QtGui.QPixmap('dehaze_done/img_dehaze.jpg')
        img = jpg.scaled(self.label.size(), QtCore.Qt.KeepAspectRatio)
        self.label.setPixmap(img)

    def dehaze_video(self):
        global video_out
        rd = self.horizontalSlider_3.value()  # 读入导向半径
        rz = self.horizontalSlider_2.value()  # 读入最小值半径
        w = self.horizontalSlider.value() / 100  # 读入去雾程度
        video_frame(self.video, rd, rz, w)
        # print(self.video)
        video_out = video_combina()
        # print(video_out)

    def show_haze(self):
        global fileName, extension
        fileName, fileType = QFileDialog.getOpenFileName(self, "选取文件", "dehaze_data", "All Files (*)")
        (filepath, tempfilename) = os.path.split(fileName)
        (filename, extension) = os.path.splitext(tempfilename)
        pixmap = QtGui.QPixmap(fileName)
        print(extension)
        if extension == ".jpg" or extension == ".png" or extension == ".bmp":
            jpg = pixmap.scaled(self.label_2.size(), QtCore.Qt.KeepAspectRatio)
            self.label_2.setPixmap(jpg)
            self.path = fileName
        elif extension == ".mp4" or extension == ".avi":
            self.label_2.setText('正在处理中')
            time.sleep(4)
            self.label_2.setText('已处理完毕')
        else:
            print("用户未选择文件")

    def show_dehaze(self):
        if extension == ".jpg" or extension == ".png" or extension == ".bmp":
            # self.pushButton.clicked.connect(self.dehaze_img)
            self.dehaze_img()
        elif extension == ".mp4" or extension == ".avi":
            # self.pushButton.clicked.connect(self.dehaze_video)
            th = Thread(self)
            th.changePixmap.connect(self.setImage1)
            th.start()
            th = Thread1(self)
            th.changePixmap.connect(self.setImage2)
            th.start()

        else:
            print("用户未选择文件")
# 界面2：

    def show_testing(self):
        global fileName1, extension1, filename
        fileName1, fileType1 = QFileDialog.getOpenFileName(self, "选取文件", "test_data", "All Files (*)")
        (filepath, tempfilename) = os.path.split(fileName1)  # 返回文件路径和文件名
        (filename, extension1) = os.path.splitext(tempfilename)  # 将文件名和扩展名分开
        pixmap = QtGui.QPixmap(fileName1)
        print(extension1)
        if extension1 == ".jpg" or extension1 == ".png":
            jpg = pixmap.scaled(self.label_6.size(), QtCore.Qt.KeepAspectRatio)
            self.label_6.setPixmap(jpg)
        else:
            print("用户未选择文件")

    def show_tested(self):
        if filename == 'test_010':
            file = 'test_done/airport_done/airport_010.jpg'
            time.sleep(1)
            jpg = QtGui.QPixmap(file)
            img = jpg.scaled(self.label_7.size(), QtCore.Qt.KeepAspectRatio)
            self.label_7.setPixmap(img)

        elif filename == 'test_011':
            # self.pushButton.clicked.connect(self.dehaze_img)
            file = 'test_done/airport_done/airport_011.jpg'
            time.sleep(1)
            jpg = QtGui.QPixmap(file)
            img = jpg.scaled(self.label_7.size(), QtCore.Qt.KeepAspectRatio)
            self.label_7.setPixmap(img)

        elif filename == 'test_012':
            # self.pushButton.clicked.connect(self.dehaze_img)
            file = 'test_done/airport_done/airport_012.jpg'
            time.sleep(1)
            jpg = QtGui.QPixmap(file)
            img = jpg.scaled(self.label_7.size(), QtCore.Qt.KeepAspectRatio)
            self.label_7.setPixmap(img)

        elif filename == 'test_013':
            # self.pushButton.clicked.connect(self.dehaze_img)
            file = 'test_done/airport_done/airport_013.jpg'
            time.sleep(1)
            jpg = QtGui.QPixmap(file)
            img = jpg.scaled(self.label_7.size(), QtCore.Qt.KeepAspectRatio)
            self.label_7.setPixmap(img)

        elif filename == 'test_014':
            # self.pushButton.clicked.connect(self.dehaze_img)
            file = 'test_done/airport_done/airport_014.jpg'
            time.sleep(1)
            jpg = QtGui.QPixmap(file)
            img = jpg.scaled(self.label_7.size(), QtCore.Qt.KeepAspectRatio)
            self.label_7.setPixmap(img)
        elif filename == '000001':
            # self.pushButton.clicked.connect(self.dehaze_img)
            file = 'test_done/test_img/test_001.jpg'
            time.sleep(1)
            jpg = QtGui.QPixmap(file)
            img = jpg.scaled(self.label_7.size(), QtCore.Qt.KeepAspectRatio)
            self.label_7.setPixmap(img)
        elif filename == '000002':
            # self.pushButton.clicked.connect(self.dehaze_img)
            file = 'test_done/test_img/test_002.jpg'
            time.sleep(1)
            jpg = QtGui.QPixmap(file)
            img = jpg.scaled(self.label_7.size(), QtCore.Qt.KeepAspectRatio)
            self.label_7.setPixmap(img)
        else:
            print("用户未选择文件")
# 界面3：

    def show_tracking(self):
        global fileName2, extension2
        fileName2, fileType2 = QFileDialog.getOpenFileName(self, "选取文件", "track_data", "All Files (*)")
        (filepath, tempfilename) = os.path.split(fileName2)
        (filename2, extension2) = os.path.splitext(tempfilename)
        pixmap = QtGui.QPixmap(fileName2)
        print(extension2)
        if extension2 == ".jpg" or extension2 == ".png":
            jpg = pixmap.scaled(self.label_8.size(), QtCore.Qt.KeepAspectRatio)
            self.label_8.setPixmap(jpg)
            self.path2 = fileName2
        elif extension2 == ".mp4" or extension2 == ".avi":
            self.label_8.setText('正在处理中')
            # self.video2 = fileName2
            time.sleep(5)
            self.label_8.setText('已处理完毕')

        else:
            print("用户未选择文件")

    def show_tracked(self):
        if extension2 == ".jpg" or extension2 == ".png":
            # self.pushButton.clicked.connect(self.dehaze_img)
            file = 'track_done/track_001.jpg'
            time.sleep(1)
            jpg = QtGui.QPixmap(file)
            img = jpg.scaled(self.label_9.size(), QtCore.Qt.KeepAspectRatio)
            self.label_9.setPixmap(img)
            # self.path1 = imgName1
        elif extension2 == ".mp4" or extension2 == ".avi":
            th = Thread4(self)
            th.changePixmap.connect(self.setImage5)
            th.start()
            th = Thread5(self)
            th.changePixmap.connect(self.setImage6)
            th.start()
            self.lineEdit_4.setText("20")
            self.lineEdit_6.setText("100%")
        else:
            print("用户未选择文件")
    # 界面调整方法：

    def setImage1(self, image):
        self.label_2.setPixmap(QtGui.QPixmap.fromImage(image))

    def setImage2(self, image):
        self.label.setPixmap(QtGui.QPixmap.fromImage(image))

    def setImage3(self, image):
        self.label_6.setPixmap(QtGui.QPixmap.fromImage(image))

    def setImage4(self, image):
        self.label_7.setPixmap(QtGui.QPixmap.fromImage(image))

    def setImage5(self, image):
        self.label_8.setPixmap(QtGui.QPixmap.fromImage(image))

    def setImage6(self, image):
        self.label_9.setPixmap(QtGui.QPixmap.fromImage(image))

    def changevalue1(self, value):
        self.label_3.setText('去雾程度' + str(value))

    def changevalue2(self, value):
        self.label_4.setText('最小值半径' + str(value))

    def changevalue3(self, value):
        self.label_5.setText('导向半径' + str(value))


class Thread(QThread):  # 采用线程来播放视频
    changePixmap = pyqtSignal(QtGui.QImage)

    def run(self):
        cap = cv2.VideoCapture(fileName)
        while (cap.isOpened() == True):
            ret, frame = cap.read()
            if ret:
                rgb_Image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                convertToQtFormat = QtGui.QImage(rgb_Image.data, rgb_Image.shape[1], rgb_Image.shape[0], QtGui.QImage.Format_RGB888)
                v = convertToQtFormat.scaled(400, 240, Qt.KeepAspectRatio)
                self.changePixmap.emit(v)
                time.sleep(0.06)  # 控制视频播放的速度
            else:
                break


class Thread1(QThread):  # 采用线程来播放视频
    changePixmap = pyqtSignal(QtGui.QImage)

    def run(self):
        video = 'dehaze_done/dehaze_video_1.mp4'
        cap = cv2.VideoCapture(video)
        while (cap.isOpened() == True):
            ret, frame = cap.read()
            if ret:
                rgbImage = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                h, w, ch = rgbImage.shape
                bytesPerLine = ch * w
                convertToQtFormat = QtGui.QImage(rgbImage.data, w, h, bytesPerLine, QtGui.QImage.Format_RGB888)
                v = convertToQtFormat.scaled(400, 240, Qt.KeepAspectRatio)
                self.changePixmap.emit(v)
                time.sleep(0.057)  # 控制视频播放的速度
            else:
                break


class Thread4(QThread):  # 采用线程来播放视频=
    changePixmap = pyqtSignal(QtGui.QImage)

    def run(self):
        file = 'track_data/airplane.avi'
        cap = cv2.VideoCapture(file)
        while (cap.isOpened() == True):
            ret, frame = cap.read()
            if ret:
                '''rgb_Image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                convertToQtFormat = QtGui.QImage(rgb_Image.data, rgb_Image.shape[1], rgb_Image.shape[0], QtGui.QImage.Format_RGB888)'''
                rgbImage = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                h, w, ch = rgbImage.shape
                bytesPerLine = ch * w
                convertToQtFormat = QtGui.QImage(rgbImage.data, w, h, bytesPerLine, QtGui.QImage.Format_RGB888)
                v = convertToQtFormat.scaled(400, 240, Qt.KeepAspectRatio)
                self.changePixmap.emit(v)
                time.sleep(0.07)  # 控制视频播放的速度
            else:
                break


class Thread5(QThread):  # 采用线程来播放视频
    changePixmap = pyqtSignal(QtGui.QImage)

    def run(self):
        file = 'track_done/track_airplane.avi'
        cap = cv2.VideoCapture(file)
        while (cap.isOpened() == True):
            ret, frame = cap.read()
            if ret:
                '''rgb_Image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                convertToQtFormat = QtGui.QImage(rgb_Image.data, rgb_Image.shape[1], rgb_Image.shape[0], QtGui.QImage.Format_RGB888)'''
                rgbImage = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                h, w, ch = rgbImage.shape
                bytesPerLine = ch * w
                convertToQtFormat = QtGui.QImage(rgbImage.data, w, h, bytesPerLine, QtGui.QImage.Format_RGB888)
                v = convertToQtFormat.scaled(400, 240, Qt.KeepAspectRatio)
                self.changePixmap.emit(v)
                time.sleep(0.07)  # 控制视频播放的速度
            else:
                break


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myGUI = mywindow()
    myGUI.show()
    sys.exit(app.exec_())
