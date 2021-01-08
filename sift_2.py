import cv2 as cv
import numpy as np

# read images
img1 = cv.imread('./Hw1/Q4_Image/Aerial1.jpg')
img2 = cv.imread('./Hw1/Q4_Image/Aerial2.jpg')

img1 = cv.cvtColor(img1, cv.COLOR_BGR2GRAY)
img2 = cv.cvtColor(img2, cv.COLOR_BGR2GRAY)

#sift
sift = cv.xfeatures2d.SIFT_create()

# find keypoints and descriptor with SIFT
keypoints_1, descriptors_1 = sift.detectAndCompute(img1,None)
keypoints_2, descriptors_2 = sift.detectAndCompute(img2,None)

# kimg_1 = cv.drawKeypoints(img1, keypoints=keypoints_6, outImage=img1, color=(0, 255, 255),
#                                 flags=cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
keypoints_1_1 = []
keypoints_2_1 = []
descriptors_1_1 =[]
descriptors_2_1 =[]
matches = None
R1 = np.random.randint(0,len(keypoints_1),size=6)
R1.sort()
for r in R1:
    keypoints_1_1.append(keypoints_1[r])
    descriptors_1_1.append(descriptors_1[r,:])

R2 = np.random.randint(0,len(keypoints_2),size=6)
R2.sort()
for r in R2:
    keypoints_2_1.append(keypoints_2[r])
    descriptors_2_1.append(descriptors_2[r,:])

descriptors_1_1= np.array(descriptors_1_1)
descriptors_2_1= np.array(descriptors_2_1)
print(R1,R2)

#feature matching
fm = cv.BFMatcher(cv.NORM_L1, crossCheck=True)
matches = fm.match(descriptors_1_1, descriptors_2_1)
print(matches)
matches_true = fm.match(descriptors_1,descriptors_2)
matches_true = sorted(matches_true, key=lambda x: x.distance)
keypoints_1_1 = []
keypoints_2_1 = []
print(len(matches))
for i in range(len(matches[:6])):
    keypoints_1_1.append(keypoints_1[ matches[i].queryIdx])
    keypoints_2_1.append(keypoints_2[ matches[i].trainIdx])
print(matches_true[:6])



img3 = cv.drawMatches(img1, keypoints_1_1, img2, keypoints_2_1, matches, img2, flags=cv.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)
# img3 = cv.drawMatches(img1, keypoints_1, img2, keypoints_2, matches_true[:6], img2, flags=cv.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)
# img1 = cv.drawKeypoints(img1, keypoints=keypoints_1_1, outImage=img1, color=(0, 255, 255),
#                        flags=cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
# img2 = cv.drawKeypoints(img2, keypoints=keypoints_2_1, outImage=img2, color=(0, 255, 255),
#                        flags=cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)


cv.imshow('show', img3)
cv.waitKey(0)
cv.destroyAllWindows()