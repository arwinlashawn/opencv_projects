import cv2
import numpy as np 
import os

os.chdir("/Users/macintosh/Desktop")

# load image and convert to grayscale
image = cv2.imread("cstudy.jpg")
while cv2.waitKey() != 27:
	cv2.imshow("Where is Mei?", image)
cv2.destroyAllWindows()

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# load template image (a small cropped area of the image)
template = cv2.imread("cropped.jpg", 0)

result = cv2.matchTemplate(gray, template, cv2.TM_CCOEFF)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

# create bounding box
top_left = max_loc
bottom_right = (top_left[0] + 200, top_left[1] + 200)
cv2.rectangle(image, top_left, bottom_right, (0, 255, 0), 5)

while cv2.waitKey() != 27:
	cv2.imshow("There she is!", image)
cv2.destroyAllWindows()