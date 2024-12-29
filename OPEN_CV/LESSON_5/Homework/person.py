import cv2
import numpy as np

# Load the uploaded image
image = cv2.imread('people.png', cv2.IMREAD_COLOR)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Gaussian blur to reduce noise
gray_blurred = cv2.GaussianBlur(gray, (15, 15), 0)

# Use HoughCircles to detect circles
detected_circles = cv2.HoughCircles(
    gray_blurred,
    cv2.HOUGH_GRADIENT,
    dp=1.2,
    minDist=50,
    param1=50,
    param2=30,
    minRadius=50,
    maxRadius=80
)

# If circles are detected, draw them
if detected_circles is not None:
    detected_circles = np.uint16(np.around(detected_circles))
    num_circles = len(detected_circles[0])
    for circle in detected_circles[0, :]:
        x, y, r = circle
        # Draw the circle outline
        cv2.circle(image, (x, y), r, (0, 255, 0), 3)
        # Draw the circle center
        cv2.circle(image, (x, y), 2, (0, 0, 255), 3)
 
text = "Number of Circular People in this image : " + str(num_circles)
cv2.putText(image, text, (20, 540), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 128, 128), 2)
        
# Display the result
cv2.imshow("Detected Circles", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
