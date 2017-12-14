from gcr.io/tensorflow/tensorflow:latest
RUN pip install Flask
RUN apt-get update
RUN apt-get install python-tk -y
RUN pip install pymodm
ENV FLASK_APP=main.py
