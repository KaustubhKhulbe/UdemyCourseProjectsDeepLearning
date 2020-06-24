import cv2
import numpy as np

# Create a black square of dimensions 512 by 512 by 3

image = np.zeros((512, 512, 3), np.uint8)
cv2.putText(image, 'Hello World', (75,290), cv2.FONT_HERSHEY_COMPLEX, 2, (100,170,0), 3)
# inputs: image, text to display, bottom left coordinate, Font, Font size, RGB value, thickness


cv2.imshow("Black rectangle (Color)", image)

cv2.waitKey(0)
cv2.destroyAllWindows()
