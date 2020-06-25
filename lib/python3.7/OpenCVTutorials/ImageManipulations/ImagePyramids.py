import cv2

image = cv2.imread('/Users/kkhulbe/PycharmProjects/UdemyCourseProjectsDeepLearning/lib/python3.7/OpenCVTutorials/ImageManipulations/input.jpeg')

smaller = cv2.pyrDown(image)
larger = cv2.pyrUp(smaller)

cv2.imshow('Original', image )

cv2.imshow('Smaller ', smaller )
cv2.imshow('Larger ', larger )
cv2.waitKey(0)
cv2.destroyAllWindows()