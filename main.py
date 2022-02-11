from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import mysql.connector


class Attendance_System:

    def __init__(self, screen):
        self.screen = screen
        self.screen.geometry("350x400+550+200")
        self.screen.title("Login")
        self.screen.resizable(False, False)

        # bg_gradient
        img1 = Image.open(r"D:\FaceDetectionAndRecognition-v2\bg_gradient.jpg")
        img1 = img1.resize((350, 400), Image.ANTIALIAS)
        self.photo_img1 = ImageTk.PhotoImage(img1)
        bg_img = Label(self.screen, image=self.photo_img1)
        bg_img.place(x=0, y=0)

        # global username_verify
        # global password_verify

        # username_verify = StringVar()
        # password_verify = StringVar()

        # global username_entry1
        # global password_entry1

        global username_verification
        global password_verification

        username_verification=StringVar()
        password_verification=StringVar()

        # Main Login Frame
        main_frame = Frame(self.screen, bg="white")
        main_frame.place(x=50, y=50, width=250, height=300)

        # Login Frame
        login_frame = LabelFrame(main_frame, bd=2, text="Login", font=("Print Bold", 18), labelanchor="n", bg="White")
        login_frame.place(x=10, y=10, width=230, height=280)

        # Username Frame
        uframe = Frame(login_frame, bg="white")
        uframe.place(x=50, y=40, height=50, width=130)

        # Username Label & Entry
        User_label = Label(uframe, text="Username", font=("Print Bold", 14), bg="white")
        User_label.pack()
        self.username_entry = ttk.Entry(uframe,textvariable=username_verification)
        self.username_entry.pack()

        # Username Icon Image
        uiconimg = Image.open(r"D:\FaceDetectionAndRecognition-v2\icons\Username_Frame.png")
        self.User_icon = ImageTk.PhotoImage(uiconimg)
        usericon = Label(uframe, image=self.User_icon, bg="white")
        usericon.place(x=5, y=-2)

        # Password Frame
        pframe = Frame(login_frame, bg="white")
        pframe.place(x=50, y=100, height=50, width=130)
        # Password  Label & Entry
        pass_label = Label(pframe, text="Password", font=("Print Bold", 14), bg="white")
        pass_label.pack()
        self.password_entry = ttk.Entry(pframe, show='*',textvariable=password_verification)
        self.password_entry.pack()

        # Password Icon Image
        piconimg = Image.open(r"D:\FaceDetectionAndRecognition-v2\icons\Password_Frame.png")
        self.pass_icon = ImageTk.PhotoImage(piconimg)
        passwordicon = Label(pframe, image=self.pass_icon, bg="white")
        passwordicon.place(x=5, y=0)

        # Login Button
        lbutton = ttk.Button(login_frame, text="Login", cursor="hand2", command=self.login)
        lbutton.place(x=125, y=190)

        # Register Button
        rbutton = ttk.Button(login_frame, text="Register", cursor="hand2")
        rbutton.place(x=25, y=190)

    #def login_verify(self):



    # Login Function
    def login(self):

        # Function to show Error and success
        def hide_username_error():
            username_error_icon.place_forget()

        def show_username_error():
            global username_error_icon
            username_error_iconimg = Image.open(r"D:\FaceDetectionAndRecognition-v2\icons\Error.png")
            self.username_error_icon = ImageTk.PhotoImage(username_error_iconimg)
            username_error_icon = Label(self.screen, image=self.username_error_icon, bg="white")
            username_error_icon.place(x=240, y=151)

        def hide_password_error():
            password_erroricon.place_forget()

        def show_password_error():
            global password_erroricon
            password_error_iconimg = Image.open(r"D:\FaceDetectionAndRecognition-v2\icons\Error.png")
            self.password_error_icon = ImageTk.PhotoImage(password_error_iconimg)
            password_erroricon = Label(self.screen, image=self.password_error_icon, bg="white")
            password_erroricon.place(x=240, y=210)

        def hide_Label_error():
            errorlabel.place_forget()

        def show_Label_error():
            global errorlabel
            errorlabel = Label(self.screen, text="*All Field Required", bg="white", fg="red")
            errorlabel.place(x=120, y=240)

        def hide_Label_Success():
            successlabel.place_forget()

        def show_Label_Success():
            global successlabel
            successlabel = Label(self.screen, text="Login Successfully", bg="white", fg="green")
            successlabel.place(x=120, y=240)

        def hide_Label_invalidpass():
            invalid_errorlabel.place_forget()

        def show_Label_invaliddata():
            global invalid_errorlabel
            invalid_errorlabel = Label(self.screen, text="Invalid Data !!!", bg="white", fg="red")
            invalid_errorlabel.place(x=120, y=240)




        ### Main Code
        if self.username_entry.get() == "" or self.password_entry.get() == "":
            show_username_error()
            show_password_error()
            show_Label_error()
        elif self.username_entry.get()=="aas" and self.password_entry.get()=="aas":
            show_Label_Success()
        else:
            show_username_error()
            show_password_error()
            show_Label_invaliddata()






if __name__ == "__main__":
    screen = Tk()
    obj = Attendance_System(screen)
    screen.mainloop()
