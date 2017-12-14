from flask import Flask, request, make_response, jsonify
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


def send_error(message, code):
    """
    This module will be used to throw HTTPS server error codes and
    messages when we specify them.
    :param message: Output that user will see
    :param code: HTTPS server error code
    :return: jsonified version of message and code
    """
    err = {
        "error": message
    }
    return jsonify(err), code


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
    from find_melanoma import Melanoma
    import base64

    data = request.json

    try:
        isinstance(data, dict) is True
    except TypeError:
        return send_error("Input was not of type=dictionary.", 400)

    prediction_result = {}
    for k in data.keys():
        # Encoding base64 string to image and saving
        encodeimage = data[k]
        image_string = base64.b64decode(encodeimage)
        # Leave image open for processing
        image_result = open('{}_decode_image.jpg'.format(k), 'w+')
        image_result.write(image_string)

        # Using tf classifier to return id and prediction
        run_script = Melanoma(image=image_result)
        prediction = run_script.use_tf()
        image_result.close()

        # Storing data in Mongo (WIP)
        new_key = '{}_prediction'.format(k)
        new_prediction = prediction
        prediction_result[new_key] = new_prediction
        patient_classification = get_patient_class(patient_id=data.keys,
                                                   prediction=new_prediction)
        # patient_classification.save()
        return jsonify(prediction_result)


# WORK IN PROGRESS
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
