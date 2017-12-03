from flask import Flask, request, make_response
import base64

app = Flask(__name__)


def send_error(message, code):
    """

    :param message:
    :param code:
    :return:
    """
    err = {
        "error": message
    }
    return err, code


@app.route("/image_classified_result", methods=['GET', 'POST'])
def image_classified_result():
    if request.method == 'POST':
       data = request.form  # base64 format data from RPi

    try:
        isinstance(data, base64)
    except TypeError:
        return send_error("The input is not in base64 format", 400)

    try:
        len(data) > 0 # the input image is not empty
    except ValueError:
        return send_error("The input is empty", 400)

        image_string = base64.decodebytes(data)
        image_result = open('decode_image.jpg', 'wb')
        image_result.write(image_string)
    #inje's class which has tensorflow
        classification  =

    if request.method == 'GET':
        response = make_response(image_result) # get image
        response.headers['Content-Type'] ='image/jpeg'
        response.headers['Content-Disposition'] = 'attachment; filename = img.jpg'
        response.headers['Classification result'] = classification
        return response


