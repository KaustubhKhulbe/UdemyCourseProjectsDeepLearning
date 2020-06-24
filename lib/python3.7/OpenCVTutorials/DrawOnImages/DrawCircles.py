import cv2
import numpy as np

# Create a black square of dimensions 512 by 512 by 3

image = np.zeros((512, 512, 3), np.uint8)
cv2.circle(image, (350, 350), 100, (15,75,50), -1)
# inputs: image, center, radius, RGB value, width
# By putting in -1, we can fill the image

cv2.imshow("Black rectangle (Color)", image)

cv2.waitKey(0)
cv2.destroyAllWindows()
