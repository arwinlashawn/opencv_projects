# opencv_projects
All mini projects from an OpenCV course.

## Project 1: Live Pencil Sketch App

### Output Preview
> ![](https://i.imgur.com/VkFQN0W.png)
> *Notice that the edges of the clouds were also captured!*

### Steps
1. Convert input image to grayscale
2. Remove noise using **Gaussian Blur**
3. Use **Canny** algorithm to detect and extract edges
4. Apply threshold binary inverse to get white background with black edges (pencil sketch effect)

---

## Project 2: Shape Identifier

### Input Preview
> ![](https://i.imgur.com/7k2zOqo.png)

### Output Preview
> ![](https://i.imgur.com/qOrPMWa.png)

### Steps
1. Convert input image to grayscale and apply thresholding
2. Extract contours from the shapes
3. Use `approxPolyDP` to get number of sides of the shape
4. Deduce the shape using number of sides. Any shape more than 15 sides is assumed to be a circle
5. Further use conditionals to handle special cases like square and rectangle
6. Fill the shape with color and shape name if identified

---

## Project 3: Circle/Ellipse Counter
*No preview available because the program somehow does not work on my machine.*

---

## Project 4: Object Detector Using Template Image

### Template Image
![](https://i.imgur.com/XjCrIAH.png)

### Input Preview
![](https://i.imgur.com/pjDD4dx.png)

### Output Preview
![](https://i.imgur.com/414KJFU.png)

### Steps
1. Convert both input and template images to grayscale
2. Use `cv2.matchTemplate()` to return an array that represents the match found
3. Use `cv2.minMaxLoc()` to return the bounding box/coordinates that Mei was found in
4. Then use the coordinates to draw the green rectangle encasing the matching object

---

## Project 5: Live Object Detector Using SIFT and ORB
*No preview available because program is buggy. Need to check documentation.*

---

## Project 6: *Coming Soon*







