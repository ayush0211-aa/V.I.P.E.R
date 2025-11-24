import cv2
import os
import numpy as np
SAVE_DIR = "saved_faces"
os.makedirs(SAVE_DIR, exist_ok=True)
recognizer = cv2.face.LBPHFaceRecognizer_create()
labels = []
faces = []
person_id = 0
trained = False
cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    face_rects = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in face_rects:
        face = gray[y:y+h, x:x+w]
        if trained:
            label, confidence = recognizer.predict(face)
            if confidence > 60:
                person_id += 1
                faces.append(face)
                labels.append(person_id)
                recognizer.train(faces, np.array(labels))

                cv2.imwrite(f"{SAVE_DIR}/person_{person_id}.jpg", frame[y:y+h, x:x+w])
                print("Saved new person:", person_id)
        else:
            person_id += 1
            faces.append(face)
            labels.append(person_id)
            recognizer.train(faces, np.array(labels))
            trained = True
            cv2.imwrite(f"{SAVE_DIR}/person_{person_id}.jpg", frame[y:y+h, x:x+w])
            print("Saved person 1")
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0,255,0), 2)
    cv2.imshow("Camera - Press Q to Quit", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()