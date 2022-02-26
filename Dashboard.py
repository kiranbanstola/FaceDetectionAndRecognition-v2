import os
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from tkinter import messagebox
import Train
from UserDetails import User_Details
import Face_Recognition
from Attendance import Attendance_Details

class Dashboard_Admin:
    def __init__(self, screen):
        self.screen = screen
        self.screen.geometry("600x500+250+100")
        self.screen.title("Attendance System")
        self.screen.resizable(False, False)
        self.path = os.getcwd()
        # bg_gradient
        main_frame = Frame(self.screen, bg="#1E1844")
        main_frame.place(x=0, y=0, width=600, height=500)

        # Main Login Frame
        main_frame = Frame(self.screen, bg="white")
        main_frame.place(x=50, y=50, width=500, height=400)
        # Main Labelframe
        main_frame = LabelFrame(main_frame, text="Welcome To Dashboard", font=("Print Bold", 18), labelanchor="n",
                                bg="white")
        main_frame.place(x=10, y=10, width=480, height=380)

        # Button with Icon for User Details
        self.User_icon = ImageTk.PhotoImage(
            Image.open(self.path+"/icons/UserDetails_Frame.png"))
        userdetails_btn = ttk.Button(main_frame,
                                     text="User Details",
                                     command=self.user_details,
                                     cursor="hand2",
                                     image=self.User_icon,
                                     compound=LEFT)
        userdetails_btn.place(x=60, y=60, width=130, height=45)

        # Button for Attendance
        self.Attendance_icon = ImageTk.PhotoImage(
            Image.open(self.path+"/icons/Attendance_Frame.png"))
        attendance_btn = ttk.Button(main_frame,
                                    text="Attendance",
                                    command=self.attendance_data,
                                    cursor="hand2",
                                    image=self.Attendance_icon,
                                    compound=LEFT,

                                    )
        attendance_btn.place(x=60, y=120, width=130, height=45)

        # Button for Detect Face
        self.DetectFace_icon = ImageTk.PhotoImage(
            Image.open(self.path+"/icons/DetectFace_Frame.png"))

        detectFace_btn = ttk.Button(main_frame,
                                    text="Detect Face",
                                    command=self.face_data,
                                    cursor="hand2",
                                    image=self.DetectFace_icon,
                                    compound=LEFT)
        detectFace_btn.place(x=60, y=180, width=130, height=45)

        # Button for Train Dataset
        self.TrainData_icon = ImageTk.PhotoImage(
            Image.open(self.path+"/icons/TrainData_Frame.png"))
        trainDataset_btn = ttk.Button(main_frame,
                                      text="Train Dataset",
                                      command=self.train_data,
                                      cursor="hand2",
                                      image=self.TrainData_icon,
                                      compound=LEFT)
        trainDataset_btn.place(x=220, y=60, width=130, height=45)

        # Button for View Dataset
        self.OpenDataset_icon = ImageTk.PhotoImage(
            Image.open(self.path+"/icons/OpenDataset_Frame.png"))
        openDataset_btn = ttk.Button(main_frame,
                                     text="Open Dataset",
                                     command=self.open_dataset,
                                     cursor="hand2",
                                     image=self.OpenDataset_icon,
                                     compound=LEFT
                                     )
        openDataset_btn.place(x=220, y=120, width=130, height=45)
        self.Logout_icon = ImageTk.PhotoImage(
            Image.open(self.path+"/icons/OpenDataset_Frame.png"))
        self.Logout_icon = ImageTk.PhotoImage(
            Image.open(self.path+"/icons/Icon=Logout_Frame, Color= Black.png"))
        logout_btn = ttk.Button(main_frame,
                                text="Logout",
                                command=self.logout,
                                cursor="hand2",
                                image=self.Logout_icon,
                                compound=LEFT
                                )
        logout_btn.place(x=220, y=180, width=130, height=45)
        # Style For TKK
        style = ttk.Style()
        style.configure("TButton",
                        font=("built titling", 9),
                        background='#fff',
                        foreground='#000')



    # Def for Opening Dataset
    def open_dataset(self):
        os.startfile("data")

    # Function Button
    def user_details(self):
        self.new_window = Toplevel(self.screen)
        self.app = User_Details(self.new_window)

    def train_data(self):
        #self.new_window = Toplevel(self.screen)
        #self.app = User_Details(self.new_window)
        Train.Train_Dataset()
        messagebox.showinfo("Result", "Training Datasets Completed!!", parent=self.screen)

    def face_data(self):
        Face_Recognition.Face_Recognition()

    def attendance_data(self):
        self.new_window = Toplevel(self.screen)
        self.app = Attendance_Details(self.new_window)

    def logout(self):
        self.screen.destroy()
if __name__ == "__main__":
    screen = Tk()
    obj = Dashboard_Admin(screen)


    def on_closing():

        exit = messagebox.askyesno("Update", "Do you want to quit?")
        if exit > 0:
            screen.destroy()
        elif not exit:
            return
    screen.protocol("WM_DELETE_WINDOW", on_closing)
    screen.mainloop()
