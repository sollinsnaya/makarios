from flask import render_template, Flask, jsonify, request, send_file
from kritis import app
import cv2
import numpy as np
from PIL import Image as im
from io import BytesIO
import base64


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/uploadImage', methods=['POST'])
def upload_image():
    # Check if the POST request has the file part
    if 'image' not in request.files:
        return 'No file part', 400

    uploaded_image = request.files['image']

    # Read the uploaded image into memory
    global uploaded_image_storage
    uploaded_image_storage = BytesIO(uploaded_image.read())
    uploaded_image.seek(0)  # Reset the file pointer

    return 'Image uploaded successfully'


@app.route('/get_data', methods=['POST'])
def get_data():

    global uploaded_image_storage
    if uploaded_image_storage is None:
        return 'No image uploaded', 400

    original_image=uploaded_image_storage.getvalue()

    # Read image data from FileStorage object
    nparr = np.fromstring(original_image, np.uint8)
    image_array = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    #Process the image

    gray = cv2.cvtColor(image_array, cv2.COLOR_RGB2GRAY)
    thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)

    #cv2.imwrite('/Users/sdennis/Desktop/Makarios/images/uploaded_image.jpg',thresh)

    processed_image= im.fromarray(thresh)

    #return processed_image
    # Save the processed image to a BytesIO object
    processed_image_data = BytesIO()
    processed_image.save(processed_image_data, format='JPEG')

    # Convert the processed image data to a base64-encoded string
    processed_image_base64 = base64.b64encode(processed_image_data.getvalue()).decode('utf-8')

    # Return the processed image data as a JSON response
    return jsonify({'processed_image_base64': processed_image_base64})

