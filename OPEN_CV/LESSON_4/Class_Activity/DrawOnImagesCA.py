# Draw a line on the image
#'''
import cv2 
image = cv2.imread("city.png")

start_point = (320, 0)
end_point = (380, 110)

start_point1 = (380, 110)
end_point1 = (440, 0)

color = (32, 165, 218)  #format for color is BGR
line_thickness = 7
  
image = cv2.line(image, start_point, end_point, color, line_thickness)
image = cv2.line(image, start_point1, end_point1, color, line_thickness) 

cv2.imshow("Image", image) 
cv2.waitKey(0)
cv2.destroyAllWindows()
#'''

# Draw a rectangle on the image
'''
import cv2 
image = cv2.imread("pika.png")
  
# Start coordinate, here (5, 5) represents the top left corner of rectangle
start_point = (190, 80)
end_point = (670, 500) 

color = (0, 0, 128)
thickness = 5
  
image = cv2.rectangle(image, start_point, end_point, color, thickness)
  
cv2.imshow("Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''

'''
# Using thickness of -1 px to fill the rectangle by black color.
import cv2
image = cv2.imread("pika.png", 0)
start_point = (100, 50)
end_point = (200, 150)
color = (0, 0, 0)
thickness = -1
image = cv2.rectangle(image, start_point, end_point, color, thickness)
cv2.imshow("Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''

# Draw the circle on the image
'''
import cv2
image = cv2.imread("pika.png")

center_coordinates = (200, 300)
radius = 55

color = (19, 69, 139)
thickness = 3

image = cv2.circle(image, center_coordinates, radius, color, thickness)

cv2.imshow("Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''

# Using thickness of -1 px to fill the circle by red color. 
'''
import cv2
image = cv2.imread("pika.png")
window_name = 'Image'
center_coordinates = (200, 300)
radius = 55
color = (0, 0, 180)
thickness = -1
image = cv2.circle(image, center_coordinates, radius, color, thickness)
cv2.imshow(window_name, image)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''

#Text on the image
'''	
import cv2
image = cv2.imread("sunflower.png")

font = cv2.FONT_HERSHEY_SIMPLEX

org = (50, 50)
fontScale = 1
color = (11, 134, 184)
thickness = 2
# Using cv2.putText() method
image = cv2.putText(image, 'Sun Flower', org, font, fontScale, color, thickness, cv2.LINE_AA)
window_name = "Tect on Image"
cv2.imshow(window_name, image)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''