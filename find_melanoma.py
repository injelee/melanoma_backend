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
        if self.predictions[0] > self.predictions[1]:
            prediction = 'non_malignant'
            marker = 0
            probability = float(self.predictions[0])
        else:
            prediction = 'malignant'
            marker = 1
            probability = float(self.predictions[1])
        prediction_dict = {'Prediction': prediction,
                           'Probability': probability}
        print("\n\nPredictions:")
        print(prediction_dict)
        if marker is 0:
            print('Our classifier thinks you do not have melanoma.')
        else:
            print('Our classifier thinks you have melanoma.')
        return prediction_dict
