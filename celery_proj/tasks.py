import cv2
import base64
import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import  models
from celery import Task, Celery

class MLTask(Task):
    """Celery Task for making Model predictions."""

    def __init__(self):
        """ class constructor """
        super().__init__()
        self.model = models.load_model("save_at_1.h5")
    
    def img_predict(self, img_data, img_size):
        img = cv2.resize(img_data, (img_size[0], img_size[1]), interpolation=cv2.INTER_NEAREST)
        img_array = keras.preprocessing.image.img_to_array(img)
        img_array = tf.expand_dims(img_array, 0) 
        predictions = self.model.predict(img_array)
        score = float(predictions[0])
        return score
    
    def json_encode(self, img):
        _, im_arr = cv2.imencode('.png', img, [cv2.IMWRITE_PNG_COMPRESSION , 1])
        im_bytes = im_arr.tobytes()
        base_img = base64.b64encode(im_bytes).decode('utf-8')
        return base_img

    def json_decode(self, img):
        out = base64.b64decode(img)
        nparr = np.fromstring(out, np.uint8)
        img_de = cv2.imdecode(nparr, flags=cv2.IMREAD_COLOR)
        return img_de

    def run(self, data, img_size):
        img_decode = self.json_decode(data)
        predicts = self.img_predict(img_data=img_decode, img_size=img_size)
        return predicts 



