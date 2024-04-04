from flask import render_template, Flask, jsonify, request
from kritis import app

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/get_data')
def get_data():
    data_from_python = {'message': 'Hello from Python!'}
    return jsonify(data_from_python)

@app.route('/uploadImage', methods=['POST'])
def upload_image():
    # Check if the POST request has the file part
    if 'image' not in request.files:
        return 'No file part', 400

    uploaded_image = request.files['image']

    # Save the uploaded image
    uploaded_image.save('/Users/sdennis/Desktop/Makarios/images/uploaded_image.jpg')  # Change the filename as needed

    return 'Image uploaded successfully'
