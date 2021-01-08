import cv2 as cv

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

print(keypoints_1)

#feature matching
fm = cv.BFMatcher(cv.NORM_L1, crossCheck=True)
matches = fm.match(descriptors_1,descriptors_2)

matches = sorted(matches, key = lambda x:x.distance)
keypoints_1_1 = []
keypoints_2_1 = []
print(len(matches))
for i in range(len(matches[:6])):
    keypoints_1_1.append(keypoints_1[ matches[i].queryIdx])
    keypoints_2_1.append(keypoints_2[ matches[i].trainIdx])



def draw_keypoints():
    FeatureAerial1 = cv.drawKeypoints(img1, keypoints=keypoints_1_1, outImage=img1,
                              flags=cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    FeatureAerial2 = cv.drawKeypoints(img2, keypoints=keypoints_2_1, outImage=img2,
                              flags=cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    cv.imwrite('./Hw1/Q4_Image/FeatureAerial1.jpg', FeatureAerial1)
    cv.imwrite('./Hw1/Q4_Image/FeatureAerial2.jpg', FeatureAerial2)
    cv.imshow('show1', FeatureAerial1)
    cv.imshow('show2', FeatureAerial2)
    cv.waitKey(0)
    cv.destroyAllWindows()
def draw_matches():
    img3 = cv.drawMatches(img1, keypoints_1, img2, keypoints_2, matches[:6], img2, flags=cv.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)
    cv.imshow('show3', img3)
    cv.waitKey(0)
    cv.destroyAllWindows()

