#  FaceLook

> A fun and practical OpenCV project to learn face recognition — with a splash of humor and AI charm!



FaceLook is a Python-based facial recognition app built for learning and exploration. It allows users to register their faces, train a recognition model, and then recognize faces in real time using a webcam. If a stranger appears, the app responds with a random programming joke!


---

# Features

## Register Faces – Collect face images from your webcam for each user.

## Train Model – Train an LBPH (Local Binary Patterns Histograms) face recognition model on collected data.

## Real-Time Recognition – Detect and identify known faces live; strangers get greeted with a joke!

## Voice Feedback – Friendly spoken messages using pyttsx3.

## Fun Touches – Playful console UI and jokes to keep things light.



---

# Use Cases

## Attendance System

How it works: Register individuals (students, employees, etc.), then automatically log their attendance with timestamps.

Benefit: Touchless, fast, and more accurate than manual systems.


## Home Security / Access Control

Recognize family or guests and trigger actions like unlocking doors or sending alerts.


## Personalized Smart Displays

Show personalized greetings, weather, or schedule based on who’s in front of the webcam.


## Small Business Enhancer

Recognize returning customers and remember preferences (with consent).


## Interactive Installations

Trigger art or animations based on recognized or new faces.



---

# Tech Stack

- Python 3

- OpenCV (cv2)

- NumPy

- Pickle

- pyttsx3 (for Text-to-Speech)



---

# Installation

## Clone the repository
git clone https://github.com/kannanhacker123/facelook.git
cd facelook

## Create and activate a virtual environment
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

## Install dependencies
pip install -r requirements.txt


---

🚀 Usage

Run the app:

```python
python face-rec.py
```
You'll see:

=== FACE RECOGNITION SYSTEM ===
1. Collect Face Data
2. Train Model
3. Start Recognition
4. Exit

# Workflow

1. Collect Face Data
Select option 1, enter a name, and let the webcam capture your face.


2. Train the Model
Option 2 will train the LBPH model using the collected faces.


3. Start Recognition
Option 3 activates real-time face recognition. Known users are greeted by name, and unknown faces get a programming joke.




---

# Project Structure
```
facelook/
├── face-rec.py          # Main application logic
├── safe_filename.py     # Utility for safe folder/file naming
├── faces/               # Directory storing face data
├── lbph_model.yml       # Trained face recognition model
├── labels.pkl           # Name-label mappings
└── requirements.txt     # Python dependencies

```
---

# Shortcuts & Tips

Press q – Quit face data collection or recognition.

Press r – Retrain the model live with new data during recognition.

All face images are saved in the faces/ directory.

Models are saved as:

lbph_model.yml (model file)

labels.pkl (label mapping)




---

# Contributing

Pull requests and issue submissions are welcome!

For large changes, please open an issue first to discuss the idea.


---

# License

This project is licensed under the MIT License.


---

# Author

Aravind K.B (Kannan)
Full-stack web developer | Python, JS, and C++ enthusiast
🔗 GitHub: @kannanhacker123


