from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import cv2
import os
import numpy as np


class Face_recog:
    def __init__(self, screen):
        self.screen = screen
        self.screen.geometry("400x200+200+150")
        self.screen.title("Face Recognition")
        self.screen.resizable(False, False)

        # bg_gradient
        img1 = Image.open(r"D:\FaceDetectionAndRecognition-v2\bg_gradient.jpg")
        img1 = img1.resize((400, 200), Image.ANTIALIAS)
        self.photo_img1 = ImageTk.PhotoImage(img1)
        bg_img = Label(self.screen, image=self.photo_img1)
        bg_img.place(x=0, y=0)
        Label(screen, text="Face Recognition", font=("Print Bold", 24), fg="SteelBlue4", bg="powder blue").place(
            relx=0.25, rely=0.05)

        # Start_Button
        start_button = ttk.Button(screen, text="Start Recognition", cursor="hand2")
        start_button.place(relx=0.25, rely=0.45, width=200, height=50)


if __name__ == "__main__":
    screen = Tk()
    obj = Face_recog(screen)
    screen.mainloop()
