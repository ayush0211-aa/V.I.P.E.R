🐍 V.I.P.E.R (Visual Identity and Person Entry Recorder)

V.I.P.E.R is a specialized surveillance and facial recognition tracking system designed to identify specific target individuals in real-time. Unlike standard CCTV, V.I.P.E.R differentiates between "Unknown" subjects and "Targets" stored in its database.
The system is built on a three-part architecture:
Autonomous Capture: Automatically catalogs faces of everyone passing by.
Target Entry (GUI): A user-friendly interface to upload specific targets (e.g., missing persons, authorized personnel) into the system.
Live Tracker: Integrates the camera feed to flag targets, log their sightings with timestamps, and ignore non-targets.


📂 Project Structure
The system consists of three main executable scripts:
test3.py (The Recorder):
Function: Automated data gathering.
Action: Opens the camera, detects faces using Haar Cascades, and automatically learns and saves faces to a local directory (saved_faces).
INTEL.py (The Manager):
Function: Target registration GUI.
Action: Allows the administrator to upload a photo of a specific person and assign a name. It uses a DNN (Deep Neural Network) to crop the face precisely and save it to the images/ database for the main tracker to use.
main.py (The Tracker):
Function: Real-time surveillance.
Action: Trains a recognizer on the images/ folder. It watches the live feed, marking recognized individuals as "FOUND: [Name]" and logging the time of entry to a CSV file. Unrecognized faces are marked as "Unknown". It also snapshots all distinct visitors to the Different_people/ folder.
⚙️ Installation
Prerequisites
Ensure you have Python installed. You will need the following dependencies:
pip install opencv-python opencv-contrib-python numpy


(Note: tkinter is usually included with Python, but if you are on Linux, you might need to install python3-tk).
Model Setup (Crucial)
This project requires Caffe Deep Learning models for accurate face detection in the INTEL and main scripts.
Create a folder named models in the root directory.
Download the following files and place them inside the models folder:
deploy.prototxt.txt

res10_300x300_ssd_iter_140000.caffemodel


💻 Usage


Step 1: General Population Capture (Optional)
Run this to simply detect and save faces of anyone who walks by.
python test3.py


Output: Saves face crops to saved_faces/.
Quit: Press q.


Step 2: Add a Target Person
Run the GUI to register a specific person you want to track.
python INTEL.py


Click "Select Photo" to choose an image of the person from your computer.
Enter the person's name in the text box.
Click "Save Person".
The system auto-crops the face and saves it to images/.


Step 3: Start Surveillance
Run the main tracking engine.
python main.py


The system will first train itself on the photos inside images/.
It will open the security camera feed.
If a Target is seen:
Visual Box: Green (FOUND: Name)
Log: Written to Target_seen (CSV file) with date and time.
If Unknown:
Visual Box: Red (Unknown)
Snapshots: Every 3 seconds, a full-frame snapshot of people is saved to Different_people/.


🛠️ Tech Stack


Language: Python 3
Computer Vision: OpenCV (cv2)
Face Detection: Haar Cascades & DNN (Caffe Model)
Face Recognition: LBPH (Local Binary Patterns Histograms)
GUI: Tkinter
Data Handling: CSV (for logs), NumPy
