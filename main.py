from flask import Flask, request, render_template, jsonify
from cd import detect_colors

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_image():
    # Retrieve the uploaded image file
    image_file = request.files['image']

    # Perform color detection on the image and get the detected colors in JSON format
    detected_colors = detect_colors(image_file)

    # Return the detected colors as JSON response
    return detected_colors



if __name__ == '__main__':
    app.run(debug=True)
