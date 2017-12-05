from get_prediction import get_prediction
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
from pymodm import connect
from pymodm import MongoModel, fields
from flask import Flask, request, jsonify


class Melanoma:

    """
    This class takes image inputs and detects whether or not the image is a healthy cell
    or indicative of melanoma.
    """

    def __init__(self, image='/images/malignant/ISIC_0011285.jpg'):
        self.image = image
        self.labels = []
        self.predictions = []

    def use_tf(self):
        img = mpimg.imread(self.image)
        (self.labels, self.predictions) = get_prediction(img)
        print("\n\nPredictions:")
        print(self.labels)
        print(self.predictions)

    # def store_data(self):



