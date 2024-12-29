import os
import cv2
from PIL import Image 

os.chdir("C:\\temp\\images")
path = "C:\\temp\\images"

mean_height = 0
mean_width = 0

num_of_images = len(os.listdir('.'))  # Count the number of images

# Calculate the mean dimensions of all images
for file in os.listdir('.'):
    img = Image.open(os.path.join(path, file))
    width, height = img.size
    mean_width = mean_width + width
    mean_height = mean_height + height

mean_width = mean_width // num_of_images
mean_height = mean_height // num_of_images

print("Mean Width:", mean_width)
print("Mean Height:", mean_height)

# Resize the images to the mean dimensions
for file in os.listdir('.'):
    if file.endswith('.jpg') or file.endswith('.jpeg') or file.endswith('.png'):
        img = Image.open(os.path.join(path, file))
        width, height = img.size
        print("Original Dimensions:", width, height)

        # Use Image.Resampling.LANCZOS instead of Image.ANTIALIAS
        imgResized = img.resize((mean_width, mean_height), Image.Resampling.LANCZOS)
        imgResized.save(file, 'PNG', quality=95)
        print(img.filename.split('\\')[-1], "is resized")

# Function to generate a video from the resized images
def videoGenerator():
    video_name = "MyFirstVideo.avi"

    os.chdir('C:\\temp\\images')

    images = []
    for img in os.listdir('.'):
        if img.endswith('.jpg') or img.endswith('.jpeg') or img.endswith('.png'):
            images.append(img)
    
    # Array images should only consider the image files ignoring others if any
    print("Images to be included in the video:", images)
    
    frame = cv2.imread(os.path.join(".", images[0]))
    # Setting the frame width, height to the width, height of the first image
    height, width, layers = frame.shape
    video = cv2.VideoWriter(video_name, 0, 1, (width, height))

    # Appending the images to the video one by one
    for image in images:
        video.write(cv2.imread(os.path.join(".", image)))

    cv2.destroyAllWindows()
    video.release()

# Generate the video
videoGenerator()
