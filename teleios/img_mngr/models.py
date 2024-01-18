from django.db import models

# image_upload/models.py
from django.db import models

class UploadImage(models.Model):
    image = models.ImageField(upload_to='images/')
