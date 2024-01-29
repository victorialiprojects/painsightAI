# https://www.datacamp.com/tutorial/face-detection-python-opencv
# Has how to get image from live video stream

import cv2
import matplotlib.pyplot as plt

def get_face(image_path):

    img = cv2.imread(image_path)
    gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    face_classifier = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    face = face_classifier.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=5, minSize=(40, 40))
    
    if len(face)>0:
        '''
        for (x, y, w, h) in face:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 4)
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        plt.figure(figsize=(20,10))
        plt.imshow(img_rgb)
        plt.show()
        '''
        return True
        
    else:
        return False