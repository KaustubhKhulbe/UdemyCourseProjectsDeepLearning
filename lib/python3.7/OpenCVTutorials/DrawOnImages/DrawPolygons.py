import cv2
import numpy as np


#Lets define 4 points
pts = np.array([ [10,50], [400,50], [90,200], [50,500]], np.int32)

#Lets reshape the points in the form required by polylines
pts = pts.reshape((-1,1,2))

# Create a black square of dimensions 512 by 512 by 3
image = np.zeros((512, 512, 3), np.uint8)

cv2.polylines(image, [pts], True, (0,0,255), 3)
# inputs: image, array of points,  , color, width
# By putting in -1, we can fill the image

cv2.imshow("Black rectangle (Color)", image)

cv2.waitKey(0)
cv2.destroyAllWindows()
