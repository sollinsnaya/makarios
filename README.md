Makarios is a Python application that converts digital images into paint-by-number templates. Paint by Numbers is a form of art where a picture is divided into shapes, each marked with a number that corresponds to a particular color.

Features:

- Upload digital images in various formats.
- Convert uploaded images into paint-by-number templates.
- Download the converted templates for printing and painting.

Installation:

1. - Clone this repository:

bash

~~~
git clone https://github.com/yourusername/paint-by-numbers-converter.git
~~~

Navigate to the project directory:

~~~
cd Makarios
~~~

Install dependencies:

~~~
# optional: install poetry with pip:
pip install poetry

#install dependencies on venv
poetry install
~~~

Run the Flask application:

~~~
make
~~~

Open your web browser and go to http://localhost:5001.

Upload a digital image using the provided interface.

Click the "TransformImage" button to generate the paint-by-number template.

Download the template and start painting!

License
This project is licensed under the MIT License - see the LICENSE file for details.

