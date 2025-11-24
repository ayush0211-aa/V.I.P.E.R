🐍 V.I.P.E.R (Visual Identity and Person Entry Recorder)

📖 Project Overview

V.I.P.E.R is a specialized surveillance and facial recognition tracking system designed to identify specific target individuals in real-time. Unlike standard CCTV, V.I.P.E.R differentiates between "Unknown" subjects and "Targets" stored in its database. The system is built on a three-part architecture: Autonomous Capture: Automatically catalogs faces of everyone passing by. Target Entry (GUI): A user-friendly interface to upload specific targets (e.g., missing persons, authorized personnel) into the system. Live Tracker: Integrates the camera feed to flag targets, log their sightings with timestamps, and ignore non-targets.

It utilizes a hybrid approach:

Deep Learning (DNN) for robust face detection (handling lighting and angles better than standard Haar cascades).

LBPH (Local Binary Patterns Histograms) for efficient face recognition.

Automated Logging to create a digital timestamp of every time a target enters the frame.

✨ Features

Real-Time Identification: Instantly differentiates between "Targets" (Green Box) and "Unknowns" (Red Box).

Secure Watchlist Management: A dedicated GUI (INTEL.py) to add specific people to the tracking database.

Intelligent Auto-Crop: The registration module automatically detects, centers, and crops faces from uploaded photos to ensure high-quality training data.

Automated Attendance/Entry Log: Saves the Name, Date, and Time of every recognized target to a CSV file.

Stranger Snapshots: Automatically saves photos of unidentified persons every 3 seconds for security review.

Autonomous Learning Mode: A separate module (test3.py) to gather data on the general population without manual input.

🛠️ Tools & Technologies Used

Language: Python 3.x

Computer Vision: OpenCV (cv2)

Deep Learning Framework: Caffe (via OpenCV DNN module)

GUI Framework: Tkinter

Data Processing: NumPy, CSV module

⚙️ Installation & Setup

1. Prerequisite Libraries

Ensure you have Python installed. Open your terminal or command prompt and install the required dependencies:

pip install opencv-python opencv-contrib-python numpy


(Note: Tkinter is usually pre-installed with Python. If you are on Linux and get an error, run sudo apt-get install python3-tk)

2. File Organization

Your project folder should look like this. Note: You must rename the file INTEL to INTEL.py.

Project_Folder/
│

├── models/                     <-- YOU MUST CREATE THIS FOLDER

│   ├── deploy.prototxt.txt

│   └── res10_300x300_ssd_iter_140000.caffemodel

│

├── images/                     <-- Created automatically by INTEL.py

├── saved_faces/                <-- Created automatically by test3.py

├── Different_people/           <-- Created automatically by main.py

│

├── INTEL.py                    <-- (Rename your 'INTEL' file to this)

├── main.py

└── test3.py


3. Model Setup (CRITICAL STEP)

The logic in INTEL.py and main.py relies on Caffe models. The project will crash if these are missing.

Create a folder named models in your project directory.

Download the following two files from the official OpenCV repository or a reliable source:

deploy.prototxt.txt

res10_300x300_ssd_iter_140000.caffemodel

Place them inside the models folder.

🚀 How to Run the Project

Phase 1: Register a Target (The Watchlist)

Before the system can recognize anyone, you must teach it who to look for.

Run the Registration GUI:

python INTEL.py


A window titled "Add person(Auto crop)" will appear.

Click "Select Photo" and choose a clear image of the person (JPG/PNG).

Type the person's Name in the text box.

Click "Save Person".

What happens: The system uses the DNN to find the face, crops it with a buffer, and saves it to the images/ folder.

Phase 2: Start Surveillance

Once you have at least one person in your images/ folder, you can start the tracker.

Run the Main Script:

python main.py


The system will:

Train: Read all photos in images/ and teach the recognizer.

Launch: Open the webcam feed.

Track: Draw Green boxes for known targets and Red boxes for strangers.

Log: Write entries to Target_seen (CSV file).

Press 'q' to quit the surveillance feed.

Optional: Autonomous Data Collection

If you want to simply collect faces from the camera without naming them (for building a raw dataset):

python test3.py


🧪 Instructions for Testing

Follow this exact sequence to verify the system is working correctly:

Test 1: Verification of Registration

Run INTEL.py.

Upload a photo of yourself.

Enter your name (e.g., "Admin").

Click Save.

Check: Go to the images/ folder in your file explorer. You should see a file named Admin.jpg that is a cropped version of your face.

Test 2: Verification of Recognition

Run main.py.

Wait for the message [INFO] Learning from your photos... in the console.

Look at the camera.

Check: A GREEN box should appear around your face with the text FOUND: Admin.

Check: A file named Target_seen (or Target_seen.csv) should be created/updated. Open it to verify it logged your name and the current time.

Test 3: Verification of Unknown Handling

Ask a friend (who is NOT in the images folder) to stand in front of the camera, OR cover your face with a mask/phone.

Check: A RED box should appear with the text Unknown.

Check: Go to the Different_people/ folder. You should see new snapshot images appearing every 3 seconds.

⚠️ Troubleshooting

Error: "Model files missing": You did not create the models folder or download the Caffe files correctly (See Installation Step 3).

Camera doesn't open: Check cv2.VideoCapture(0) in the code. If you have multiple cameras, try changing 0 to 1.

Laggy Video: The system saves a snapshot every 3 seconds. If your computer is slow, this might cause a slight stutter.
