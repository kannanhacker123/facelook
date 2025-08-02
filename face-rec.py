# === Imports ===
import os
import cv2, cv2.face, cv2.data
import numpy as np
import pickle
import pyttsx3
import random
from datetime import datetime
from safe_filename import make_filename_safe

# === TTS Initialization ===
try:
    tts_engine = pyttsx3.init()
    tts_available = True
except Exception:
    print("TTS not available. Voice disabled.")
    tts_available = False

def speak(text: str):
    """Print and speak the text."""
    print(text)
    if tts_available:
        tts_engine.say(text)
        tts_engine.runAndWait()

# === Joke List for Strangers ===
jokes = [
    "Why did the computer go to the doctor? Because it had a virus!",
    "Why do programmers prefer dark mode? Because light attracts bugs!",
    "Why was the math book sad? Because it had too many problems.",
    "Why did the developer go broke? Because he used up all his cache.",
    "Why do Java developers wear glasses? Because they don't see sharp.",
]

# === Ensure Faces Directory Exists ===
os.makedirs("faces", exist_ok=True)

# === Face Data Collection ===
def collect_data(name: str, max_samples: int = 100):
    name = make_filename_safe(name)
    folder_path = os.path.join("faces", name)
    os.makedirs(folder_path, exist_ok=True)

    cap = cv2.VideoCapture(0)
    detector = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    speak(f"Starting face capture for {name}. Press 'q' to quit.")
    count = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            speak("Camera error.")
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = detector.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in faces:
            count += 1
            face_img = gray[y:y + h, x:x + w]
            face_img = cv2.resize(face_img, (200, 200))
            cv2.imwrite(f"{folder_path}/{count}.jpg", face_img)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(frame, f"{name} #{count}", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

        cv2.imshow("Collecting Data", frame)
        if cv2.waitKey(1) == ord('q') or count >= max_samples:
            break

    cap.release()
    cv2.destroyAllWindows()
    speak(f"Collected {count} samples for {name}.")

# === Model Training ===
def train_model():
    recognizer = cv2.face.LBPHFaceRecognizer_create()  # type: ignore
    detector = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

    faces = []
    labels = []
    label_dict = {}
    current_id = 0

    for person in os.listdir("faces"):
        person_path = os.path.join("faces", person)
        if not os.path.isdir(person_path):
            continue

        label_dict[person] = current_id
        for image_file in os.listdir(person_path):
            img_path = os.path.join(person_path, image_file)
            img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
            if img is None:
                continue
            faces.append(img)
            labels.append(current_id)

        current_id += 1

    if not faces:
        speak("No training data found.")
        return

    recognizer.train(faces, np.array(labels))
    recognizer.save("lbph_model.yml")

    with open("labels.pkl", "wb") as f:
        pickle.dump(label_dict, f)

    speak("Model trained and saved.")

# === Face Recognition ===
def recognize_faces():
    if not os.path.exists("lbph_model.yml"):
        speak("Model not trained yet.")
        return

    recognizer = cv2.face.LBPHFaceRecognizer_create()  # type: ignore
    recognizer.read("lbph_model.yml")

    with open("labels.pkl", "rb") as f:
        label_dict = pickle.load(f)

    rev_label_dict = {v: k for k, v in label_dict.items()}

    cap = cv2.VideoCapture(0)
    detector = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    last_seen = {}

    speak("Recognition started. Press 'q' to quit.")

    while True:
        ret, frame = cap.read()
        if not ret:
            speak("Camera error.")
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = detector.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in faces:
            face_img = gray[y:y + h, x:x + w]
            face_img = cv2.resize(face_img, (200, 200))
            label, confidence = recognizer.predict(face_img)

            now = datetime.now().timestamp()

            if confidence < 60:
                name = rev_label_dict[label]
                color = (0, 255, 0)
                if name not in last_seen or now - last_seen[name] > 5:
                    speak(f"Hello, {name}!")
                    last_seen[name] = now
            else:
                name = "Unknown"
                color = (0, 0, 255)
                if "stranger" not in last_seen or now - last_seen["stranger"] > 10:
                    speak("Hello stranger. Here's a joke: " + random.choice(jokes))
                    last_seen["stranger"] = now

            cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
            cv2.putText(frame, f"{name} ({confidence:.1f})", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2)

        cv2.imshow("Face Recognition", frame)
        key = cv2.waitKey(1)

        if key == ord('q'):
            break
        elif key == ord('r'):
            cap.release()
            cv2.destroyAllWindows()
            train_model()
            return recognize_faces()

    cap.release()
    cv2.destroyAllWindows()

# === Main Menu ===
def menu():
    while True:
        print("\n=== FACE RECOGNITION SYSTEM ===")
        print("1. Collect Face Data")
        print("2. Train Model")
        print("3. Start Recognition")
        print("4. Exit")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            name = input("Enter name: ").strip()
            collect_data(name)
        elif choice == "2":
            train_model()
        elif choice == "3":
            recognize_faces()
        elif choice == "4":
            speak("Goodbye.")
            break
        else:
            print("Invalid choice. Please enter 1-4.")

# === Entry Point ===
if __name__ == "__main__":
    menu()
