from get_prediction import get_prediction
import matplotlib
import matplotlib.image as mpimg
import numpy as np
import matplotlib.pyplot as plt
from pymodm import connect
from pymodm import MongoModel, fields
from flask import Flask, request, jsonify
matplotlib.use('Agg')


class Melanoma:

    """
    This class takes image inputs and detects whether or not the image
    is a healthy cell or indicative of melanoma, with probability
    outputs.
    :return: The prediction information and classification
    :rtype: dict
    """

    def __init__(self, image='/images/malignant/ISIC_0011285.jpg'):
        self.image = image
        self.labels = []
        self.predictions = []

    def use_tf(self):
        img_read = mpimg.imread(self.image)
        image = np.array(img_read)
        # Want to remove 4th layer in PNG files w/ transparency layers
        if image.shape[2] > 3:
            img = image[..., :3].shape
        else:
            img = img_read
        (self.labels, self.predictions) = get_prediction(img)
        print("\n\nPredictions:")
        print(self.labels)
        print(self.predictions)
        if self.predictions[0] > self.predictions[1]:
            prediction = 'non_malignant'
            probability = float(self.predictions[0])
        else:
            prediction = 'malignant'
            probability = float(self.predictions[1])
        prediction_dict = {'Prediction': prediction,
                           'Probability': probability}
        return prediction_dict
