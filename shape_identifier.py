import cv2
import numpy as np 
import os 

os.chdir("/Users/macintosh/Desktop")

# load the shape template or reference image
image = cv2.imread("shapes.png")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# get the width and height and scale them
width = int(image.shape[1] * 0.8)
height = int(image.shape[0] * 0.8)
 
# image = cv2.resize(image, (width, height)) # to resize window because too big
cv2.imshow('Shape Identifier', image)
cv2.waitKey()

ret, thresh = cv2.threshold(gray, 127, 255, 1)

# extract contours
contours, hierarchy = cv2. findContours(thresh.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)

for cnt in contours:

	# get approximate polygons
	approx = cv2.approxPolyDP(cnt, 0.01 * cv2.arcLength(cnt, True), True)

	if len(approx) == 3:
		shape_name = "Triangle"
		cv2.drawContours(image, [cnt], 0, (0, 255, 0), -1)

		# find contour center to place text at the center
		M = cv2.moments(cnt)
		cx = int(M['m10'] / M['m00'])
		cy = int(M['m01'] / M['m00'])
		cv2.putText(image, shape_name, (cx-50, cy), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 1)

	elif len(approx) == 4:
		x,y,w,h = cv2.boundingRect(cnt)
		# print(x, y, w, h)
		M = cv2.moments(cnt)
		cx = int(M['m10'] / M['m00'])
		cy = int(M['m01'] / M['m00'])

		# check to see if 4-side polygon is square OR rectangle
		# cv2.boundingRect returns the top left and then width and height
		if abs(w-h) == 0:
			shape_name = "Square"

			# find contour center to place text at center
			cv2.drawContours(image, [cnt], 0, (0, 125, 255), -1)
			cv2.putText(image, shape_name, (cx-50, cy), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 1)

		else:
			shape_name = "Rectangle"

			# find contour center to place text at the center
			cv2.drawContours(image, [cnt], 0, (0, 0, 255), -1)
			M = cv2.moments(cnt)
			cx = int(M['m10'] / M['m00'])
			cy = int(M['m01'] / M['m00'])
			cv2.putText(image, shape_name, (cx-50, cy), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 1)

	elif len(approx) == 6:
		shape_name = "Hexagon"
		cv2.drawContours(image, [cnt], 0, (255, 0, 0), -1)
		M = cv2.moments(cnt)
		cx = int(M['m10'] / M['m00'])
		cy = int(M['m01'] / M['m00'])
		cv2.putText(image, shape_name, (cx-50, cy), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 1)

	elif len(approx) == 10:
		shape_name = "Star"
		cv2.drawContours(image, [cnt], 0, (255, 255, 0), -1)
		M = cv2.moments(cnt)
		cx = int(M['m10'] / M['m00'])
		cy = int(M['m01'] / M['m00'])
		cv2.putText(image, shape_name, (cx-50, cy), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 1)

	elif len(approx) >= 15:
		shape_name = "Circle"
		cv2.drawContours(image, [cnt], 0, (0, 255, 255), -1)
		M = cv2.moments(cnt)
		cx = int(M['m10'] / M['m00'])
		cy = int(M['m01'] / M['m00'])
		cv2.putText(image, shape_name, (cx-50, cy), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 1)

width = int(image.shape[1] * 0.8)
height = int(image.shape[0] * 0.8)


# image = cv2.resize(image, (width, height)) # to resize window because too big
while cv2.waitKey() != 27: # to only close when pressing Esc! had to do this because i wanted to take a screenshot
	cv2.imshow("Shape Identifier", image)


cv2.destroyAllWindows()












