import cv2
import numpy as np

def draw_rectangles(image_path, annotation_path):
    # Load the image
    image = cv2.imread(image_path)
    height, width, _ = image.shape

    # Read the annotation file
    with open(annotation_path, 'r') as file:
        lines = file.readlines()

    for line in lines:
        data = line.strip().split()
        class_id = int(data[0])
        x, y, w, h = map(float, data[1:])
        
        # Convert center coordinates and box size to pixel values
        x = int(x * width)
        y = int(y * height)
        w = int(w * width)
        h = int(h * height)
        
        # Calculate top-left and bottom-right coordinates of the rectangle
        x1, y1 = int(x - w / 2), int(y - h / 2)
        x2, y2 = int(x + w / 2), int(y + h / 2)
        
        # Draw the rectangle on the image
        cv2.rectangle(image, (x1, y1), (x2, y2), (255, 0, 0), 2)

    # Display the image with rectangles
    cv2.imshow('Image with Rectangles', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Path to the image file
image_path = 'datasets\\yolo\\images\\00000.png'

# Path to the YOLO annotation file
annotation_path = 'datasets\\yolo\\labels\\00000.txt'

# Call the function to draw rectangles
draw_rectangles(image_path, annotation_path)
