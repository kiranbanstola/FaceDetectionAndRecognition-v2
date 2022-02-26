from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import mysql.connector
import cv2
import csv
from time import strftime
from datetime import datetime


class Face_Recognition:
    # Layout Design
    def __init__(self):
        self.face_recog()

    # Attendance Function
    def mark_attendance(self, i, n):
        with open("attendance.csv", "r+", newline="\n") as f:
            myDataList = f.readlines()
            name_list = []
            for line in myDataList:
                entry = line.split((","))  # kiran,2
                name_list.append(entry[0])
            # mark present if not present
            if ((i not in name_list) and (n not in name_list)):
                now = datetime.now()
                d1 = now.strftime("%d/%m/%Y")
                dtString = now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{n},{dtString},{d1},Present")


    # Face Recognition
    def face_recog(self):

        # Function To Draw Boundary

        def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)

            coord = []
            # For making rectangle
            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
                id, predict = clf.predict(gray_image[y:y + h, x:x + w])
                confidence = int((100 * (1 - (predict / 300))))

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

                # for attendance
                my_cursor.execute("select Userid from users where Userid=" + str(id))
                i = my_cursor.fetchone()
                i = "+".join(i)

                # Condition for Confidence greater than 75%
                if confidence > 80:
                    cv2.putText(img, f"Userid:{i}", (x, y - 55), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
                    cv2.putText(img, f"Username:{n}", (x, y - 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
                    self.mark_attendance(i, n)
                else:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
                    cv2.putText(img, "Unknown Face", (x, y - 50), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)
                coord = [x, y, w, h]
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
    Face_Recognition()
