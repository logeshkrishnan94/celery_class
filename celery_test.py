import cv2
import base64
import json
import time
import os
from celery import group
from celery_proj.celery_app import predict_task


img_ls = []
img_loc = "Data"
for filename in os.listdir(img_loc):
    if filename.endswith(".jpg"):
        img_ls.append(filename)
    
def json_encode(img):
    full_p = os.path.join(img_loc, img)
    img = cv2.imread(full_p)
    _, im_arr = cv2.imencode('.jpg', img)
    im_bytes = im_arr.tobytes()
    base_img = base64.b64encode(im_bytes).decode('utf-8')
    return base_img

predict_result = group(predict_task.s(json_encode(i), (180, 180)) for i in img_ls)()
res = predict_result.get()

for i in res:
    print(i)