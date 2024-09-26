from manim import *
import cv2

cap = cv2.VideoCapture("Anúncio LinkedIn 3 - A. P. Rodrigues.mp4")
flag = True
while flag:
    flag, frame = cap.read()
    if flag:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame_img = ImageMobject(frame)
        self.add(frame_img)
        self.wait(0.04)
        self.remove(frame_img)
cap.release()
