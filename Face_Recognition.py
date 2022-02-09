from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np


class Face_recog:
    # Layout Design
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
        Label(screen, text="Face Recognition", font=("Print Bold", 24), fg="SteelBlue4", bg="powder blue").place(relx=0.25, rely=0.05)

        # Start_Button
        start_button = ttk.Button(screen, command=self.face_recog, text="Start Recognition", cursor="hand2")
        start_button.place(relx=0.25, rely=0.45, width=200, height=50)

    # Face Recognition
    def face_recog(self):
        # Function To Draw Boundary
        def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)

            coord = []
            # For making rectangle
            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
                id, predict = clf.predict(gray_image[y:y + h, x:x + w])
                confidence = int((100*(1 - predict / 300)))

                # Connect Database and fetch Data
                conn = mysql.connector.connect(host="localhost",
                                               user="root",
                                               password="root",
                                               database="attendance_system"
                                               )
                my_cursor = conn.cursor()

                my_cursor.execute("select Username from users where Userid=" + str(id))
                n = my_cursor.fetchone()
                n = "+".join(n)

                my_cursor.execute("select Rollno from users where Userid=" + str(id))
                r = my_cursor.fetchone()
                r = "+".join(r)

                my_cursor.execute("select Faculty from users where Userid=" + str(id))
                f = my_cursor.fetchone()
                f = "+".join(f)

                # Condition for Confidence greater than 75%
                if confidence > 80:
                    cv2.putText(img, f"Rollno:{r}", (x, y - 50), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 3)
                    cv2.putText(img, f"Username:{n}", (x, y - 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 3)
                    cv2.putText(img, f"Faculty:{f}", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 3)
                else:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
                    cv2.putText(img, "Unknown Face", (x, y - 50), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 3)
                coord = [x, y, w, y]
            return coord

        # Function to Recognize Face
        def recognize(img, clf, faceCascade):
            coord = draw_boundary(img, faceCascade, 1.1, 10, (0, 255, 0), "Face", clf)
            return img

        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        # Histogram Alg
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap = cv2.VideoCapture(0)
        while True:
            ret, img = video_cap.read()
            img = recognize(img, clf, faceCascade)
            cv2.imshow("Welcome to Face Recognition", img)
            if cv2.waitKey(1) == 13:
                break
            video_cap.release()
            cv2.destroyAllWindows()


if __name__ == "__main__":
    screen = Tk()
    obj = Face_recog(screen)
    screen.mainloop()
