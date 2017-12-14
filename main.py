from flask import Flask, request, make_response, jsonify
from find_melanoma import Melanoma
import base64
from pymodm import connect
from pymodm import MongoModel, fields

connect("mongodb://vcm-2117.vm.duke.edu:27017/melanoma_db")
app = Flask(__name__)


@app.route('/')
def hello_world():
    """
    Simple hello world function to test working Docker container.
    :return: Hello World
    :rtype: str
    """
    return 'Hello, world2'


class get_patient_class(MongoModel):
    patient_id = fields.CharField()
    prediction = fields.CharField()
    # actual = fields.CharField() will add


@app.route("/patient_classification", methods=['POST'])
def patient_prediction():
    """
    This posting method will post the image base64 string as a JSON dictionary,
    and will return a dictionary that shows the ID of the image (as dictated
    by the user in the name of the image) and will have the prediction and
    probability of melanoma in the image.
    :return: Prediction results from classifier.
    :rtype: dict
    """
    data = request.json
    prediction_result = {}
    for k in data.keys():
        encodeimage = data[k]
        image_string = base64.b64decode(encodeimage)
        image_result = open('{}_decode_image.jpg'.format(k), 'w+')
        image_result.write(image_string)
        # image_id = k
        run_script = Melanoma(image=image_result)
        prediction = run_script.use_tf()

        # store the <id, prediction> into MongoDB

        # Return the id and prediction
        new_key = '{}_prediction'.format(k)
        new_prediction = prediction
        prediction_result[new_key] = new_prediction
        patient_classification = get_patient_class(patient_id=data.keys,
                                                   prediction=new_prediction)
        # patient_classification.save()
        return jsonify(prediction_result)


@app.route("/image_result/<string:patient_id>", methods=['GET'])
def patient_result(patient_id):
    """
    This module will have allow the user to see the relevant patient data for
    a specific patient ID (e.g. image filename).
    :param patient_id: Name of the patient of interest.
    :return: The patient ID information.
    :rtype: dict
    """
    # response = make_response('image1decode_image.jpg')  # get image
    # response.headers['Content-Type'] = 'image/jpeg'
    # response.headers['Content-Disposition']= 'attachment; filename = img.jpg'
    # response.headers['Classification result'] = prediction
    patient_result = []
    for patients in get_patient_class.objects.raw({'patient_id': patient_id}):
        patient_result.append(float(patients.prediction))
    patient_class = patient_result
    return jsonify(patient_class)
