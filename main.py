from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import mysql.connector
from Dashboard import Dashboard_Admin


def main():
    win = Tk()
    app = Attendance_System(win)
    win.mainloop()


class Attendance_System:

    def __init__(self, screen):
        self.screen = screen
        self.screen.geometry("350x400+550+200")
        self.screen.title("Login")
        self.screen.resizable(False, False)

        # bg_COLOR
        main_frame = Frame(self.screen, bg="#8ABECC")
        main_frame.place(x=0, y=0, width=350, height=400)

        # Text variable
        self.var_name = StringVar()
        self.var_Username = StringVar()
        self.var_contact = StringVar()
        self.var_email = StringVar()
        self.var_password = StringVar()
        self.var_confirmpassword = StringVar()
        self.var_checkbutton = IntVar()

        # Main Login Frame
        main_frame = Frame(self.screen, bg="White")
        main_frame.place(x=50, y=50, width=250, height=300)

        # Login Frame
        login_frame = LabelFrame(main_frame, bd=2, text="Login",
                                 font=("Heebo Regular", 18),
                                 labelanchor="n", bg="White", fg="#1E1844")
        login_frame.place(x=10, y=10, width=230, height=280)

        # Username Frame
        uframe = Frame(login_frame, bg="white")
        uframe.place(x=50, y=25, height=50, width=130)

        # Username Label & Entry
        User_label = Label(uframe, text="Username",
                           font=("print bold", 14),
                           bg="white", fg="#1E1844")
        User_label.pack()
        self.username_entry = ttk.Entry(uframe, textvariable=self.var_Username)
        self.username_entry.pack()

        # Username Icon Image
        uiconimg = Image.open(r"D:\FaceDetectionAndRecognition-v2\icons\Username_Frame.png")
        self.User_icon = ImageTk.PhotoImage(uiconimg)
        usericon = Label(uframe, image=self.User_icon, bg="white")
        usericon.place(x=5, y=-3)

        # Password Frame
        pframe = Frame(login_frame, bg="white")
        pframe.place(x=50, y=85, height=50, width=130)
        # Password  Label & Entry
        pass_label = Label(pframe, text="Password", font=("print bold", 14), bg="white")
        pass_label.pack()
        self.password_entry = ttk.Entry(pframe, show='*', textvariable=self.var_password)
        self.password_entry.pack()

        # Password Icon Image
        piconimg = Image.open(r"D:\FaceDetectionAndRecognition-v2\icons\Password_Frame.png")
        self.pass_icon = ImageTk.PhotoImage(piconimg)
        passwordicon = Label(pframe, image=self.pass_icon, bg="white")
        passwordicon.place(x=5, y=0)

        # Login Button
        lbutton = Button(login_frame, text="Login", cursor="hand2", command=self.login, bg="#1E1844", fg="white")
        lbutton.place(x=125, y=190, height=30, width=75)

        # Register Button
        rbutton = Button(login_frame, text="Register", command=self.register_window, cursor="hand2", bg="White",
                         borderwidth=2, highlightcolor="#1E1844")
        rbutton.place(x=25, y=190, height=30, width=75)



    # Login Function
    def login(self):
        ##########################################
        # Function to show Error and success
        def show_error():
            main_showFrame = Frame(self.screen)
            main_showFrame.place(x=90, y=240, height=21, width=180)
            self.error_icon = ImageTk.PhotoImage(
                Image.open(r"D:\FaceDetectionAndRecognition-v2\icons\Icon=ErrorR_Frame.png"))
            error_icon = Label(main_showFrame, image=self.error_icon, bg="white")
            error_icon.place(x=0, y=0)
            error_label = Label(main_showFrame, text="Invalid Username and Password!!", font=("open sans condensed", 9),
                                fg="red", bg="White")
            error_label.place(x=22, y=0)

        def show_success():
            main_showFrame = Frame(self.screen, bg="white")
            main_showFrame.place(x=90, y=240, height=21, width=180)
            self.success_icon = ImageTk.PhotoImage(
                Image.open(r"D:\FaceDetectionAndRecognition-v2\icons\Icon=Success_Frame.png"))
            success_icon = Label(main_showFrame, image=self.success_icon, bg="white")
            success_icon.place(x=20, y=2)
            success_label = Label(main_showFrame, text="Login Successfully!!", font=("open sans condensed", 9),
                                  fg="green", bg="White")
            success_label.place(x=47, y=0)

        def show_nothing():
            main_showFrame = Frame(self.screen, bg="white")
            main_showFrame.place(x=90, y=240, height=21, width=180)



        ############################################
        # Main Code
        if self.username_entry.get() == "" or self.password_entry.get() == "":
            show_error()
        else:
            conn = mysql.connector.connect(host="localhost",
                                           user="root",
                                           password="root",
                                           database="attendance_system"
                                           )
            my_cursor = conn.cursor()
            my_cursor.execute("select * from admin where username=%s and password=%s",
                              (self.username_entry.get(), self.password_entry.get()))
            row = my_cursor.fetchone()
            if row is None:
                show_error()
            else:
                show_success()
                self.username_entry.delete(0, END)
                self.password_entry.delete(0, END)

                self.screen = Toplevel(self.screen)
                self.app = Dashboard_Admin(self.screen)


            conn.commit()
            conn.close()


    def register_window(self):
        self.new_window = Toplevel(self.screen)
        self.app = Register_Admin(self.new_window)


class Register_Admin:

    def __init__(self, screen):
        self.screen = screen
        self.screen.geometry("500x600+150+100")
        self.screen.title("Register Admin")
        self.screen.resizable(False, False)

        # bg_gradient
        main_frame = Frame(self.screen, bg="#8ABECC")
        main_frame.place(x=0, y=0, width=500, height=600)


        # Text variable
        self.var_name = StringVar()
        self.var_Username = StringVar()
        self.var_contact = StringVar()
        self.var_email = StringVar()
        self.var_password = StringVar()
        self.var_confirmpassword = StringVar()
        self.var_checkbutton = IntVar()

        # Main Login Frame
        main_frame = Frame(self.screen, bg="white")
        main_frame.place(x=50, y=50, width=400, height=500)
        # Main Labelframe
        main_frame = LabelFrame(main_frame, text="Register", font=("Print Bold", 18), labelanchor="n", bg="white")
        main_frame.place(x=10, y=10, width=380, height=480)

        # Name Label and Entry
        name_label = Label(main_frame, text="Name", font=("Print Bold", 12), bg="white")
        name_label.place(x=55, y=45)
        name_entry = ttk.Entry(main_frame, textvariable=self.var_name, width=20)
        name_entry.place(x=30, y=70)

        # Name Icon Image
        uiconimg = Image.open(r"D:\FaceDetectionAndRecognition-v2\icons\Username_Frame.png")
        self.User_icon1 = ImageTk.PhotoImage(uiconimg)
        usericon1 = Label(main_frame, image=self.User_icon1, bg="white")
        usericon1.place(x=30, y=39)

        # Username Label & Entry
        username_label = Label(main_frame, text="Username", font=("Print Bold", 12), bg="white")
        username_label.place(x=230, y=45)
        username_entry = ttk.Entry(main_frame, textvariable=self.var_Username, width=20)
        username_entry.place(x=205, y=70)

        # Username Icon Image
        uiconimg = Image.open(r"D:\FaceDetectionAndRecognition-v2\icons\Username_Frame.png")
        self.User_icon2 = ImageTk.PhotoImage(uiconimg)
        usericon2 = Label(main_frame, image=self.User_icon2, bg="white")
        usericon2.place(x=205, y=39)

        # Contact Label & Entry
        contact_label = Label(main_frame, text="Contact", font=("Print Bold", 12), bg="white")
        contact_label.place(x=55, y=120)
        contact_entry = ttk.Entry(main_frame, textvariable=self.var_contact, width=20)
        contact_entry.place(x=30, y=145)

        # Contact Icon Image
        contacticonimg = Image.open(r"D:\FaceDetectionAndRecognition-v2\icons\Contact_Frame.png")
        self.Contact_icon = ImageTk.PhotoImage(contacticonimg)
        contacticon = Label(main_frame, image=self.Contact_icon, bg="white")
        contacticon.place(x=30, y=117)

        # Email Label & Entry
        email_label = Label(main_frame, text="Email", font=("Print Bold", 12), bg="white")
        email_label.place(x=230, y=120)
        email_entry = ttk.Entry(main_frame, textvariable=self.var_email, width=20)
        email_entry.place(x=205, y=145)

        #  Email Icon Image
        emailiconimg = Image.open(r"D:\FaceDetectionAndRecognition-v2\icons\Email_Frame.png")
        self.Email_icon = ImageTk.PhotoImage(emailiconimg)
        emailicon = Label(main_frame, image=self.Email_icon, bg="white")
        emailicon.place(x=205, y=117)

        # password Label & Entry
        password_label = Label(main_frame, text="Password", font=("Print Bold", 12), bg="white")
        password_label.place(x=55, y=195)
        password_entry = ttk.Entry(main_frame, textvariable=self.var_password, show="*", width=20)
        password_entry.place(x=30, y=220)

        # Password Icon Image
        piconimg = Image.open(r"D:\FaceDetectionAndRecognition-v2\icons\Password_Frame.png")
        self.pass_icon = ImageTk.PhotoImage(piconimg)
        passwordicon = Label(main_frame, image=self.pass_icon, bg="white")
        passwordicon.place(x=30, y=192)

        # confirm_password Label & Entry
        confirm_password_label = Label(main_frame, font=("Print Bold", 12), text="Confirm Password", bg="white")
        confirm_password_label.place(x=230, y=195)
        confirm_password_entry = ttk.Entry(main_frame, textvariable=self.var_confirmpassword, show="*", width=20)
        confirm_password_entry.place(x=205, y=220)

        # Password Icon Image
        piconimg = Image.open(r"D:\FaceDetectionAndRecognition-v2\icons\Password_Frame.png")
        self.pass1_icon = ImageTk.PhotoImage(piconimg)
        password1icon = Label(main_frame, image=self.pass1_icon, bg="white")
        password1icon.place(x=205, y=192)

        # Checkbtn For terms and Condition
        checkbtn = Checkbutton(main_frame, text="Agree Terms And Condition.", font=("Print Bold", 12),
                               variable=self.var_checkbutton, onvalue=1,
                               offvalue=0, takefocus=0,
                               command=self.button_activate,
                               bg="white")
        checkbtn.place(x=30, y=260)

        # Register Button
        rbutton = ttk.Button(main_frame, text="Register", command=self.register_user, cursor="hand2", width=20)
        rbutton.place(x=30, y=320)

    # FUnction Dec For Button
    def register_user(self):

        # Function For validation
        def show_error1():
            main_showFrame = Frame(self.screen, bg="white")
            main_showFrame.place(x=90, y=380, height=21, width=180)
            self.error_icon = ImageTk.PhotoImage(
                Image.open(r"D:\FaceDetectionAndRecognition-v2\icons\Icon=ErrorR_Frame.png"))
            error_icon = Label(main_showFrame, image=self.error_icon, bg="white")
            error_icon.place(x=0, y=0)
            error_label = Label(main_showFrame, text="All Field Required!!", font=("open sans condensed", 9),
                                fg="red", bg="White")
            error_label.place(x=22, y=0)

        def show_error2():
            main_showFrame = Frame(self.screen, bg="white")
            main_showFrame.place(x=90, y=380, height=21, width=300)
            self.error_icon = ImageTk.PhotoImage(
                Image.open(r"D:\FaceDetectionAndRecognition-v2\icons\Icon=ErrorR_Frame.png"))
            error_icon = Label(main_showFrame, image=self.error_icon, bg="white")
            error_icon.place(x=0, y=0)
            error_label = Label(main_showFrame, text="Password and Confirm Password must be same!!",
                                font=("open sans condensed", 9),
                                fg="red", bg="White")
            error_label.place(x=22, y=0)

        def show_error3():
            main_showFrame = Frame(self.screen, bg="white")
            main_showFrame.place(x=90, y=380, height=21, width=300)
            self.error_icon = ImageTk.PhotoImage(
                Image.open(r"D:\FaceDetectionAndRecognition-v2\icons\Icon=ErrorR_Frame.png"))
            error_icon = Label(main_showFrame, image=self.error_icon, bg="white")
            error_icon.place(x=0, y=0)
            error_label = Label(main_showFrame, text="User Already Exist!!", font=("open sans condensed", 9),
                                fg="red", bg="White")
            error_label.place(x=22, y=0)

        def show_success():
            main_showFrame = Frame(self.screen, bg="white")
            main_showFrame.place(x=90, y=380, height=21, width=300)
            self.success_icon = ImageTk.PhotoImage(
                Image.open(r"D:\FaceDetectionAndRecognition-v2\icons\Icon=Success_Frame.png"))
            success_icon = Label(main_showFrame, image=self.success_icon, bg="white")
            success_icon.place(x=0, y=2)
            success_label = Label(main_showFrame, text="Register Successfully!!", font=("open sans condensed", 9),
                                  fg="green", bg="White")
            success_label.place(x=22, y=0)

        if self.var_name.get() == "" or self.var_Username.get() == "" or self.var_contact.get() == "" or self.var_email.get() == "" or self.var_password.get() == "" or self.var_confirmpassword.get() == "":
            show_error1()
        elif self.var_password.get() != self.var_confirmpassword.get():
            show_error2()
        elif self.var_checkbutton.get() == 0:
            show_error1()

        else:
            conn = mysql.connector.connect(host="localhost",
                                           user="root",
                                           password="root",
                                           database="attendance_system"
                                           )
            my_cursor = conn.cursor()
            query = "select * from admin where username=%s"
            val = (self.var_Username.get(),)
            my_cursor.execute(query, val)
            row = my_cursor.fetchone()
            if row != None:
                show_error3()
            else:
                my_cursor.execute("insert into admin values (%s,%s,%s,%s,%s) ",
                                  (
                                      self.var_name.get(),
                                      self.var_Username.get(),
                                      self.var_contact.get(),
                                      self.var_email.get(),
                                      self.var_password.get()
                                  )
                                  )
                show_success()
                self.screen.after(500, lambda: self.screen.destroy())
            conn.commit()
            conn.close()


if __name__ == "__main__":
    main()
