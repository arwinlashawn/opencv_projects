import cv2
import numpy as np 
import time
import os 


os.chdir("/Users/macintosh/Desktop")

### Pedestrian Identifier

# first create our body classifier
body_classifier = cv2.CascadeClassifier("haarcascade_fullbody.xml")

# initiate the video capture for video file
cap = cv2.VideoCapture("tokyo.mp4")

# loop once video is successfully loaded
while cap.isOpened():

	# read first frame
	ret, frame = cap.read()
	frame = cv2.resize(frame, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_LINEAR)

	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	# pass frame to our body classifier
	bodies = body_classifier.detectMultiScale(gray, 1.2, 3)

	# extract bounding boxes for any bodies identified
	for (x,y,w,h) in bodies:
		cv2.rectangle(frame, (x,y), (x+w, y+h), (0, 255, 255), 2)
		cv2.imshow("Pedestrians", frame)

	if cv2.waitKey(1) == 27:
		break

cap.release()
cv2.destroyAllWindows()


### Car detection

# set car classifier
car_classifier = cv2.CascadeClassifier("cars.xml")

# initiate video captire for video file
cap = cv2.VideoCapture("cars.mp4")

# loop once video is successfully loaded
while cap.isOpened():

	time.sleep(.2)
	# read first frame
	ret, frame = cap.read()
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	# pass frmae to our car classfier
	cars = car_classifier.detectMultiScale(gray, 1.3, 3)

	# extract bounding boxes for any car identified
	for (x,y,w,h) in cars:
		cv2.rectangle(frame, (x,y), (x+w, y+h), (0, 255, 255), 2)
		cv2.imshow("Cars", frame)

	if cv2.waitKey(1) == 27:
		break

cap.release()
cv2.destroyAllWindows()










