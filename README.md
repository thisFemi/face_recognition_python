# face_recognition_python
A Facial Recognition backend model that accepts imgs in (url). Deployed to heroku and can be used accessed as a RESTFUl Api


Introduction
This project is a simple face recognition backend built using Flask, a Python web framework. It uses the face_recognition library to compare faces and determine whether they match. The backend exposes an API endpoint for face recognition through a POST request.

Setup
Install the required Python packages:
pip install Flask face_recognition

Run the Flask application:
python app.py

The application will start at http://localhost:5000.

API Endpoint
Endpoint: /recognize

Method: POST

Request Format:
{
  "url1": "URL of the first image",
  "url2": "URL of the second image"
}

Response Format:
{
  "status": true,
  "message": "Recognition successful/unsuccessful",
  "data": 0,  // 0 for no face detected, 1 for unsuccessful recognition, 2 for successful recognition
}

A Working example can be checked here:
https://github.com/thisFemi/face_recognition_app

Feel free to contact me for any further assistance
