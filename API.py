from flask import Flask, request, Response
from utils.model import load_model

import cv2
import numpy as np
import tensorflow as tf
import json
import os
import argparse
from datetime import datetime

from PIL import Image

app = Flask(__name__)

@app.route("/api/v1/classify", methods=["POST"])
def detect():
    # Get current request time
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")

    # Load multipart/form-data
    # Get Request data
    f = request.files['image']

    # Convert to JPG, resize, and normalization
    img = Image.open(f)
    img = img.convert("RGB")
    img = np.array(img)
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    img = cv2.resize(img, (160, 160))
    img = np.expand_dims(img, axis=0)
    img = img/.255

    # predict
    prediction = model.predict(img)[0]
    prediction = prediction.tolist()
    confidence = max(prediction) * 100
    prediction = prediction.index(max(prediction))

    # Get Disease name
    disease_name = ''
    for key in labels_map.keys():
        if labels_map[key]['label'] == prediction:
            disease_name = key

    if disease_name == 'dermatofibroma' or disease_name == 'melanocytic nevus':
        isDanger = False
    elif disease_name == 'melanoma' or disease_name == 'basal cell carcinoma' or disease_name == 'actinic keratosis' or disease_name == 'vascular lesions':
        isDanger = True

    # Packing JSON
    response = {
        "status":"success",
        "requestAt":current_time,
        "message":"classification succesful",
        "is_danger":isDanger,
        "disease":{
            "disease_name":disease_name,
            "confidence":confidence
        }   
    }

    serialized_dict = json.dumps(response, ensure_ascii=False).encode('utf8')
    return Response(serialized_dict, mimetype='application/json')
    

if __name__ == "__main__": 
    parser = argparse.ArgumentParser(description="API yolov4 for Japanese Character Recognition")
    parser.add_argument("--port", default=5000, type=int, help="port number to start")
    args = parser.parse_args()

    # Load model
    model = load_model('utils/demo_weight.h5')

    # Load label
    f = open("utils/label_encode.json")
    labels_map = json.load(f)
    f.close()

    # Run Api
    port = int(os.environ.get('PORT', 6000))
    app.run(host='0.0.0.0', port=port,debug=False)
