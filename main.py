import csv
import cv2
import os
import numpy as np
from datetime import datetime
import time
input_folder="images"
different_people="Different_people"
csv_file="Target_seen"
if os.path.exists(different_people)==False:
    os.makedirs(different_people)
proto_path = "models/deploy.prototxt.txt"
model_path = "models/res10_300x300_ssd_iter_140000.caffemodel"
net=cv2.dnn.readNetFromCaffe(proto_path,model_path)
face_match=cv2.face.LBPHFaceRecognizer_create()
print("[INFO] Learning from your photos...")
faces=[]
ids=[]
names={}
files=os.listdir(input_folder)
current_id=0
for filename in files:
    if filename.endswith(".jpg") or filename.endswith(".png") or filename.endswith(".jpeg"):
        path=os.path.join(input_folder,filename)
        img=cv2.imread(path)
        name=os.path.splitext(filename)[0]
        face_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        current_id+=1
        faces.append(face_gray)
        ids.append(current_id)
        names[current_id]=name
        print(f" - Learned:{name}")
face_match.train(faces,np.array(ids))
print("Training complete... setting up Camera")
cap=cv2.VideoCapture(0)
last_save_t=time.time()
while True:
    ret, frame = cap.read()
    if not ret: break
    (h, w) = frame.shape[:2]
    blob = cv2.dnn.blobFromImage(cv2.resize(frame, (300, 300)), 1.0, (300, 300), (104.0, 177.0, 123.0))
    net.setInput(blob)
    detections = net.forward()
    for i in range(detections.shape[2]):
        con = detections[0, 0, i, 2]
        if con > 0.35:
            box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
            (xi, yi, xf, yf) = box.astype("int")
            (fw,fh)=((xf-xi),(yf-yi))
            dim=max(fw,fh)
            p=int(dim*0.3)
            l=dim+p
            (cx,cy)=(xi+fw//2,yi+fh//2)
            (nx,ny)=(max(0,cx-(l//2)),max(0,cy-(l//2)))
            (nxf,nyf)=(min(w,cx+(l//2)),min(h,cy+(l//2)))
            cv2.rectangle(frame,(nx,ny),(nxf,nyf),(255,0,0),2)
            face_crop = frame[ny:nyf, nx:nxf]
            if face_crop.size == 0:
                continue
            if time.time() - last_save_t > 3:
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                save_path = os.path.join(different_people, f"person_{timestamp}.jpg")
                cv2.imwrite(save_path, frame)
                print(f"[SNAPSHOT] Saved person to {save_path}")
                last_save_t = time.time()
            face_gray = cv2.cvtColor(face_crop, cv2.COLOR_BGR2GRAY)     
            try:
                id, conf = face_match.predict(face_gray)
                if conf < 50:
                    name = names[id]
                    cv2.rectangle(frame, (xi,yi), (xf,yf), (0, 255, 0), 2)
                    cv2.putText(frame, f"FOUND: {name}", (xi,yi - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
                    now=datetime.now()
                    with open(csv_file, 'a', newline='') as f:
                        writer = csv.writer(f)
                        writer.writerow([name, now.strftime("%Y-%m-%d"), now.strftime("%H:%M:%S")])
                        print(f"[MATCH] Logged {name} into CSV.")
                else:
                    cv2.rectangle(frame, (xi,yi), (xf,yf), (0, 0, 255), 2)
                    cv2.putText(frame, "Unknown", (xi,yi - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)
            except Exception as e:
                pass
    cv2.imshow("Security Camera", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
