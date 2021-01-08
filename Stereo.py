import cv2 as cv

class Disparity_map():
    def __init__(self):
        self.file_path = './Hw1/Q3_Image/'
        self.imgL = cv.imread(self.file_path+'imL.png', 0)
        self.imgR = cv.imread(self.file_path+'imR.png', 0)
    def disparity(self):
        window_size = 15 # odd number in 5-255
        numDisparities=16 # positive and divided by 16
        stereo = cv.StereoBM_create(numDisparities=numDisparities, blockSize=window_size)
        disparity_map = stereo.compute(self.imgL, self.imgR)
        # Visualization
        disparity_map = cv.normalize(disparity_map, disparity_map, alpha=0, beta=255, norm_type=cv.NORM_MINMAX, dtype=cv.CV_8U)

        cv.imshow('disparity', disparity_map)
        cv.waitKey(5000)
        cv.destroyAllWindows()
