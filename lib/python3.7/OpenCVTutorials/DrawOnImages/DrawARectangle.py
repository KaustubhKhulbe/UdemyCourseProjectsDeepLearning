import cv2
import numpy as np

# Create a black square of dimensions 512 by 512 by 3

image = np.zeros((512, 512, 3), np.uint8)
cv2.rectangle(image, (0, 0), (300, 250), (127, 50, 127),5)
# inputs: image, top left coordinate, bottom right coordinate, RGB value, width
# By putting in -1 instead of 5, we can fill the image

cv2.imshow("Black rectangle (Color)", image)

cv2.waitKey(0)
cv2.destroyAllWindows()
