# FaceLook 😄🎥

A fun and practical OpenCV project for learning face recognition—with a splash of humor and AI charm!

---

## What is FaceLook?

**FaceLook** is a Python-based facial recognition app designed for hands-on exploration. Register your face, train a recognition model, and recognize faces in real time using your webcam. If a stranger appears, FaceLook responds with a random programming joke!

---

## Features

- **Register Faces:** Collect face images from your webcam for each user
- **Train Model:** Train an LBPH (Local Binary Patterns Histograms) face recognition model
- **Real-Time Recognition:** Detect and identify known faces live; strangers get greeted with a joke!
- **Voice Feedback:** Friendly spoken messages using `pyttsx3`
- **Fun Touches:** Playful console UI and jokes for a lighthearted experience

---

## Use Cases

- **Attendance System:** Touchless logging for students, employees, etc.
- **Home Security / Access Control:** Recognize family or guests, trigger actions
- **Personalized Smart Displays:** Greet users, show weather/schedules
- **Small Business Enhancer:** Remember returning customers and preferences (with consent)
- **Interactive Installations:** Trigger art or animations for recognized or new faces

---

## Tech Stack

- Python 3
- OpenCV (`cv2`)
- NumPy
- Pickle
- pyttsx3 (Text-to-Speech)

---

## Installation

1. **Clone the repository**
    ```sh
    git clone https://github.com/kannanhacker123/facelook.git
    cd facelook
    ```

2. **Create and activate a virtual environment**
    ```sh
    python -m venv venv
    # Windows
    venv\Scripts\activate
    # macOS/Linux
    source venv/bin/activate
    ```

3. **Install dependencies**
    ```sh
    pip install -r requirements.txt
    ```

---

## 🚀 Usage

Run the app:

```sh
python face-rec.py
```

You'll see:

```
=== FACE RECOGNITION SYSTEM ===
1. Collect Face Data
2. Train Model
3. Start Recognition
4. Exit
```

### Workflow

1. **Collect Face Data:**  
   Select option 1, enter a name, and let the webcam capture your face.

2. **Train the Model:**  
   Choose option 2 to train the LBPH model with your collected faces.

3. **Start Recognition:**  
   Option 3 activates real-time recognition. Known users are greeted by name, unknown faces get a programming joke.

---

## Project Structure

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

## Shortcuts & Tips

- **Press `q`** – Quit face data collection or recognition
- **Press `r`** – Retrain the model live with new data during recognition
- Face images are saved in the `faces/` directory
- Models are saved as:
    - `lbph_model.yml` (model file)
    - `labels.pkl` (label mapping)

---

## Contributing

Pull requests and issue submissions are welcome!  
For large changes, please open an issue first to discuss your idea.

---

## License

This project is licensed under the MIT License.

---

## Author

**Aravind K.B (Kannan)**  
Full-stack web developer | Python, JS, and C++ enthusiast  
🔗 [GitHub: @kannanhacker123](https://github.com/kannanhacker123)
