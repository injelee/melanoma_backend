# Bme590 Final Project: Melanoma_Detection
This Melanoma project aims to develop a system that takes in images of skin lesions as inputs, and outputs the likelihood that the lesion is malignant, in order to facilitate early diagnosis of melanoma. We use a Raspberry Pi to access images via USB. The images then is sent to the web service to undergo a trained classifier function which compute the likelihood that the lesion is malignant and return this percentage to the user. The image/patient ID and the prediction results are also stored in a database which can be accessed later.
Please refer to our final report for more details. 
Report: 
https://docs.google.com/document/d/1SiJ7uANaeKdDCQd2NfZjOofposAL70jx3MNFOODZi_s/edit?usp=sharing

Running method
===============
The main file to run is called "main.py", the input is the images from usb and the output is the prediction value, which is 
posted on the web server. To run this project, run docker-compose up from the root of the repository. This will start up the web service in main.py serving on Duke VM, http://vcm-2117.vm.duke.edu:8000/. You can then edit the files in the repository, and the Flask web server will automatically reload as you make changes during development. If you want to interact with the project in an interactive iPython notebook, you should be able to click on the provided link that should appear when you run docker-compose up.
More information about setting up the raspberry pi can be accessed on our front end repo: 
https://github.com/NinjMenon/bme590_melanoma_rp

http://vcm-2117.vm.duke.edu:8000/ --> This address will yield a short message, the appearance of which confirms that the Docker image has been configured correctly.

http://vcm-2117.vm.duke.edu:8000/patient_classification (POST only) --> Inputs of type JSON dictionary will be accepted, where the user should specify the patient ID as the key. The tf code will process and return the patient ID, along with the prediction and probability of the prediction being accurate according to the classifier.

License
==============
We choose to use Apache License, Version 2.0 for our project's license because this license provides an express grant of patent rights
from contributors to users.


Contributors
============
Jing-Rui Li (jl714@duke.edu)
Inje Lee (inje.lee@duke.edu)
Niranjana Shashikumar (ns229@duke.edu)
