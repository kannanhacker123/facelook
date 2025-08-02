# FaceLook

FaceLook is a fun project built primarily to learn OpenCV, with a practical twist: it allows you to register faces along with their names, train a recognition model, and then recognize faces using your webcam. The project is written in Python and uses OpenCV, with some AI/vibe coding sprinkled in.

## Features

- **Register Faces:** Collect face data for a given name using your webcam.
- **Train Model:** After collecting faces, train an LBPH face recognition model.
- **Face Recognition:** Recognize registered faces in real time. If an unknown face is detected, the app tells a programming joke!
- **Voice Feedback:** Uses text-to-speech for friendly prompts and greetings.
- **Fun Touches:** Jokes for strangers, playful UI in console.

## Tech Stack

- Python 3
- OpenCV (cv2)
- pyttsx3 (text-to-speech)
- Numpy
- Pickle

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/kannanhacker123/facelook.git
   cd facelook
   ```
2. **Create a virtual environment and activate it:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the main script:

```bash
python face-rec.py
```

You’ll see a menu:

```
=== FACE RECOGNITION SYSTEM ===
1. Collect Face Data
2. Train Model
3. Start Recognition
4. Exit
```

**Workflow:**
1. Select **1** to collect face data for a person. Enter their name when prompted and look at the webcam.
2. Select **2** to train the recognition model on your collected faces.
3. Select **3** to start face recognition. The app will greet recognized faces and tell jokes to strangers!

**Tips:**
- Face images are stored in the `faces/` folder.
- Trained model is saved as `lbph_model.yml` and labels as `labels.pkl`.
- Press "q" to quit recognition or data collection.
- Press "r" during recognition to retrain the model on new data.

## Contributing

Contributions are welcome! Feel free to open issues or pull requests. For major changes, please open an issue first to discuss what you’d like to change.

## License

MIT License

## Author

Made by Aravind K.B (Kannan)  
Full-stack web developer | Python, JS, C++ enthusiast  
GitHub: [kannanhacker123](https://github.com/kannanhacker123)

---

## Codebase Tour & Structure

- `face-rec.py`: Main application script containing all logic (data collection, training, recognition, voice feedback, jokes).
- `safe_filename.py`: Utility for sanitizing names for folder/file safety.
- `faces/`: Directory for storing captured face images for each registered user.
- `lbph_model.yml`, `labels.pkl`: Trained model and label mappings.

No extra user or developer guides are present in the repo. All instructions are visible via menu prompts in the terminal.

---

Enjoy experimenting and learning with FaceLook!
