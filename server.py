from flask import Flask, request, make_response, json
import base64

app = Flask(__name__)


@app.route("/image_classified_result", methods=['GET', 'POST'])
def image_classified_result():
    if request.method == 'POST':
        data = request.json

        for k in data.keys():
            encodeimage = data[k]
            image_string = base64.decodestring(encodeimage)
            image_result = open(data.keys[k]+'decode_image.jpg', 'wb')
            image_result.write(image_string)


    # inje's class which has tensorflow
        # classification  = get_prediction(image_result)

    if request.method == 'GET':
        response = make_response('image1decode_image.jpg')  # get image
        response.headers['Content-Type'] = 'image/jpeg'
        response.headers['Content-Disposition'] = 'attachment; filename = img.jpg'

        #response.headers['Classification result'] = classification
        return response


