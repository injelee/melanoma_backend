# bme590 Final Project: Melanoma_Detection
The Melanoma project aims to develop a system that takes in images of skin lesions as inputs, and outputs the likelihood that the lesion is malignant, in order to facilitate early diagnosis of melanoma. We use a Raspberry Pi to access images via USB. The images then is sent to the web service to undergo a trained classifier function which compute the likelihood that the lesion is malignant and return this percentage to the user. The image/patient ID and the prediction results are also stored in a database which can be accessed later.

Running method
===============
The main file to run is called "main.py", the input is the images from usb and the output is the prediction value, which is 
posted on the web server.

If no image is stored in usb, there will be an error message returned to the raspberry pi (We hope to trigger a LED light on raspberry pi if this happens.)

License
==============
We choose to use Apache License, Version 2.0 for our project's license. Because this license provides an express grant of patent rights
from contributors to users.

Documentation
==============
The latest documentation is automatically generated using Sphinx and can be found through the link below:



Contributors
============
Jing-Rui Li (jl714@duke.edu)
Inje Lee (inje.lee@duke.edu)
Niranjana Shashikumar (ns229@duke.edu)
