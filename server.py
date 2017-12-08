from flask import Flask, request, make_response, json
from find_melanoma import Melanoma
import base64

app = Flask(__name__)


@app.route("/patient_classification", methods=['POST'])
def patient_prediction(base64image, filename):
    #for key in data.keys():
        #for value in data.getlist(key):
    #data = request.json
    #for k in data.keys():
    #    encodeimage = data[k]
    #    image_string = base64.decodestring(encodeimage)
     #   image_result = open('{}+decode_image.jpg'.format(k), 'wb')

     #   image_result.write(image_string)
      #  prediction = Melanoma(image=image_result)

        #store the <id, prediction> into MongoDB

    #eturn prediction
     with open(filename, “wb”) as image_out:
        image_out.write(base64.b64decode(base64image))

    prediction = Melanoma(image = image_out)
    return prediction

@app.route("/image_result", methods=['GET'])
def patient_result():
    if request.method == 'GET':
        response = make_response('image1decode_image.jpg')  # get image
        response.headers['Content-Type'] = 'image/jpeg'
        response.headers['Content-Disposition'] = 'attachment; filename = img.jpg'
        response.headers['Classification result'] = prediction
        return response

def encode_image_string(filename):
    with open(filename, “rb”) as image_file:
        image_string = base64.b64encode(image_file.read())
        return image_string

def save_image_string(base64image, filename):
    with open(filename, “wb”) as image_out:
        image_out.write(base64.b64decode(base64image))


if __name__ == ‘__main__‘:
    encoded_image = encode_image_string(“pup.jpg”)
    print(encoded_image)
    save_image_string(encoded_image, “pupper_new.jpg”)


