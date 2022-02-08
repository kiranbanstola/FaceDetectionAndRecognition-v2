from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import cv2
import os
import numpy as np


class Train_Dataset:
    def __init__(self, screen):
        self.screen = screen
        self.screen.geometry("400x200+200+150")
        self.screen.title("Train Dataset")
        self.screen.resizable(False, False)

        # bg_gradient
        img1 = Image.open(r"D:\FaceDetectionAndRecognition-v2\bg_gradient.jpg")
        img1 = img1.resize((400, 200), Image.ANTIALIAS)
        self.photo_img1 = ImageTk.PhotoImage(img1)
        bg_img = Label(self.screen, image=self.photo_img1)
        bg_img.place(x=0, y=0)
        Label(text="Train Data", font=("Print Bold", 24), fg="SteelBlue4",bg="powder blue").place(relx=0.35, rely=0.05)

        # Tain_Button
        train_button = ttk.Button(screen, command=self.train_dataset, text="Start Training Dataset", cursor="hand2")
        train_button.place(relx=0.25, rely=0.45, width=200, height=50)

    # Function for Train Algorithm
    def train_dataset(self):
        data_dir = ("data")
        path = [os.path.join(data_dir, file) for file in os.listdir(data_dir)]
        faces = []
        ids = []
        for image in path:
            # Gray Scale Image Convert
            img = Image.open(image).convert('L')
            imageNp = np.array(img, 'uint8')
            id = int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training Dataset", imageNp)
            cv2.waitKey(1) == 13
        ids = np.array(ids)

        # Train Classifier and Save
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces, ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result", "Training Datasets Completed!!")


if __name__ == "__main__":
    screen = Tk()
    obj = Train_Dataset(screen)
    screen.mainloop()
