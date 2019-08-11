# https://stackoverflow.com/questions/43469281/how-to-predict-input-image-using-trained-model-in-keras

from keras.applications.imagenet_utils import preprocess_input, decode_predictions
import keras

from keras.models import load_model
from keras.preprocessing import image
#from keras.applications.imagenet_utils import decode_predictions
import matplotlib.pyplot as plt
import numpy as np
import os


# model = SqueezeNet()
# img = image.load_img('images/cat.jpeg', target_size=(227, 227))
# x = image.img_to_array(img)
# x = np.expand_dims(x, axis=0)
# x = preprocess_input(x)
# preds = model.predict(x)
# decoded_preds = decode_predictions(preds)

def load_image(img_path, show=False):
    keras.backend.set_image_dim_ordering('tf')
    img = image.load_img(img_path, target_size=(224, 224))
    img_tensor = image.img_to_array(img)                    # (height, width, channels)
    img_tensor = np.expand_dims(img_tensor, axis=0)         # (1, height, width, channels), add a dimension because the model expects this shape: (batch_size, height, width, channels)
    #img_tensor /= 255.                                      # imshow expects values in the range [0, 1]
    img_tensor = preprocess_input(img_tensor)

    if show:
        plt.imshow(img_tensor[0])
        plt.axis('off')
        plt.show()

    return img_tensor


train_dir = './clean-dataset/train'
validation_dir = './clean-dataset/validation'
image_size = 224
model = load_model('all_freezed.h5')

# print(model.get_config())

validation_pumpkin_dir = validation_dir + '/pumpkin'
validation_pumpkin_images = os.listdir(validation_pumpkin_dir)
validation_tomato_dir = validation_dir + '/tomato'
validation_tomato_images = os.listdir(validation_tomato_dir)
validation_watermelon_dir = validation_dir + '/watermelon'
validation_watermelon_images = os.listdir(validation_watermelon_dir)


def my_predict(img_path):
    #print(img_path)
    # load a single image
    new_image = load_image(img_path)
    # check prediction
    preds = model.predict(new_image)
    #print(preds)

    pred_probas = model.predict_proba(new_image)
    pred_classes = model.predict_classes(new_image)
    print(preds, pred_probas, pred_classes)


pumpkin0 = validation_pumpkin_dir + '/' + validation_pumpkin_images[0]
tomato0 = validation_tomato_dir + '/' + validation_tomato_images[0]
watermelon0 = validation_watermelon_dir + '/' + validation_watermelon_images[0]

my_predict(pumpkin0)
my_predict(tomato0)
my_predict(watermelon0)

print('=================pumpkin')
for i in range(len(validation_pumpkin_images)):
    pumpkin = validation_pumpkin_dir + '/' + validation_pumpkin_images[i]
    my_predict(pumpkin)

print('=================tomato')
for i in range(len(validation_tomato_images)):
    tomato = validation_tomato_dir + '/' + validation_tomato_images[i]
    my_predict(tomato)

print('=================watermelon')
for i in range(len(validation_watermelon_images)):
    watermelon = validation_watermelon_dir + '/' + validation_watermelon_images[i]
    my_predict(watermelon)

# # load a single image
# new_image = load_image(tomato0)
#
# # check prediction
# preds = model.predict(new_image)
# print(preds)
#
# predict_classes = model.predict_classes(new_image)
# print(predict_classes)

# y_classes = preds.argmax(axis=-1)
# print(y_classes)

# https://stackoverflow.com/questions/49259361/valueerror-decode-predictions-expects-a-batch-of-predictions-i-e-a-2d-array
# decoded_preds = decode_predictions(preds)
# print(decoded_preds)

# (class_name, class_description, score) = decode_predictions(pred)[0]
# print(class_name, class_description, score)