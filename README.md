# 🎮 Hand Gesture Rock–Paper–Scissors Game

> A real-time **Rock–Paper–Scissors game controlled using hand gestures**, built with Computer Vision and a webcam.

---

## ✨ Project Overview

This project is a **touchless Rock–Paper–Scissors game** where the player uses **hand gestures** to play against the computer.  
The system captures live video from a webcam, detects hand landmarks, recognizes gestures, and determines the winner automatically.

This project demonstrates **real-time computer vision**, **gesture recognition**, and **human–computer interaction** using modern tools.

---

## 🔑 Features

✔ Real-time hand detection using webcam  
✔ Accurate hand landmark tracking  
✔ Gesture recognition:
- ✊ Rock  
- ✋ Paper  
- ✌️ Scissors  

✔ Computer opponent with random move generation  
✔ Automatic result evaluation (Win / Lose / Draw)  
✔ Timed gameplay logic for smooth experience  
✔ Live visualization of hand landmarks and results  
✔ Runs completely on local machine  

---

## 🛠️ Tech Stack

- 🐍 **Python**
- 📷 **OpenCV** – Webcam access & visualization
- ✋ **MediaPipe Tasks API** – Hand landmark detection
- 🧠 **Computer Vision** – Gesture recognition logic

---

## 🧠 How It Works (Process)

1️⃣ **Webcam Capture**  
OpenCV captures real-time video frames from the webcam.

2️⃣ **Hand Landmark Detection**  
MediaPipe Tasks API detects hand landmarks from each frame.

3️⃣ **Gesture Recognition**  
Finger positions are analyzed to classify gestures:
- Rock
- Paper
- Scissors

4️⃣ **Game Logic Execution**  
The computer randomly selects a move and the result is evaluated.

5️⃣ **Real-Time Display**  
Player move, computer move, and result are displayed instantly.

---

## 🖐️ Hand Gesture Mapping

| Gesture | Meaning |
|-------|--------|
| ✊ Closed Fist | Rock |
| ✋ Open Palm | Paper |
| ✌️ Two Fingers | Scissors |

⏱ Hold the gesture for **3 seconds** to register a move.

---

## 📂 Project Structure

