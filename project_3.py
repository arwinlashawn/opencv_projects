import cv2
import numpy as np 
import os

os.chdir("/Users/macintosh/Desktop")

# load the image
image = cv2.imread("circles.jpg", 0)
cv2.imshow("Original Image", image)
cv2.waitKey()

# initialize the detector using the default parameters
detector = cv2.SimpleBlobDetector()

# detect blobs
keypoints = detector.detect(image)

# draw blobs on our image as red circles
blank = np.zeros((1, 1))
blobs = cv2.drawKeyPoints(image, keypoints, blank, (0, 0, 255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

number_of_blobs = len(keypoints)
text = "Total Number of Blobs: " + str(len(keypoints))
cv2.putText(blobs, text, (20, 550), cv2.FONT_HERSHEY_SIMPLEX, 1, (100, 0, 255), 2)

# display image with blob keypoints
cv2.imshow("Blobs using default parameters", blobs)
cv2.waitKey()

# set out filtering parameters
# initialize the parameter setting usng cv2.SimpleBlobDetector
params = cv2.SimpleBlobDetector_Params()

# set area filtering parameters
params.filterByArea = True
params.minArea = 100

# set circularity filtering parameters
params.filterByCircularity = True
params.minCircularity = 0.9

# set convexity filtering parameters
params.filterByConvexity = True
params.minConvexity = 0.2

# set inertia filtering parameters
params.filterByInertia = True
params.minInertiaRatio = 0.01

# create a detector with the parameters
detector = cv2.SimpleBlobDetector(params)

# detect blobs
keypoints = detector.detect(image)

# draw blobs on our image as red circles
blank = np.zeros((1, 1))
blobs = cv2.drawKeyPoints(image, keypoints, blank, (0, 255, 0), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

number_of_blobs = len(keypoints)
text = "Number of circular blobs: " + str(len(keypoints))
cv2.putText(blobs, text, (20, 550), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 100, 255), 2)

# show blobs

cv2.imshow("Filtering Circular Blobs Only", keypoints)

cv2.waitKey(0)

cv2.destroyAllWindows()














