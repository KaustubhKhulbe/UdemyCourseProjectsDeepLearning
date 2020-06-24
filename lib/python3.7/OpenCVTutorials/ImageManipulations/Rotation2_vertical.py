import cv2



#Other Option to Rotate
img = cv2.imread('/Users/kkhulbe/PycharmProjects/UdemyCourseProjectsDeepLearning/lib/python3.7/OpenCVTutorials/ImageManipulations/input.jpeg')

rotated_image = cv2.transpose(img)

cv2.imshow('Rotated Image - Method 2', rotated_image)
cv2.waitKey()
cv2.destroyAllWindows()