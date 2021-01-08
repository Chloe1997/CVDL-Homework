# -*- coding: utf-8 -*-
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from hw1 import Ui_MainWindow
import sys
import os
import chessboard
import AR
import Stereo
import numpy as np
import SIFT_show as sift


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # Label
        self.ui.label.setFont(QtGui.QFont('Arial', 14))
        self.ui.label.setText('1. Calibration')

        self.ui.label_2.setFont(QtGui.QFont('Arial', 8))
        self.ui.label_2.setText('1.3 Find Extrinsic')

        self.ui.label_3.setFont(QtGui.QFont('Arial', 8))
        self.ui.label_3.setText('Select Image')

        self.ui.label_4.setFont(QtGui.QFont('Arial', 14))
        self.ui.label_4.setText('2. Augmented Reality')

        self.ui.label_5.setFont(QtGui.QFont('Arial', 14))
        self.ui.label_5.setText('3. Stereo Disparity Map')

        self.ui.label_6.setFont(QtGui.QFont('Arial', 14))
        self.ui.label_6.setText('4 SIFT')

        # Button
        self.ui.pushButton.setText('1.1 Find Corners')
        self.ui.pushButton.clicked.connect(self.buttonClicked1_1)

        self.ui.pushButton_2.setText('1.2 Find Intrinsic')
        self.ui.pushButton_2.clicked.connect(self.buttonClicked1_2)

        self.ui.pushButton_3.setText('1.4 Find Distortion')
        self.ui.pushButton_3.clicked.connect(self.buttonClicked1_3)

        self.ui.pushButton_4.setText('1.3 Find Extrinsic')
        self.ui.pushButton_4.clicked.connect(self.buttonClicked1_4)

        self.ui.pushButton_5.setText('2.1 Augmented Reality ')
        self.ui.pushButton_5.clicked.connect(self.buttonClicked1_5)

        self.ui.pushButton_6.setText('3.1 Stereo Disparity Map ')
        self.ui.pushButton_6.clicked.connect(self.buttonClicked1_6)


        self.ui.pushButton_7.setText('4.1 keypoints ')
        self.ui.pushButton_7.clicked.connect(self.buttonClicked1_7)


        self.ui.pushButton_8.setText('4.2 Matched keypoints ')
        self.ui.pushButton_8.clicked.connect(self.buttonClicked1_8)



        item = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15']
        [self.ui.comboBox.addItem(i) for i in item]
        self.ui.comboBox.activated[str].connect(self.Combox_4) #Signal


    def buttonClicked1_1(self):
        chessboard.Corners().cornerdec()

    def buttonClicked1_2(self):
        chessboard.Intrinsic_Matrix().find_Intrinsic_Matrix()

    def buttonClicked1_3(self):
        chessboard.Distortion_coefficients().find_distorsion()

    def Combox_4(self,text):
        chessboard.Extrinsic_Matrix().choose_file(text)

    def buttonClicked1_4(self):
        chessboard.Extrinsic_Matrix().find_extrinsic()

    def buttonClicked1_5(self):
        AR.AR_project().find_project_image()

    def buttonClicked1_6(self):
        Stereo.Disparity_map().disparity()

    def buttonClicked1_7(self):
        sift.draw_keypoints()

    def buttonClicked1_8(self):
        sift.draw_matches()

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())