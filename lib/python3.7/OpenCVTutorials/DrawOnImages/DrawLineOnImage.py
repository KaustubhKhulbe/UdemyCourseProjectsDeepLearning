import cv2
import numpy as np

#Create a black square of dimensions 512 by 512 by 3
#Draw a diagonal blue line of width 5 pixels
image = np.zeros((512,512,3), np.uint8)
cv2.line(image, (0,0), (511,511), (255,127,0), 5) # inputs: image, top left coordinate, bottom right coordinate, RGB value, witdth


cv2.imshow("Black rectangle (Color)", image)

cv2.waitKey(0)
cv2.destroyAllWindows()
