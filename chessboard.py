import cv2 as cv
import numpy as np
import glob
import argparse


# parser = argparse.ArgumentParser(description='camera calibration')
# parser.add_argument('--which_file', default=None, type=str, help='learning rate')
# args = parser.parse_args()

file_path = './Hw1/Q1_Image/'

object_point = [] # 3D world
image_point = [] # 2D image plane
image_size = []
intrinsics_matrix = []
distortion_coefficients = []
f = None # 1.3 choose file name
rotation_vectors = []
translation_vectors = []


class Corners():
    # def __init__(self):
    #     self.object_point = [] # 3D world
    #     self.image_point = [] # 2D image plane
    # def cornerdec(self):
    def cornerdec(self):
        # glob image_size
        # threshold
        criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 30, 0.001)
        # size of chessboard corner
        w , h = 11,8
        # coordination of chessboard in 3D world
        ob_cd = np.zeros((w*h, 3), dtype=np.float32)
        ob_cd[:,:2] = np.mgrid[0:w,0:h].T.reshape(-1,2)
        # print(ob_cd)
        images = glob.glob(file_path + '*.bmp')
        # print(images)
        global object_point
        global image_point
        for file_name in images:
            # print(file_name)
            img = cv.imread(file_name)
            img2gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
            global image_size
            image_size = img2gray.shape[::-1]

            # find chess board corners
            ret, corners = cv.findChessboardCorners(img2gray,(w,h),None)
            # print(ret)
            # Add object points, image points
            if ret == True:
                # increase accuracy with cv.cornerSubPix
                corners2 = cv.cornerSubPix(img2gray,corners, winSize=(5,5),zeroZone=(-1,-1), criteria=criteria)
                # self.object_point.append(ob_cd)
                # self.image_point.append(corners2)
                object_point.append(ob_cd)
                image_point.append(corners2)
                # draw the corners
                cv.drawChessboardCorners(img, patternSize=(w, h), corners=corners2, patternWasFound=ret)
                # cv.drawChessboardCorners(img, patternSize=(w, h), corners=corners, patternWasFound=ret)
                cv.imshow('img', img)
                cv.waitKey(1000)
        cv.destroyAllWindows()

class Intrinsic_Matrix(Corners):
    def __init__(self):
        super(Corners)
        self.intrinsics_matrix = []
        self.distortion_coefficients=[]
        self.rotation_vectors=[]
        self.translation_vectors=[]
    def find_Intrinsic_Matrix(self):
        global distortion_coefficients,intrinsics_matrix,rotation_vectors,translation_vectors
        ret, intrinsics_matrix, distortion_coefficients,rotation_vectors,translation_vectors = cv.calibrateCamera(object_point,image_point,image_size,None,None)
        self.intrinsics_matrix.append(intrinsics_matrix)
        self.distortion_coefficients.append(distortion_coefficients)
        self.rotation_vectors.append(rotation_vectors)
        self.translation_vectors.append(translation_vectors)
        print('intrinsics_matrix','\n',intrinsics_matrix)
        # print(np.shape(rotation_vectors),np.shape(translation_vectors))

        return self.intrinsics_matrix,self.distortion_coefficients,self.rotation_vectors,self.translation_vectors

class Distortion_coefficients(Intrinsic_Matrix):
    def __init__(self):
        super(Intrinsic_Matrix, self)
    def find_distorsion(self):
        print('distortion_coefficients','\n',distortion_coefficients)

class Extrinsic_Matrix():
    def __init__(self):
        super(Intrinsic_Matrix)
    def choose_file(self,file_name):
        global f
        f = int(file_name)
        # print(f)
    def find_extrinsic(self):
        ro,t = rotation_vectors[f-1],translation_vectors[f-1]
        Ro = cv.Rodrigues(ro.T)[0]
        extrinsic = np.concatenate((Ro,t),axis=1)
        print('extrinsic matrix','image',f,'\n',extrinsic)


# if __name__ == '__main__':
#     Corners().cornerdec()
#     # print(im)
#     # print(object_point,image_point)
#     Intrinsic_Matrix().find_Intrinsic_Matrix()
#     Extrinsic_Matrix().choose_file(5)
#     Extrinsic_Matrix().find_extrinsic()









