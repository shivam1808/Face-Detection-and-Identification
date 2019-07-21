import numpy as np
import cv2
import pickle

face_cascade = cv2.CascadeClassifier('cascades/data/haarcascade_frontalface_alt2.xml')
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("trainer.yml")

labels = {"person_name": 1}
with open("labels.pickle", "rb") as f:
     og_labels = pickle.load(f)
     labels = {v:k for k,v in og_labels.items()}

cap = cv2.VideoCapture(0)

def detect_face(img):
    face_img = img.copy()
    gray = cv2.cvtColor(face_img, cv2.COLOR_BGR2GRAY)
    face_rects = face_cascade.detectMultiScale(face_img,scaleFactor=1.2, minNeighbors=10)
    for (x,y,w,h) in face_rects:
        print(x,y,w,h)
        cv2.rectangle(face_img, (x,y), (x+w,y+h), (255,255,255), 5)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = face_img[y:y+h, x:x+w]

        id_, conf = recognizer.predict(roi_gray)
        if conf>=45 and conf<=85:
            print(id_)
            print(labels[id_])
            font = cv2.FONT_HERSHEY_PLAIN
            name = labels[id_]
            cv2.putText(face_img, name, (x, y-20), font, 1.5, (255, 255, 255), 2, cv2.LINE_AA)
        else:
            cv2.rectangle(face_img, (x, y), (x + w, y + h), (0, 0, 255), 5)
        img_item = "new.png"
        cv2.imwrite(img_item, roi_color)
    return face_img



while True:
     ret, frame = cap.read(0)
     frame = detect_face(frame)
     cv2.imshow('Video Face Detection', frame)

     c = cv2.waitKey(1)
     if c == 27:
         break

cap.release()
cv2.destroyAllWindows()
