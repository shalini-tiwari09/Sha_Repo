import cv2, sys, numpy, os
haar_file = 'C:\\Users\\shaln\\python\\Python\\OPEN_CV\\LESSON_8\\haarcascade_frontalface_default.xml'

datasets = 'C:\\Users\\shaln\\python\\Python\\OPEN_CV\\LESSON_8\\datasets' 
 
# These are sub data sets of folder to store the image
sub_data = 'C:\\Users\\shaln\\python\\Python\\OPEN_CV\\LESSON_8\\shalini'    
 
path = os.path.join(datasets, sub_data)
if not os.path.isdir(path):
    os.mkdir(path)
 
# defining the size of images
(width, height) = (530, 500)   
 
face_cascade = cv2.CascadeClassifier(haar_file)
webcam = cv2.VideoCapture(0)
 
# The program loops until it has captured 30 faces in total
total_faces_saved = 0
max_faces_to_save = 30  # we can Change this to desired number of face to captures

while total_faces_saved < max_faces_to_save:
    (_, im) = webcam.read()
    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 4)
    
    # Loop through all detected faces
    for i, (x, y, w, h) in enumerate(faces):
        cv2.rectangle(im, (x, y), (x + w, y + h), (255, 0, 0), 2)
        face = gray[y:y + h, x:x + w]
        face_resize = cv2.resize(face, (width, height))
        
        filename = f'{path}/face_{total_faces_saved + 1}_person{i + 1}.png'
        cv2.imwrite(filename, face_resize)
        total_faces_saved += 1
        
        # Stop if we reach the maximum number of face captures
        if total_faces_saved >= max_faces_to_save:
            break
        
    cv2.imshow('OpenCV', im)
    key = cv2.waitKey(10)
    if key == 27:
        break
    
webcam.release()