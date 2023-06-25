import cv2
import numpy as np
import json
from webcolors import rgb_to_name

# Load image
def detect_colors(img):
    img_path = 'image1.jpg'
    img = cv2.imread(img_path)

    # Reshape image to a list of pixels
    pixels = img.reshape(-1, 3).astype(np.float32)

    # Apply K-means clustering to identify dominant colors
    num_colors = 10
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.2)
    _, labels, centers = cv2.kmeans(pixels, num_colors, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)

    # Convert the RGB color values to integers
    centers = np.uint8(centers)

    # Get the counts of each color cluster
    color_counts = np.bincount(labels.flatten())

    # Sort colors by count in descending order
    sorted_indices = np.argsort(color_counts)[::-1]
    sorted_centers = centers[sorted_indices]

    # Create a list of detected colors
    detected_colors = []
    for color in sorted_centers:
        r, g, b = color.tolist()
        try:
            named_color = rgb_to_name((int(r), int(g), int(b)), spec='css3')
        except ValueError:
            named_color = "N/A"
            color_info = {
                'color_name': named_color,
                'R': int(r),
                'G': int(g),
                'B': int(b)
            }
            detected_colors.append(color_info)
        

    # Convert the list of detected colors to JSON format
    json_data = json.dumps(detected_colors)

    # Display the JSON data
    return json_data
