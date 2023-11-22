from flask import Flask, render_template, jsonify, request
import face_recognition
from io import BytesIO
import json
import requests

app = Flask(__name__)

# Load your image from a URL
def load_image_from_url(url):
    response = requests.get(url)
    img = face_recognition.load_image_file(BytesIO(response.content))
    return img

# Encode a face from an image
def encode_face(image):
    face_encoding = face_recognition.face_encodings(image)
    if len(face_encoding) > 0:
        return face_encoding[0]
    else:
        return None

@app.route('/')
def index():
    return '<h1>Welcome to Attend Sense</h1>'

@app.route('/recognize', methods=['POST'])
def recognize():
    try:
        data = request.json
        url1 = data.get("url1")
        url2 = data.get("url2")

        if url1 is not None and url2 is not None:
            # Load images from URLs
            image1 = load_image_from_url(url1)
            image2 = load_image_from_url(url2)

            # Encode faces
            encoding1 = encode_face(image1)
            encoding2 = encode_face(image2)

            if encoding1 is not None and encoding2 is not None:
                # Compare face encodings
                results = face_recognition.compare_faces([encoding1], encoding2)

                if results[0] == True:
                    response = {"status": True, "message": "Recognition successful", "data": 2}
                else:
                    response = {"status": True, "message": "Recognition unsuccessful", "data": 1}
            else:
                response = {"status": True, "message": "No face detected in one or both images", "data": 0}
        else:
            response = {"status": False, "message": "Invalid request format"}

        return jsonify(response)
    except json.JSONDecodeError:
        return jsonify({"status": False, "message": "Invalid JSON format"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))