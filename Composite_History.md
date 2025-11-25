## 📜 Project History: V.I.P.E.R Evolution
Project: Visual Identity and Person Entry Recorder
Status: Active / Stable
## 📅 Version 0.1: The "Collector" Phase (Proof of Concept)
Associated Module: test3.py
Focus: Autonomous Data Collection & Unsupervised Learning
The project began with a fundamental challenge: "Can we build a system that detects faces and learns from them without human intervention?"
In this initial phase, the goal was to access the camera feed and catalog visitors autonomously. We implemented Haar Cascade Classifiers due to their lightweight processing requirements, allowing the system to run on lower-end hardware.
	•	Key Milestone: Implementation of cv2.face.LBPHFaceRecognizer_create().
	•	Feature Implemented: Autonomous Capture. The system watches a video stream, detects a face, and if the confidence distance is high (indicating a new person), it automatically saves the face crop to the saved_faces/directory.
	•	Limitation Identified: Haar Cascades proved too sensitive to background noise, often misinterpreting shadows or non-human objects as faces. A more robust detection method was required for high-security applications.
## 📅 Version 0.5: The "Manager" Phase (Target Definition)
Associated Module: INTEL.py (Registration GUI)
Focus: Precision, User Interface, and Data Quality
To address the accuracy limitations of v0.1, we transitioned from Haar Cascades to Deep Learning (Caffe Model) for the crucial task of registering targets. We needed a mechanism for a human administrator to explicitly define who the system should look for.
	•	Key Milestone: Integration of cv2.dnn.readNetFromCaffe.
	•	Feature Implemented: Graphical User Interface (Tkinter). This bridged the gap between raw code and usability, allowing non-technical administrators to upload reference photos easily.
	•	Feature Implemented: "Smart Cropping." Instead of storing raw uploaded photos, the system was programmed to detect the face, calculate a bounding box with a 30% padding margin, and save a standardized crop to the images/directory.
	•	Impact: This ensured that the training dataset contained only high-fidelity, centered face images, drastically improving recognition rates.
## 📅 Version 1.0: The "Sentinel" Phase (Active Surveillance)
Associated Module: main.py (The Core Engine)
Focus: System Integration, Real-Time Logic, & Logging
This phase represented the convergence of the previous technologies. We combined the robust dataset management of v0.5 with the live video processing logic of v0.1 to create a unified security tool.
	•	Key Milestone: Hybrid Architecture Implementation.
	◦	Detection: Utilized Caffe DNN for high-accuracy face finding.
	◦	Recognition: Utilized LBPH for fast, low-latency identity prediction.
	•	Feature Implemented: Logic Gates for "Known" vs. "Unknown".
	◦	Target Found: If Confidence < 60, the system draws a Green Box and logs the event to a CSV file.
	◦	Stranger Detected: If Confidence > 60, the system draws a Red Box and triggers a snapshot.
	•	Feature Implemented: Rate Limiting. To prevent file I/O operations from freezing the video feed, we implemented a timer logic (time.time() - last_save_t > 3) to limit stranger snapshots to once every 3 seconds.
## 🚀 Current State (v1.1)
The system is now a fully functional "Active Surveillance" unit capable of deployment.

##Architecture Comparison

| Features.          |v0.1 (test3.py).  |v1.0 (main.py)               |
| ------------------ |:----------------:|---------------------------- |
|Detection Algorithm |Haar Cascade (XML)|Deep Neural Network (Caffe)  |
|Data Source         |Live Camera Only  |Live Camera + Static Database|
|User Control        |None (Autonomous) |Full GUI (INTEL.py)          |
|Output.             |Raw Images.       | CSV Logs + Annotated Video. |

## Future Roadmap (v2.0 Concepts)

Database Migration: Transition from file-based storage (images/ folder) to a structured SQL database for faster querying.

Remote Alerts: Integration of an SMTP client to send email notifications upon target detection.

Multi-Camera Support: Refactoring the main.py loop to handle multiple IP camera streams simultaneously.
