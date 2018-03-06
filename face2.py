import httplib, urllib, base64
import cv2
import numpy as np
import json
import sys

headers = {
    # Request headers
    'Content-Type': 'application/octet-stream',
    'Ocp-Apim-Subscription-Key': '8569ea97c29540bdbfe196b66aeb02ae',
}

params = urllib.urlencode({
    # Request parameters
    'analyzesFaceLandmarks': 'false',
    'analyzesAge': 'true',
    'analyzesGender': 'true',
    'analyzesHeadPose': 'false',
})

def display_expression(data,img):
    font = cv2.FONT_HERSHEY_PLAIN
    font_size = 2

    data = json.loads(data)
    for face in data:
        f_rec  =  face['faceRectangle']
        width  =  f_rec['width']
        height =  f_rec['height']
        left   =  f_rec['left']
        top    =  f_rec['top']
        cv2.rectangle(img,(left,top),(left+width,top+height),(0,200,0),2)

        f_attr = face['attributes']
        gender = f_attr['gender']
        age = f_attr['age']
        cv2.putText(img, gender, (left, 30+top+height), font, font_size, (0, 200, 0), 2)
        cv2.putText(img, str(age), (left, 60+top+height), font, font_size, (0, 200, 0), 2)



if __name__ == '__main__':
    if len(sys.argv) < 1:
        quit()
    file_path = sys.argv[0]
    conn = httplib.HTTPSConnection('api.projectoxford.ai')
    conn.request("POST", "/face/v0/detections?%s" % params, open(file_path, 'rb'), headers)
    response = conn.getresponse()
    data = response.read()

    print(data)

    img = cv2.imread(file_path)
    display_expression(data, img)

    cv2.imshow('image',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    conn.close()
