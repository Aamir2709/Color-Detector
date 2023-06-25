# Color-Detector
Urine Colour Detection from Image

This project focuses on detecting urine colours from an image using clustering and OpenCV. The goal is to extract the dominant colours present in the image and represent them in JSON format.

Dependencies

OpenCV
numpy
json

Usage

Provide the path to the input image.
The image is loaded using OpenCV.
Apply clustering to identify the dominant colours.
Extract the RGB values of the clustered colours.
Convert the RGB values to JSON format.
Print the JSON data representing the detected colours.

Algorithm

Load the image using OpenCV.
Reshape the image to a list of pixels.
Apply K-means clustering to identify dominant colours.
Convert the RGB colour values to integers.
Get the counts of each colour cluster.
Sort the colours by count in descending order.
Create a list of detected colours with their RGB values.
Convert the list of detected colours to JSON format.
Print the JSON data representing the detected colours.
![image](https://github.com/Aamir2709/Color-Detector/assets/84448909/9a557e3a-416a-45e6-b908-a752c6fce82f)
