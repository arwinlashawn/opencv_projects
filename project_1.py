import cv2
import numpy as np 
import os 

os.chdir("/Users/macintosh/Desktop")

### Live Pencil Sketch App! 
# for some reason this only works in Jupyter Notebook, not Sublime Text

def sketch(image):
	# first convert image to grayscale
	img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

	# clean up image using Gaussian Blue (removes noise)
	img_gray_blur = cv2.GaussianBlur(img_gray, (5,5), 0)

	# time to extract edges using the best algo, canny
	canny_edges = cv2.Canny(img_gray_blur, 10, 70) # can play around with these thresholds

	# need to invert binarize the image. if not done, it will be a black backrground with white edges 
	ret, mask = cv2.threshold(canny_edges, 70, 255, cv2.THRESH_BINARY_INV)
	return mask


# initialize webcam, cap is the project provided by VideoCapture
# it contains a boolean indicating if it was successful or not (ret)
# it also contains the images collected from the webcam (frame)

cap = cv2.VideoCapture(0)

while True:
	ret, frame = cap.read()
	cv2.imshow("My Live Sketcher", sketch(frame))
	if cv2.waitKey(1) == 13: # 13 here is the Enter key
		break

# to release camera and close windows
cap.release()
cv2.destroyAllWindows()


