import time
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import cv2
import os
import numpy as np


class Train_Dataset:
    def __init__(self):
        #self.screen = screen
        #self.screen.geometry("300x50+600+500")
        #self.screen.title("Training Dataset")
        #self.screen.resizable(False, False)
        #self.progress = ttk.Progressbar(self.screen,orient=HORIZONTAL,length=300,mode='indeterminate')
        #self.progress.pack(pady=5)
        #self.progress.start(1)
        #self.screen.update_idletasks()
        self.train_dataset()
        #self.progress.stop()
        #self.screen.destroy()

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
            #cv2.imshow("Training Dataset", imageNp)
            #cv2.waitKey(1) == 13
        ids = np.array(ids)

        # Train Classifier and Save
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces, ids)
        clf.write("classifier.xml")
        #cv2.destroyAllWindows()



if __name__ == "__main__":
    Train_Dataset()
