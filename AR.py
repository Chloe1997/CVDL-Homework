import cv2 as cv
import numpy as np
import glob


file_path = './Hw1/Q2_Image/'

object_point = [] # 3D world
image_point = [] # 2D image plane
image_size = []
intrinsics_matrix = []
distortion_coefficients = []
rotation_vectors = []
translation_vectors = []

class Corners():
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

            if ret == True:
                object_point.append(ob_cd)
                # increase accuracy with cv.cornerSubPix
                corners2 = cv.cornerSubPix(img2gray,corners, winSize=(5,5),zeroZone=(-1,-1), criteria=criteria)
                image_point.append(corners2)




class Intrinsic_Extrinsic_Matrix(Corners):
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


def draw(img, imgpts):
    # Draw three lines in three directions
    for j in range(np.shape(imgpts)[0]):
        cv.line(img, tuple(imgpts[j,0].ravel()), tuple(imgpts[j,1].ravel()), (0, 0, 255), 5)
    return img


class AR_project():
    def __init__(self):
        super(Intrinsic_Extrinsic_Matrix)
        self.tetrahedron = np.float32([[3,3,-3],[1,1,0],[3,5,0],[5,1,0]]).reshape(-1,3)

    def find_project_image(self):
        Corners().cornerdec()
        Intrinsic_Extrinsic_Matrix().find_Intrinsic_Matrix()
        # print(intrinsics_matrix,'\n',distortion_coefficients)
        # print(self.tetrahedron.shape)
        # size of chessboard corner
        w, h = 11, 8
        # coordination of chessboard in 3D world
        ob_cd = np.zeros((w * h, 3), dtype=np.float32)
        ob_cd[:, :2] = np.mgrid[0:w, 0:h].T.reshape(-1, 2)
        # print(ob_cd)
        images = glob.glob(file_path + '*.bmp')
        # print(images)
        for file_name in images:
            # print(file_name)
            img = cv.imread(file_name)
            img2gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
            # find chess board corners
            ret, corners = cv.findChessboardCorners(img2gray, (w, h), None)
            # Add object points, image points
            if ret == True:
                _,ro, t,_ = cv.solvePnPRansac(ob_cd, corners, intrinsics_matrix,distortion_coefficients)
                object_image,ret = cv.projectPoints(self.tetrahedron, ro, t, intrinsics_matrix,distortion_coefficients)
                object_image = np.reshape(object_image, [4, 2])
                p = []
                for i in range(0, 4):
                    for j in range(i + 1, 4):
                        p.append([object_image[i], object_image[j]])
                p = np.array(p)
                img = draw(img, p)
                cv.imshow('img', img)
                cv.waitKey(500)
        cv.destroyAllWindows()





if __name__ == '__main__':
    AR_project().find_project_image()









