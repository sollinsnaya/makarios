from flask import render_template, Flask, jsonify
from kritis import app

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/get_data')
def get_data():
    data_from_python = {'message': 'Hello from Python!'}
    return jsonify(data_from_python)


