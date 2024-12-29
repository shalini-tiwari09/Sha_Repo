# Draw a line on the image
#'''
import cv2 
image = cv2.imread("night.jpg")

# Draw a hut on the image
start_point = (300,500)
end_point = (500, 650)
 
start_point3 = (410,580)
end_point3 = (450, 650) 

#Roof
start_point1 = (300,500)
end_point1 = (400, 400) 
  
start_point2 = (400, 400)
end_point2 = (500, 500)

color = (32, 165, 218)
line_thickness = 4

#dotted Stars
cir_centre = (240, 250)
cir_centre1 = (500, 40)
cir_centre2 = (400, 250)
cir_centre3 = (120, 25)
cir_centre4 = (350, 80)
cir_centre5 = (50, 300)
cir_centre6 = (350, 200)

radius = 3

color1 = (255, 255, 255)
thickness = -1
st_thickness = 2

image = cv2.rectangle(image, start_point, end_point, color, line_thickness)
image = cv2.line(image, start_point1, end_point1, color, line_thickness)
image = cv2.line(image, start_point2, end_point2, color, line_thickness) 
image = cv2.rectangle(image, start_point3, end_point3, color, line_thickness)

image = cv2.circle(image, cir_centre, radius, color1, thickness)
image = cv2.circle(image, cir_centre1, radius, color1, thickness)
image = cv2.circle(image, cir_centre2, radius, color1, thickness)
image = cv2.circle(image, cir_centre3, radius, color1, thickness)
image = cv2.circle(image, cir_centre4, radius, color1, thickness)
image = cv2.circle(image, cir_centre5, radius, color1, thickness)
image = cv2.circle(image, cir_centre6, radius, color1, thickness)

# Draw the star by connecting points
cv2.line(image, (200, 10), (210, 50), color1, 2)
cv2.line(image, (210, 50), (170, 25), color1, 2)  
cv2.line(image, (170, 25), (220, 25), color1, 2)  
cv2.line(image, (220, 25), (175, 50), color1, 2)  
cv2.line(image, (175, 50), (200, 10), color1, 2) 

font = cv2.FONT_HERSHEY_SCRIPT_COMPLEX
org = (50, 50)
fontScale = 1
color = (11, 134, 184)
thickness = 2
image = cv2.putText(image, 'Welcome', org, font, fontScale, color, thickness, cv2.LINE_AA)

window_name = "New_Creation"

cv2.imshow(window_name, image)
cv2.waitKey(0)
cv2.destroyAllWindows()
