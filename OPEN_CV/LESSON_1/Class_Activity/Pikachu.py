#with the Pikachu image , perform the same sequence 
#of steps as done in the class activity file

'''
import cv2
img = cv2.imread("pikachu.png", cv2.IMREAD_COLOR)
cv2.imshow("Pikachu Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''

#Display an image in grayscale 
'''
import cv2
img = cv2.imread("pikachu.png", cv2.IMREAD_COLOR)
cv2.imshow("Pikachu in Grayscale", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''

#Saving an image after making some changes
'''
import cv2
import os

saved_directory = "C:/temp"  #location where to save the image after changes
img = cv2.imread("pikachu.png", 0)
cv2.imshow("Pikachu in Black and White", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#save image 
os.chdir(saved_directory)
cv2.imwrite("BlackWhite.png", img)
print("Successfully Saved")
'''

#different color formats
'''
import cv2
image = cv2.imread("pikachu.png", 1)
# Split the image in red, blue and green different saturations
B, G, R = cv2.split(image)
  
cv2.imshow("original", image)
cv2.waitKey(0)
  
cv2.imshow("Blue Saturation Image", B)
cv2.waitKey(0)
  
cv2.imshow("Green Saturation Image", G)
cv2.waitKey(0)
  
cv2.imshow("Red Saturation Image", R)
cv2.waitKey(0)
  
cv2.destroyAllWindows()
'''