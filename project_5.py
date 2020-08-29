import cv2
import numpy as np 
import os

os.chdir("/Users/macintosh/Desktop")

print("hey")

def sift_detector(new_image, image_template):
	# function that compares input image to template
	# it then returns the number of SIFT matches between them

	image1 = cv2.cvtColor(new_image, cv2.COLOR_BGR2GRAY)
	image2 = image_template

	# create SIFT detector object
	sift = cv2.SIFT()

	# obtain the keypoints and descriptors using SIFT
	keypoints_1, descriptors_1 = sift.detectAndCompute(image1, None)
	keypoints_2, descriptors_2 = sift.detectAndCompute(image2, None)

	# define parameters for our Flann Matcher
	FLANN_INDEX_KDTREE = 0
	index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees=3)
	search_params = dict(checks=100)

	# create the Flann Matcher object
	flann = cv2.FlannBasedMatcher(index_params, search_params)

	# obtain matches using KNN method
	# the result "matches" us
	matches = flann.knnMatch(descriptors_1, descriptors_2, k=2)

	# store good matches using Lowe's ratio test
	good_matches = []
	for m, n in matches:
		if m.distance < 0.7 * n.distance:
			good_matches.append[m]

	return len(good_matches)

cap = cv2.VideoCapture(0)

# load our image template, this is our reference image
image_template = cv2.imread("milo.jpg", 0)


while True:
	# get webcam images
	ret, frame = cap.read() 

	# get height and width of webcam frame
	height, width = frame.shape[:2]

	# definte ROI Box dimensions
	top_left_x = width/3
	top_left_y = (height/2) + (height/4)
	bottom_right_x = (width/3) * 2
	bottom_right_y = (height/2) - (height/4)

	# draw rectangular window for our region of interest
	cv2.rectangle(frame, (top_left_x, top_left_y), (bottom_right_x, bottom_right_y), 255, 3)

	# crop window of observation we defined above
	cropped = frame[bottom_right_y:top_left_y, top_left_x:bottom_right_x]

	# flip frame orientation horizontally
	frame = cv2.flip(frame, 1)

	# get number of SIFT matches
	matches = sift_detector(cropped, image_template)

	# display statis string showing the current number of matches
	cv2.putText(frame, str(matches), (450, 450), cv2.FRONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 1)

	# our threshold to indicate object detection
	# we use 10 since the SIFT detector returns little false positives
	threshold = 10

	# if matches exceed our threshold then object has been detected
	if matches > threshold:
		cv2.rectangle(frame, (top_left_x, top_left_y), (bottom_right_x, bottom_right_y), (0, 255, 0), 3)
		cv2.putText(frame, "Object Found", (50, 50), cv2.FRONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)

	cv2.imshow("Object Detector Using SIFT", frame)
	if cv2.waitKey(1) == 13: # 13 is the Enter key
		break

cap.release()
cv2.destroyAllWindows()










