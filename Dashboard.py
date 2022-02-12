import os
from tkinter import *
from UserDetails import User_Details
from Train import Train_Dataset
from Face_Recognition import Face_Recognition
from Attendance import Attendance_Details


class Dashboard_Admin:
    def __init__(self, screen):
        self.screen = screen
        self.screen.geometry("1280x720+150+75")
        self.screen.title("Attendance System")
        self.screen.resizable(False, False)

        # Label for Welcome
        Label(self.screen,text="Welcome to Dashboard", font=("Print Bold", 24)).pack()

        # Button for User Details
        Button(self.screen,
               text="User Details",
               bg="blue", fg="White",
               font=("Montserrat bold", 10),
               command=self.user_details
               ).place(relx=0.2, rely=0.3, height=40, width=120)

        # Button for Attendance
        Button(self.screen,
               text="Attendance",
               bg="black", fg="White",
               font=("Montserrat bold", 10),
               command=self.attendance_data
               ).place(relx=0.35, rely=0.3, height=40, width=120)

        # Button for Detect Face
        Button(self.screen,
               text="Detect Face",
               bg="black", fg="White",
               font=("Montserrat bold", 10),
               command=self.face_data
               ).place(relx=0.5, rely=0.3, height=40, width=120)

        # Button for Training Dataset
        Button(self.screen,
               text="Train Data",
               bg="black", fg="White",
               font=("Montserrat bold", 10),
               command=self.train_data
               ).place(relx=0.2, rely=0.4, height=40, width=120)

        # Button for ViewImage In Dataset
        Button(self.screen,
               text="View Dataset",
               bg="black", fg="White",
               font=("Montserrat bold", 10),
               command=self.open_dataset
               ).place(relx=0.35, rely=0.4, height=40, width=120)

    # Def for Opening Dataset
    def open_dataset(self):
        os.startfile("data")

    # Function Button
    def user_details(self):
        self.new_window = Toplevel(self.screen)
        self.app = User_Details(self.new_window)

    def train_data(self):
        self.new_window = Toplevel(self.screen)
        self.app = Train_Dataset(self.new_window)

    def face_data(self):
        self.new_window = Toplevel(self.screen)
        self.app = Face_Recognition(self.new_window)

    def attendance_data(self):
        self.new_window = Toplevel(self.screen)
        self.app = Attendance_Details(self.new_window)


if __name__ == "__main__":
    screen = Tk()
    obj = Dashboard_Admin(screen)
    screen.mainloop()
