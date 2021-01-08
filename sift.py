# -*- coding:utf-8 -*-
import os
import cv2 as cv
import numpy as np
import glob

path = './Hw1/Q4_Image/'
keypoints_6 = []
keypoints = []
class find_keypoints():
    file_path = glob.glob(path + '*.jpg')
    n = 0
    for i in file_path:
        img = cv.imread(i)
        gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        # create sift
        sift = cv.xfeatures2d.SIFT_create()

        # 進行檢測和計算  返回特徵點資訊和描述符
        global keypoints_6, keypoints
        keypoints, descriptor = sift.detectAndCompute(gray, None)
        # keypoints：特徵點集合list，向量內每一個元素是一個KeyPoint物件，包含了特徵點的各種屬性資訊

        # Draw 6 keypoints
        K = np.random.randint(0,len(keypoints),size=6)
        [keypoints_6.append(keypoints[k]) for k in K]
        # , color=(0, 0, 256)
        img = cv.drawKeypoints(img, keypoints=keypoints_6, outImage=img, color=(0, 255, 255),
                                flags=cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
        print(keypoints_6)
        n = n +1
        # sift得到的影象為128維的特徵向量集
        file_name = 'FeatureAerial'+str(n)+'.jpg'
        print(file_name)
        cv.imwrite(file_name,img)
        cv.imshow('sift.jpg', img)
    cv.waitKey(100)
    cv.destroyAllWindows()

find_keypoints()

