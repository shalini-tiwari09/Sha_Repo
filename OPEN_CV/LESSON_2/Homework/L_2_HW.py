#use of basic utility functions on images like arithmetic operations 
#of addition and subtraction, resizing, erosion, blurring and bordering.

#Addition
#'''
import cv2 
#import numpy as np 
     
image1 = cv2.imread('img1.jpg') 
image2 = cv2.imread('img2.jpg')

New_img_Sum = cv2.addWeighted(image1, 1.0, image2, 0.8, 0)
cv2.imshow(' Image 1 ', image1) 
cv2.imshow(' Image 2 ', image2) 
cv2.imshow('Weighted Image', New_img_Sum)

cv2.waitKey(0) 
cv2.destroyAllWindows() 
#'''

#Subtraction
'''
import cv2 

image1 = cv2.imread('im1.jpg') 
image2 = cv2.imread('im2.jpg')
  
new_img_sub = cv2.subtract(image1, image2)
cv2.imshow(' Image 1 ', image1) 
cv2.imshow(' Image 2 ', image2) 
cv2.imshow('Subtracted Image', new_img_sub)
  
cv2.waitKey(0)
cv2.destroyAllWindows()
'''

#Image Resizing
# Explain the various situtions where image resizing is needed

'''
import cv2

img = cv2.imread("Artt.png",1)
cv2.imshow("Original Image", img)

#Dimensions is (WIDTH, HEIGHT)
resized = cv2.resize(img, (200, 300))
cv2.imshow("reducedImage", resized)

cv2.waitKey(0)
cv2.destroyAllWindows()
'''

#Erosion
'''
import cv2
import numpy as np
  
image = cv2.imread("Artt.png", 1) 
cv2.imshow("Original", image) 
# kernel is used for erosion as an input
kernel = np.ones((5, 5), np.uint8)

image = cv2.erode(image, kernel) 
cv2.imshow("Eroded Image", image)

cv2.waitKey(0)
cv2.destroyAllWindows()
'''

#Bluring of an image
'''
import cv2

image = cv2.imread("penguin.png")

cv2.imshow('Original Image', image)
cv2.waitKey(0)

#Gaussian Blur
Gaussian = cv2.GaussianBlur(image, (7, 7), 0)
cv2.imshow('Gaussian Blurring', Gaussian)
cv2.waitKey(0)

#Median Blur
median = cv2.medianBlur(image, 5)
cv2.imshow('Median Blurring', median)
cv2.waitKey(0)


#Bilateral Blur
bilateral = cv2.bilateralFilter(image, 2, 85, 85)
cv2.imshow('Bilateral Blurring', bilateral)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''
'''
#Bordering an image
#cv2.copyMakeBorder(image, top, bottom, left, right, borderType, colorValue)
#SOLID Border
import cv2

img = cv2.imread("penguin.png")
borderedImage = cv2.copyMakeBorder(img, 10, 10, 30, 30, cv2.BORDER_CONSTANT, value = (100,0,105))

cv2.imshow("Bordered Image", borderedImage)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''

# Reflective Border around an image

'''
import cv2

img = cv2.imread("tree.png")
borderedImage = cv2.copyMakeBorder(img, 30, 30, 30, 30, cv2.BORDER_REFLECT, value = 1)
cv2.imshow("Original", img)
cv2.imshow("Bordered Image", borderedImage)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''

