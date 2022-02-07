from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk


class Attendance_System:

    def __init__(self, screen):
        self.screen = screen
        self.screen.geometry("800x600+200+100")
        self.screen.title("Attendance System")
        self.screen.resizable(False, False)

        # bg_gradient
        img1 = Image.open(r"D:\FaceDetectionAndRecognition-v2\bg_gradient.jpg")
        img1 = img1.resize((800, 600), Image.ANTIALIAS)
        self.photo_img1 = ImageTk.PhotoImage(img1)
        bg_img = Label(self.screen, image=self.photo_img1)
        bg_img.place(x=0, y=0)

        Label(screen, text="Automatic Attendance System", font=("Montserrat Bold", 18), bg="pale turquoise",
              fg="SteelBlue4").place(x=155, y=70)

        global username_verify
        global password_verify

        username_verify = StringVar()
        password_verify = StringVar()

        global username_entry1
        global password_entry1

        # Username Label
        Label(text="Username", font=("Print Bold", 16)).place(x=213, y=138)
        # Username Entry
        username_entry1 = Entry(textvariable=username_verify)
        username_entry1.place(x=213, y=165)

        # Password Label
        Label(text="Password", font=("Print Bold", 16)).place(x=213, y=214)
        # Password Entry
        password_entry1 = Entry(show='*', textvariable=password_verify)
        password_entry1.place(x=213, y=236)

        # Login Button
        Button(text="Login", padx=10, pady=5,
               fg="white", bg="black", cursor="hand2").place(x=338,y=313)

        # Register Button
        Button(text="Register", padx=10, pady=5,
               fg="white", bg="black", cursor="hand2").place(x=238,y=313)



if __name__ == "__main__":
    screen = Tk()
    obj = Attendance_System(screen)
    screen.mainloop()
