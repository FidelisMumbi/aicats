from django.db import models

# Create your models here.
# ai_app/models.py
from tensorflow import keras

class ImageClassifier(keras.Model):
    # Define your image classification model architecture here
    def __init__(self):
        # ...
        super(ImageClassifier, self).__init__()


