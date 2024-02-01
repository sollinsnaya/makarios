from flask import render_template
from kritis import app

@app.route('/')
@app.route('/index')
def index():
    image = 'im an image'
    return render_template('index.html', title='Home', image=image)