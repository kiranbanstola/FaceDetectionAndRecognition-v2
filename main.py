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

        # bg_gradient
        img1 = Image.open(r"D:\FaceDetectionAndRecognition-v2\bg_gradient.jpg")
        img1 = img1.resize((350, 400), Image.ANTIALIAS)
        self.photo_img1 = ImageTk.PhotoImage(img1)
        bg_img = Label(self.screen, image=self.photo_img1)
        bg_img.place(x=0, y=0)

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
        self.username_entry = ttk.Entry(uframe, textvariable=self.var_Username)
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
        self.password_entry = ttk.Entry(pframe, show='*', textvariable=self.var_password)
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
        rbutton = ttk.Button(login_frame, text="Register", command=self.register_window, cursor="hand2")
        rbutton.place(x=25, y=190)

    # Login Function
    def login(self):
        """
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

    """
        # Main Code
        if self.username_entry.get() == "" or self.password_entry.get() == "":
                #show_username_error()
                #show_password_error()
                #show_Label_error()
                invalid_errorlabel = Label(self.screen, text="Invalid Data !!!", bg="white", fg="red")
                invalid_errorlabel.place(x=120, y=240)
        elif self.username_entry.get() == "aas" and self.password_entry.get() == "aas":
            #show_Label_Success()
            invalid_errorlabel = Label(self.screen, text="valid Data !!!", bg="white", fg="red")
            invalid_errorlabel.place(x=120, y=240)
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
                messagebox.showerror("Error", "Invalid Username and Password!!")
            else:
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
        self.screen.geometry("800x600+150+100")
        self.screen.title("Register Admin")
        self.screen.resizable(False, False)

        # bg_gradient
        img1 = Image.open(r"D:\FaceDetectionAndRecognition-v2\bg_gradient.jpg")
        img1 = img1.resize((800, 600), Image.ANTIALIAS)
        self.photo_img1 = ImageTk.PhotoImage(img1)
        bg_img = Label(self.screen, image=self.photo_img1)
        bg_img.place(x=0, y=0)

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
        main_frame.place(x=50, y=50, width=700, height=500)

        # Name Label and Entry
        name_label = Label(main_frame, text="Name", bg="white")
        name_label.place(x=50, y=50)
        name_entry = ttk.Entry(main_frame, textvariable=self.var_name, width=20)
        name_entry.place(x=50, y=70)

        # Username Label & Entry
        username_label = Label(main_frame, text="Username", bg="white")
        username_label.place(x=225, y=50)
        username_entry = ttk.Entry(main_frame, textvariable=self.var_Username, width=20)
        username_entry.place(x=225, y=70)

        # Contact Label & Entry
        contact_label = Label(main_frame, text="Contact", bg="white")
        contact_label.place(x=50, y=125)
        contact_entry = ttk.Entry(main_frame, textvariable=self.var_contact, width=20)
        contact_entry.place(x=50, y=145)

        # Email Label & Entry
        email_label = Label(main_frame, text="Email", bg="white")
        email_label.place(x=225, y=125)
        email_entry = ttk.Entry(main_frame, textvariable=self.var_email, width=20)
        email_entry.place(x=225, y=145)

        # password Label & Entry
        password_label = Label(main_frame, text="Password", bg="white")
        password_label.place(x=50, y=200)
        password_entry = ttk.Entry(main_frame, textvariable=self.var_password, show="*", width=20)
        password_entry.place(x=50, y=220)

        # confirm_password Label & Entry
        confirm_password_label = Label(main_frame, text="Confirm Password", bg="white")
        confirm_password_label.place(x=225, y=200)
        confirm_password_entry = ttk.Entry(main_frame, textvariable=self.var_confirmpassword, show="*", width=20)
        confirm_password_entry.place(x=225, y=220)

        # Checkbtn For terms and Condition
        checkbtn = Checkbutton(main_frame, text="Agree Terms And Condition.", variable=self.var_checkbutton, onvalue=1,
                               offvalue=0, takefocus=0,
                               bg="white")
        checkbtn.place(x=50, y=260)

        # Register Button
        rbutton = ttk.Button(main_frame, text="Register", command=self.register_user, cursor="hand2", width=20)
        rbutton.place(x=50, y=320)

    # FUnction Dec For Button
    def register_user(self):
        if self.var_name.get() == "" or self.var_Username.get() == "" or self.var_contact.get() == "" or self.var_email.get() == "" or self.var_password.get() == "" or self.var_confirmpassword.get() == "":
            messagebox.showerror("Error", "All Fields Are Required")
        elif self.var_password.get() != self.var_confirmpassword.get():
            messagebox.showerror("Error", "Password and Confirm Password must be Same")
        elif self.var_checkbutton.get() == 0:
            messagebox.showerror("Error", "Please, Agree Terms and Condition!")
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
                messagebox.showerror("Error", "User Already Exist!!")
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
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "Register Successfully!!!!")


if __name__ == "__main__":
    main()
