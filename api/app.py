#!/usr/local/bin/python3

# Dependencies
import joblib
import pandas as pd
from flask import Flask, jsonify, request
from PIL import Image
from keras.models import load_model
import keras
from keras.preprocessing import image
from keras.applications.imagenet_utils import preprocess_input, decode_predictions
import numpy as np

# Your API definition
app = Flask(__name__)

@app.route('/image/predict', methods=['POST'])
def predict():
    f = request.files['image']
    im = Image.open(f)
    new_image = load_image(im)
    new_image = preprocess_input(new_image)
    # check prediction
    preds = model.predict(new_image)
    #print(preds)

    pred_probas = model.predict_proba(new_image)
    pred_classes = model.predict_classes(new_image)

    print(pred_classes)

    if pred_classes == 0 :
        object = 'pumpkin'
    elif pred_classes == 1:
        object = 'tomato'
    else:
        object = 'watermelon'
    
    probability = str(pred_probas[:,pred_classes][0][0])

    return jsonify(
        object = object,
        probability = probability
    )

def load_image(img, show=False):
    img_tensor = image.img_to_array(img)                    # (height, width, channels)
    img_tensor = np.expand_dims(img_tensor, axis=0)         # (1, height, width, channels), add a dimension because the model expects this shape: (batch_size, height, width, channels)
    #img_tensor /= 255.                                      # imshow expects values in the range [0, 1]
    img_tensor = preprocess_input(img_tensor)

    return img_tensor

if __name__ == '__main__':
    model = load_model('da_last4_layers.h5')
    model._make_predict_function()
    keras.backend.set_image_dim_ordering('tf')
    app.run(debug=True, host='0.0.0.0')