import time
import cv2
import mss
import numpy
import requests

with mss.mss() as sct:
    monitor = {"top": 0, "left": 0, "width": 1920, "height": 1080}
    url = "http://0.0.0.0:5000/api/v1/places/get_places"
    # url = "http://34.66.27.157/api/v1/places/get_places"

    headers = {
                'content-type': "image/jpeg"
            }


    last_time = time.time()
    i = 0
    # while "Screen capturing":
    #     if time.time() - last_time >= 5:
    # img = numpy.array(sct.grab(monitor))
    img = cv2.imread('test/test.png')
    _, img_encoded = cv2.imencode('.jpg', img)
    response = requests.request("POST", url, data=img_encoded.tostring(),  headers=headers)
    print(response.text)

    last_time = time.time()
    i += 1
