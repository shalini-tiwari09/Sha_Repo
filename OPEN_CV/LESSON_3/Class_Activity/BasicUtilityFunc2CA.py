#This project explores more basic utility functions like changing colour 
#spaces for an image and applying rotation and edge detection techniques.

# Grayscaling of an image read as colored
#Grayscale the image - Using cvtColor() function
#'''
import cv2
 
image = cv2.imread('pika.png')
cv2.imshow('Original Image', image)
cv2.waitKey(0)

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow('Grayscale Image', gray_image)

cv2.waitKey(0) 
cv2.destroyAllWindows() 
#'''

'''
#Grayscale the image - Without using the library
#Using averaging of pixels method
import cv2

img = cv2.imread('pika.png')
(row, col) = img.shape[0:2]

for i in range(row):
	for j in range(col):
		# Find the average of the BGR pixel values
		img[i, j] = sum(img[i, j]) * 0.33

cv2.imshow('Grayscale Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''

'''
# Rotating an image
import cv2

img = cv2.imread("pika.png")
(rows, cols) = img.shape[:2]

M = cv2.getRotationMatrix2D((cols / 2, rows / 2), 45, 1)
res = cv2.warpAffine(img, M, (cols, rows))

cv2.imwrite('result.jpg', res)
'''

'''
#Edge Detection in an image
import cv2
img = cv2.imread('pika.png')
edges = cv2.Canny(img, 100, 200)

cv2.imwrite('result_edge_detect.jpg', edges)
'''

# Convert an image from RGB to HSV - using cv2.cvtColor() method
'''
import cv2

image = cv2.imread('pika.png')
hsvImage = cv2.cvtColor(image, cv2.COLOR_BGR2HSV )

cv2.imshow("Pikachu I am", image)
cv2.waitKey(0)
cv2.imshow("Pikachu I am", hsvImage)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''