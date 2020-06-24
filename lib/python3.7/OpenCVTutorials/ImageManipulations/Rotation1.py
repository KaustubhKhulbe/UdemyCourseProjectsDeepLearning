import cv2
import numpy as np

image = cv2.imread('/Users/kkhulbe/PycharmProjects/UdemyCourseProjectsDeepLearning/lib/python3.7/OpenCVTutorials/ImageManipulations/input.jpeg')
height, width = image.shape[:2]

# Divide by two to rototate the image around its centre
rotation_matrix = cv2.getRotationMatrix2D((width/2, height/2), 90, .5)

rotated_image = cv2.warpAffine(image, rotation_matrix, (width, height))

cv2.imshow('Rotated Image', rotated_image)
cv2.waitKey()
cv2.destroyAllWindows()