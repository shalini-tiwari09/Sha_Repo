import cv2
import os

save_to_dir = "C:/temp"

img = cv2.imread("house.png", 1)
# Split the image in red, blue and green different saturations
B, G, R = cv2.split(img)
  
cv2.imshow("original", img)
cv2.waitKey(0)
  
cv2.imshow("Blue Saturation Image", B)
cv2.waitKey(0)
  
cv2.imshow("Green Saturation Image", G)
cv2.waitKey(0)
  
cv2.imshow("Red Saturation Image", R)
cv2.waitKey(0)
  
cv2.destroyAllWindows()
#''' remove hashtag to see output for another way
os.chdir(save_to_dir)
cv2.imwrite("original.png", img)
cv2.imwrite("Blue_saturation.png", B)
cv2.imwrite("Green_saturation.png", G)
cv2.imwrite("Red_saturation.png", R)
print("Successfully Saved")
'''
#save to the directory
#ANOTHER WAY - Without os.chdir(save_to_dir)

cv2.imwrite(save_to_dir + "/Original_Image.png", img)
cv2.imwrite(save_to_dir + "/Blue_Channel.png", B)
cv2.imwrite(save_to_dir + "/Green_Channel.png", G)
cv2.imwrite(save_to_dir + "/Red_Channel.png", R)
''' #remove the quotes for second method output