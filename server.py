from flask import Flask, request, make_response, json
from find_melanoma import Melanoma
import base64

app = Flask(__name__)


@app.route("/image_classified_result", methods=['GET', 'POST'])
def image_classified_result():
    if request.method == 'POST':
        data = request.form

    for key in data.keys():
        for value in data.getlist(key):
            encodeimage = value
            image_string = base64.decodestring(encodeimage)
            image_result = open(key+'decode_image.jpg', 'wb')
            image_result.write(image_string)


    # inje's class which has tensorflow
        prediction = Melanoma(image=image_result)

    if request.method == 'GET':
        response = make_response('image1decode_image.jpg')  # get image
        response.headers['Content-Type'] = 'image/jpeg'
        response.headers['Content-Disposition'] = 'attachment; filename = img.jpg'
        response.headers['Classification result'] = prediction
        return response


