#this part will open an GUI and allow user to upload photo and name of the person who we are searching for
import os
import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog, messagebox
if os.path.exists("images")==False:
    os.makedirs("images")
proto_path = os.path.join("models", "deploy.prototxt.txt")
model_path = os.path.join("models", "res10_300x300_ssd_iter_140000.caffemodel")
if  os.path.exists(proto_path)==False or os.path.exists(model_path)==False:
    print("ERROR: Model files missing. Please create a 'models' folder.")
else:
    net = cv2.dnn.readNetFromCaffe(proto_path, model_path)
def select():
    path=filedialog.askopenfilename(title="SELECT PHOTOS",filetypes=[("Image files","*.jpg *.jpeg *.png")])
    lbl_path.config(text=path)
def save_data():
    name= entry_name.get()
    source_path=lbl_path.cget("text")
    if name=="" or source_path=="No photo selected":
        messagebox.showwarning("enter a name and select a photo")
        return
    image=cv2.imread(source_path)
    (h,w)=image.shape[:2]
    blob=cv2.dnn.blobFromImage(cv2.resize(image,(300,300)),1.0,(300,300),(104.0,177.0,123.0))
    net.setInput(blob)
    detections=net.forward()
    max_con=0
    best_box=None
    for i in range(0,detections.shape[2]):
        con=detections[0,0,i,2]
        if con >0.65 and con>max_con:
            max_con=con
            box=detections[0,0,i,3:7]*np.array([w,h,w,h])
            best_box=box.astype("int")
    if best_box is not None:
        (xi,yi,xf,yf)=best_box
        (fw,fh)=((xf-xi),(yf-yi))
        dim=max(fw,fh)
        p=int(dim*0.3)
        l=dim+p
        (cx,cy)=(xi+fw//2,yi+fh//2)
        (nx,ny)=(max(0,cx-(l//2)),max(0,cy-(l//2)))
        (nxf,nyf)=(min(w,cx+(l//2)),min(h,cy+(l//2)))
        face_crop=image[ny:nyf , nx:nxf]
        destination = os.path.join("images", f"{name}.jpg")
        cv2.imwrite(destination, face_crop)
        messagebox.showinfo("Success", f"Found face and saved as {name}.jpg!")
        entry_name.delete(0, tk.END)
        lbl_path.config(text="No photo selected")
    else:
        messagebox.showerror("Failed", "No face detected in this photo. Try another.")
#GUI SETUP
root=tk.Tk()
root.title("Add person(Auto crop)")
root.geometry("400x250")
tk.Label(root, text="Enter Name:", font=("Arial", 12)).pack(pady=5)
entry_name = tk.Entry(root, font=("Arial", 12))
entry_name.pack(pady=5)
btn_select = tk.Button(root, text="Select Photo", command=select, bg="lightblue")
btn_select.pack(pady=10)
lbl_path = tk.Label(root, text="No photo selected", fg="gray")
lbl_path.pack(pady=5)
btn_save = tk.Button(root, text="Save Person", command=save_data, bg="green", fg="white", font=("Arial", 10, "bold"))
btn_save.pack(pady=20)
root.mainloop()