#imports
import cv2 #OpenCV
import numpy as np #Arrays

#read image
image = cv2.imread('../red.png')

#convert to HSV
col = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

#only check for certain range of red
mask = cv2.inRange(col, np.array([0, 175, 175]), np.array([0, 255, 255]))

#smoothing the image
gaus = cv2.GaussianBlur(mask, (5, 5), 0)

#simple threshold
_, thresh = cv2.threshold(gaus, 150, 255, cv2.THRESH_BINARY)

#image dimensions
h, w = thresh.shape

#each set of cones is split based on whether they were on the left or right side of the image
left = []
right = []
for y in range(h):
    for x in range(w):
        #only checking the filtered red pixels
        if thresh[y, x] == 255:
            if x < w/2:
                left.append((x, y))
            else:
                right.append((x, y))

#draws straight lines for each side of cones
cv2.line(image, left[0], left[-1], (0, 0, 255), 2)
cv2.line(image, right[0], right[-1], (0, 0, 255), 2)

cv2.imwrite('../answer.png', image)
