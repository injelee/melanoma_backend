from flask import Flask, request, make_response, json
from find_melanoma import Melanoma
import base64

app = Flask(__name__)


@app.route("/patient_classification", methods=['POST'])
def patient_prediction():
    data = request.json
    for k in data.keys():
        encodeimage = data[k]
        image_string = base64.b64decode(encodeimage)
        image_result = open('{}+decode_image.jpg'.format(k), 'wb')
        image_result.write(image_string)
        #prediction = Melanoma(image=image_result)

        #store the <id, prediction> into MongoDB
    print('Hello!')


@app.route("/image_result", methods=['GET'])
def patient_result():
    if request.method == 'GET':
        response = make_response('image1decode_image.jpg')  # get image
        response.headers['Content-Type'] = 'image/jpeg'
        response.headers['Content-Disposition'] = 'attachment; filename = img.jpg'
        response.headers['Classification result'] = prediction
        return response



