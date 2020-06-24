import cv2

image = cv2.imread('/Users/kkhulbe/PycharmProjects/UdemyCourseProjectsDeepLearning/lib/python3.7/OpenCVTutorials/ImageManipulations/input.jpeg')
# Let's now to a horizontal flip (reflection).
flipped = cv2.flip(image, 1)
cv2.imshow('Horizontal Flip', flipped)
cv2.waitKey()
cv2.destroyAllWindows()