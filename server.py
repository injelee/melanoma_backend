from flask import Flask, request, make_response, redirect, url_for
import base64

ALLOWED_EXTENTIONS = set(['txt'])

app = Flask(__name__)

def allowed_file(filename):
    return '.' in filename and \
filename.rsplt('.', 1)[1].lower in ALLOWED_EXTENTIONS

@app.route("/image_classified_result", methods=['GET', 'POST'])
def image_classified_result():
    if request.method == 'POST':
      if 'file' not in request.files:
          flash('No file part')
        return redirect(request.url)

      if file.filename == '':
          flash('No selected file')
        return redirect(request.url)
    if file and allowed_filename(file.filename):
       for file in request.files:
           data = request.files['file']
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


