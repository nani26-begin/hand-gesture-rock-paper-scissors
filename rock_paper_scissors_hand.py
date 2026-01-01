import cv2
import mediapipe as mp
import random
import time
import numpy as np
from mediapipe.tasks import python
from mediapipe.tasks.python import vision

# -------------------- MediaPipe Hand Landmarker --------------------
base_options = python.BaseOptions(model_asset_path="hand_landmarker.task")
options = vision.HandLandmarkerOptions(
    base_options=base_options,
    num_hands=1
)
detector = vision.HandLandmarker.create_from_options(options)

# -------------------- Game Variables --------------------
cap = cv2.VideoCapture(0)
choices = ["Rock", "Paper", "Scissors"]

last_time = time.time()
computer_move = "Waiting"
winner = ""

# -------------------- Gesture Detection --------------------
def get_gesture(landmarks):
    tips = [8, 12, 16, 20]
    folded = 0

    for tip in tips:
        if landmarks[tip].y > landmarks[tip - 2].y:
            folded += 1

    if folded == 4:
        return "Rock"
    elif folded == 0:
        return "Paper"
    elif folded == 2:
        return "Scissors"
    else:
        return "Unknown"

# -------------------- Main Loop --------------------
while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    mp_image = mp.Image(
        image_format=mp.ImageFormat.SRGB,
        data=rgb
    )

    result = detector.detect(mp_image)

    user_move = "Waiting"

    # -------- Hand Detection --------
    if result.hand_landmarks:
        hand = result.hand_landmarks[0]
        user_move = get_gesture(hand)

        for lm in hand:
            x = int(lm.x * frame.shape[1])
            y = int(lm.y * frame.shape[0])
            cv2.circle(frame, (x, y), 5, (0, 255, 0), -1)

    # -------- Game Logic (Every 3 Seconds) --------
    if user_move in choices and time.time() - last_time > 3:
        computer_move = random.choice(choices)
        last_time = time.time()

        if user_move == computer_move:
            winner = "Draw"
        elif (user_move == "Rock" and computer_move == "Scissors") or \
             (user_move == "Paper" and computer_move == "Rock") or \
             (user_move == "Scissors" and computer_move == "Paper"):
            winner = "You Win!"
        else:
            winner = "Computer Wins!"

    # -------- Display Text --------
    cv2.putText(frame, f"You: {user_move}", (10, 40),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv2.putText(frame, f"Computer: {computer_move}", (10, 80),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

    cv2.putText(frame, f"Result: {winner}", (10, 120),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    cv2.imshow("Rock Paper Scissors - Hand Gesture", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# -------------------- Cleanup --------------------
cap.release()
cv2.destroyAllWindows()
