import numpy as np
import cv2

image = cv2.imread('/Users/kkhulbe/PycharmProjects/UdemyCourseProjectsDeepLearning/lib/python3.7/OpenCVTutorials/Blurring/elephant.jpg')

# Parameters, after None are - the filter strength 'h' (5-10 is a good range)
# Next is hForColorComponents, set as same value as h again
#
dst = cv2.fastNlMeansDenoisingColored(image, None, 6, 6, 7, 21)

cv2.imshow('Fast Means Denoising', dst)
cv2.waitKey(0)

cv2.destroyAllWindows()