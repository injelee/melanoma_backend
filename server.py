from flask import Flask, request, make_response, json
#from find_melanoma import Melanoma
import base64

app = Flask(__name__)


@app.route("/patient_classification", methods=['POST'])
def patient_prediction():
    data = request.json

    if 'error' not in data.keys():
        #prediction_result = {}
        for k in data.keys():
            encodeimage = data[k]
            image_string = base64.b64decode(encodeimage)
            image_result = open('{}_decode_image.jpg'.format(k), 'wb')
            image_result.write(image_string)
        return 'ok'

        #prediction = Melanoma(image=image_result)

        #store the <id, prediction> into MongoDB

        # Return the id and prediction
        #new_key = '{}_prediction'.format(k)
        #new_prediction = prediction
        #prediction_result[new_key] = new_prediction
    else:
        error_response = data['error']
     #    print('there is no image input.')
        return error_response
    

@app.route("/image_result", methods=['GET'])
def patient_result():
    r = patient_prediction()
    if r:
        return r
    else:
        return 'no error'



