Project Statement: V.I.P.E.R

Project Title: Visual Identity and Person Entry Recorder (V.I.P.E.R)
Domain: Computer Vision / Security Surveillance
Technology Stack: Python, OpenCV, Deep Learning (Caffe), Tkinter

1. Problem Definition

The Current Landscape

Traditional Close-Circuit Television (CCTV) systems are predominantly passive. They record hours of footage that usually sit unreviewed on a hard drive until an incident occurs. Finding a specific person (e.g., a missing child, a known shoplifter, or an authorized employee) requires manual scanning of hours of video, which is:

Time-Consuming: Humans cannot watch multiple screens effectively 24/7.

Error-Prone: Fatigue leads to missed sightings.

Reactive: Action is usually taken after the person has left the premises.

The Need

There is a critical need for an active surveillance system that can:

Automatically detect faces in a live feed.

Instantly distinguish between a "Target of Interest" and the general public.

Log the entry time of specific individuals without human intervention.

2. Proposed Solution

V.I.P.E.R is an intelligent surveillance system designed to bridge the gap between passive recording and active security. It utilizes computer vision and deep learning to identify specific individuals in real-time.

The system operates on a "Watchlist" principle:

For Targets: If a person on the watchlist is seen, the system highlights them in Green, displays their name, and logs their entry time to a secure CSV record.

For Unknowns: If a person is not recognized, they are marked as "Unknown" in Red, but the system continues to snapshot the environment to ensure a record of all visitors is kept.

3. Methodology & Architecture

The project is divided into three distinct functional modules to handle the lifecycle of data:

Phase 1: Data Collection (Autonomous)

Script: test3.py

Logic: Uses Haar Cascade classifiers to detect faces in a live stream. It autonomously captures and saves face crops of passersby to build a raw dataset (saved_faces), eliminating the need for manual image gathering.

Phase 2: Target Registration (Management)

Script: INTEL.py

Logic: A Graphical User Interface (GUI) built with Tkinter. It allows security administrators to upload a photo of a specific target. The system uses a pre-trained Caffe Deep Neural Network (DNN) to precisely extract facial features and save them to the recognition database (images/). This ensures high-quality data for the recognizer.

Phase 3: Real-Time Recognition (Surveillance)

Script: main.py

Logic: This is the core engine. It performs three simultaneous tasks:

Training: On startup, it trains an LBPH (Local Binary Patterns Histograms) recognizer on the registered targets.

Detection: It scans the live camera feed for faces.

Classification:

Match Found: Logs name and timestamp to Target_seen.csv.

No Match: Snapshots the scene to Different_people/ every 3 seconds to maintain a visual log of all traffic.

4. Conclusion

V.I.P.E.R transforms standard surveillance from a retrospective tool into a proactive security asset. By automating the identification process, it reduces the workload on security personnel and ensures that the entry of critical individuals is never missed.
