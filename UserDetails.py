import os
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import re

save_flag = 1


class User_Details:
    def __init__(self, screen):
        self.screen = screen
        self.screen.geometry("1280x720+150+75")
        self.screen.title("User Details")
        self.screen.resizable(False, False)
        self.photo_flag = -1
        main_frame = Frame(self.screen, bg="#8ABECC")
        main_frame.place(x=0, y=0, width=1280, height=720)

        Label(screen, text="Users Details", font=("Print Bold", 36), fg="SteelBlue4").place(relx=0.4, rely=0.01)

        main_frame = Frame(self.screen, bg="white", highlightthickness=2, highlightbackground="black")
        main_frame.place(x=50, y=100, width=1180, height=580)

        # Button for Back
        path = os.getcwd()
        self.Back_icon = ImageTk.PhotoImage(
            Image.open(path + "/icons/Back_Frame.png"))
        back_btn = ttk.Button(main_frame,
                              text="Back",
                              command=self.back_screen,
                              cursor="hand2",
                              image=self.Back_icon,
                              compound=LEFT)
        back_btn.place(x=50, y=30, width=100, height=35)

        # Variables Define
        self.var_userid = StringVar()
        self.var_username = StringVar()
        self.var_roll = StringVar()
        self.var_email = StringVar()
        self.var_dob = StringVar()
        self.var_phone = StringVar()
        self.var_gender = StringVar()

        # Variable for Search  Option
        self.var_searchentry = StringVar()

        # Upper Frame
        Upper_frame = LabelFrame(main_frame, bd=2, text="Add User", font=("Print Bold", 18),
                                 labelanchor="n",
                                 bg="white")
        Upper_frame.place(x=20, y=20, width=825, height=230)

        # Lower Frame
        Lower_frame = LabelFrame(main_frame, bd=2, text="User Details", font=("Print Bold", 18),
                                 labelanchor="n",
                                 bg="white")
        Lower_frame.place(x=20, y=260, width=1140, height=300)

        # Frame Containing User Information
        User_info_frame = Frame(Upper_frame, bg="white")
        User_info_frame.place(x=10, y=10, width=800, height=190)

        # User ID Label
        Userid_label = Label(User_info_frame, text="User ID:", font=("Montserrat semi-bold", 12), bg="white")
        Userid_label.grid(row=0, column=0, padx=10, pady=10)
        # User ID Entry
        Userid_entry = ttk.Entry(User_info_frame, textvariable=self.var_userid, width=10,
                                 font=("Montserrat semi-bold", 12))
        Userid_entry.grid(row=0, column=1, padx=10, pady=10)

        # User Name Label
        Username_label = Label(User_info_frame, text="Name:", font=("Montserrat semi-bold", 12), bg="white")
        Username_label.grid(row=0, column=2, padx=10, pady=10)
        # UserName Entry
        Username_entry = ttk.Entry(User_info_frame, textvariable=self.var_username, width=20,
                                   font=("Montserrat semi-bold", 12))
        Username_entry.grid(row=0, column=3, padx=10, pady=10)

        # Roll number Label
        Rollno_label = Label(User_info_frame, text="Roll no:", font=("Montserrat semi-bold", 12), bg="white")
        Rollno_label.grid(row=1, column=0, padx=10, pady=10)
        # Roll number Entry
        Rollno_entry = ttk.Entry(User_info_frame, textvariable=self.var_roll, width=10,
                                 font=("Montserrat semi-bold", 12))
        Rollno_entry.grid(row=1, column=1, padx=10, pady=10)

        # Email Label
        Email_label = Label(User_info_frame, text="Email:", font=("Montserrat semi-bold", 12), bg="white")
        Email_label.grid(row=1, column=2, padx=10, pady=10)
        # Email Entry
        Email_entry = ttk.Entry(User_info_frame, textvariable=self.var_email, width=20,
                                font=("Montserrat semi-bold", 12))
        Email_entry.grid(row=1, column=3, padx=10, pady=10)

        # Gender Label
        Gender_label = Label(User_info_frame, text="Gender:", font=("Montserrat semi-bold", 12), bg="white")
        Gender_label.grid(row=0, column=4, padx=10, pady=10)
        # Gender Entry
        r1 = ttk.Radiobutton(User_info_frame, variable=self.var_gender, text="Male", value="male")
        r1.grid(row=0, column=5, padx=0, pady=0)
        r2 = ttk.Radiobutton(User_info_frame, variable=self.var_gender, text="Female", value="female")
        r2.grid(row=0, column=6, padx=20, pady=0)
        r3 = ttk.Radiobutton(User_info_frame, variable=self.var_gender, text="Other", value="other")
        r3.grid(row=1, column=5, padx=0, pady=0)

        # DOB Label
        dob_label = Label(User_info_frame, text="DOB:", font=("Montserrat semi-bold", 12), bg="white")
        dob_label.grid(row=2, column=0, padx=10, pady=10)
        # DOB Entry
        dob_entry = ttk.Entry(User_info_frame, textvariable=self.var_dob, width=12, font=("Montserrat semi-bold", 10))
        dob_entry.grid(row=2, column=1, padx=10, pady=10)
        dob_entry.insert(0, "MM/DD/YYYY")
        # Phone Label
        Phone_label = Label(User_info_frame, text="Phone:", font=("Montserrat semi-bold", 12), bg="white")
        Phone_label.grid(row=2, column=2, padx=10, pady=10)
        # Phone Entry
        Phone_entry = ttk.Entry(User_info_frame, textvariable=self.var_phone, width=20,
                                font=("Montserrat semi-bold", 12))
        Phone_entry.grid(row=2, column=3, padx=10, pady=10)

        # Frame Containing Buttons
        Buttons_frame = Frame(Upper_frame, bg="white")
        Buttons_frame.place(x=50, y=150, width=750, height=50)
        # Reset Buttons
        Reset_btn = ttk.Button(Buttons_frame, command=self.reset_data, text="Reset", width=15, cursor="hand2")
        Reset_btn.grid(row=0, column=0, padx=15, pady=10)
        # Update Buttons
        Update_btn = ttk.Button(Buttons_frame, command=self.update_data, text="Update", width=15, cursor="hand2")
        Update_btn.grid(row=0, column=1, padx=15, pady=10)
        # Delete Buttons
        Delete_btn = ttk.Button(Buttons_frame, command=self.delete_data, text="Delete", width=15, cursor="hand2")
        Delete_btn.grid(row=0, column=2, padx=15, pady=10)
        # Save Buttons
        Save_btn = ttk.Button(Buttons_frame, command=self.add_data, text="Save", width=15, cursor="hand2")
        Save_btn.grid(row=0, column=3, padx=15, pady=10)
        # Take Photo Buttons
        Take_photo_btn = ttk.Button(Buttons_frame, command=self.generate_dataset, text="Take Photo", width=15,
                                    cursor="hand2")
        Take_photo_btn.grid(row=0, column=4, padx=15, pady=10)

        # Search System
        SearchLabel_frame = LabelFrame(main_frame, bd=2, text="Search Details", bg="white", labelanchor="n",
                                       font=("Print Bold", 18))
        SearchLabel_frame.place(x=875, y=50, width=250, height=150)

        # Details Label
        Details_label = Label(SearchLabel_frame, text="Enter ID:", font=("open sans", 12), bg="white")
        Details_label.place(x=10, y=20)

        # Details by input Entry
        Details_entry = ttk.Entry(SearchLabel_frame, textvariable=self.var_searchentry, width=10,
                                  font=("Montserrat semi-bold", 12))
        Details_entry.place(x=110, y=20)

        # Details by input button
        Search_btn = ttk.Button(SearchLabel_frame, command=self.search_data, text="Search", width=10)
        Search_btn.place(x=125, y=75)

        # Details by Show All  button
        Searchreset_btn = ttk.Button(SearchLabel_frame, command=self.fetch_data, text="Reset", width=10)
        Searchreset_btn.place(x=30, y=75)

        # Table Frame
        Table_Details_frame = Frame(Lower_frame, bg="white")
        Table_Details_frame.place(x=5, y=5, width=1130, height=265)

        scroll_x = ttk.Scrollbar(Table_Details_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(Table_Details_frame, orient=VERTICAL)

        self.user_table = ttk.Treeview(Table_Details_frame, columns=(
            "userid", "username", "roll", "email", "gender", "dob", "phone"), xscrollcommand=scroll_x.set,
                                       yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.user_table.xview)
        scroll_y.config(command=self.user_table.yview)

        # Display Text From Dommi Name
        self.user_table.heading("userid", text="User ID")
        self.user_table.heading("username", text="User Name")
        self.user_table.heading("roll", text="Roll No")
        self.user_table.heading("email", text="Email")
        self.user_table.heading("gender", text="Gender")
        self.user_table.heading("dob", text="Birth Date")
        self.user_table.heading("phone", text="Phone Number")
        self.user_table["show"] = "headings"
        self.user_table.column("userid", width=75)
        self.user_table.column("username", width=100)
        self.user_table.column("roll", width=50)
        self.user_table.column("email", width=120)
        self.user_table.column("gender", width=50)
        self.user_table.column("dob", width=100)
        self.user_table.pack(fill=BOTH, expand=1)
        self.user_table.bind("<ButtonRelease>", self.get_cursor)
        self.fetch_data()

    # Function Dec
    def add_data(self):
        if self.var_username.get() == "" or self.var_userid.get() == "" or self.var_roll.get() == "" or self.var_email.get() == "" or self.var_phone.get() == "" \
                or self.var_gender.get() == "" or self.var_dob.get() == "MM/DD/YY":
            messagebox.showerror("Error", "All field Required", parent=self.screen)
        elif not self.var_userid.get().isnumeric():
            messagebox.showerror("Error", "Enter number for ID", parent=self.screen)
        elif not self.var_roll.get().isnumeric():
            messagebox.showerror("Error", "Enter number for roll", parent=self.screen)
        elif not self.var_phone.get().isnumeric():
            messagebox.showerror("Error", "Enter valid phone number", parent=self.screen)
        elif not self.check_email(self.var_email.get()):
            messagebox.showerror("Error", "Invalid email", parent=self.screen)
        elif not self.is_date(self.var_dob.get()):
            messagebox.showerror("Error", "Invalid Date!!Enter Date in MM/DD/YY format", parent=self.screen)
        elif self.photo_flag == -1:
            messagebox.showerror("Error", "Take Photo", parent=self.screen)
        else:
            try:
                conn = mysql.connector.connect(host="localhost",
                                               user="root",
                                               password="root",
                                               database="attendance_system"
                                               )
                my_cursor = conn.cursor()
                my_cursor.execute("insert into users values(%s,%s,%s,%s,%s,%s,%s)", (
                    self.var_userid.get(),
                    self.var_username.get(),
                    self.var_roll.get(),
                    self.var_email.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_phone.get(),
                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                global save_flag
                save_flag = 0
                messagebox.showinfo("Success", "Student Details Added Successfully", parent=self.screen)

            except Exception as es:
                messagebox.showerror("Error", f"Due to :{str(es)}", parent=self.screen)
                self.delete_photo(self.var_userid.get())

    # Function to Fetch Data From Database to Details
    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost",
                                       user="root",
                                       password="root",
                                       database="attendance_system"
                                       )
        my_cursor = conn.cursor()
        my_cursor.execute("select * from users")
        data = my_cursor.fetchall()

        if len(data) != 0:
            self.user_table.delete(*self.user_table.get_children())
            for i in data:
                self.user_table.insert("", END, values=i)
            conn.commit()
        conn.close()

    # Function to update Data
    def get_cursor(self, event=""):
        cursor_focus = self.user_table.focus()
        content = self.user_table.item(cursor_focus)
        data = content["values"]
        self.var_userid.set(data[0]),
        self.var_username.set(data[1]),
        self.var_roll.set(data[2]),
        self.var_email.set(data[3]),
        self.var_gender.set(data[4]),
        self.var_dob.set(data[5]),
        self.var_phone.set(data[6]),

    # Update Function
    def update_data(self):
        if self.var_username.get() == "" or self.var_userid.get() == "" or self.var_roll.get() == "" or self.var_email.get() == "" or self.var_phone.get() == "" \
                or self.var_gender.get() == "" or self.var_dob.get() == "":
            messagebox.showerror("Error", "All field Required", parent=self.screen)
        elif self.var_userid.get().isnumeric() == False:
            messagebox.showerror("Error", "Enter number for ID", parent=self.screen)
        elif self.var_roll.get().isnumeric() == False:
            messagebox.showerror("Error", "Enter number for roll", parent=self.screen)
        elif self.var_phone.get().isnumeric() == False:
            messagebox.showerror("Error", "Enter valid phone number", parent=self.screen)
        elif self.check_email(self.var_email.get()) == False:
            messagebox.showerror("Error", "Invalid email", parent=self.screen)
        else:
            try:
                Update = messagebox.askyesno("Update", "Do you want to update details?", parent=self.screen)
                if Update > 0:
                    conn = mysql.connector.connect(host="localhost",
                                                   user="root",
                                                   password="root",
                                                   database="attendance_system"
                                                   )
                    my_cursor = conn.cursor()
                    my_cursor.execute(
                        "update users set Username=%s, Rollno=%s, Email=%s, Gender=%s, DOB=%s, Phone=%s where Userid=%s ",
                        (
                            self.var_username.get(),
                            self.var_roll.get(),
                            self.var_email.get(),
                            self.var_gender.get(),
                            self.var_dob.get(),
                            self.var_phone.get(),
                            self.var_userid.get()
                        ))
                else:
                    if not Update:
                        return

                messagebox.showinfo("Success", "Student update Successfully", parent=self.screen)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error", f"Due to :{str(es)}", parent=self.screen)

    # Delete Function
    def delete_data(self):
        if self.var_userid.get() == "":
            messagebox.showerror("Error", "Nothing to Delete", parent=self.screen)
        else:
            try:
                delete = messagebox.askyesno("Delete Details", "Confirm Delete?", parent=self.screen)
                if delete > 0:
                    conn = mysql.connector.connect(host="localhost",
                                                   user="root",
                                                   password="root",
                                                   database="attendance_system"
                                                   )
                    my_cursor = conn.cursor()
                    query = "delete from users where Userid=%s"
                    val = (self.var_userid.get(),)
                    my_cursor.execute(query, val)
                else:
                    if not delete:
                        return
                self.delete_photo(self.var_userid.get())
                conn.commit()
                self.fetch_data()
                conn.close()

                messagebox.showinfo("Deleted", "Successfully Deleted", parent=self.screen)

            except Exception as es:
                messagebox.showerror("Error", f"Due to :{str(es)}", parent=self.screen)

    # Reset Function
    def reset_data(self):
        self.var_userid.set("")
        self.var_username.set("")
        self.var_roll.set("")
        self.var_email.set("")
        self.var_gender.set("")
        self.var_dob.set("")
        self.var_phone.set("")

    # Generate data set and take Sample using Opencv
    def generate_dataset(self):

        if self.var_username.get() == "":
            messagebox.showerror("Error", "Username required", parent=self.screen)

        elif self.var_userid.get() == "":
            messagebox.showerror("Error", "ID required", parent=self.screen)
        else:
            try:
                # Load haarcascade_frontalface_default from opencv
                face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray, 1.3, 5)
                    # Scaling Factor = 1.3  Minimum Neighbor = 5
                    for (x, y, w, h) in faces:
                        face_cropped = img[y:y + h, x:x + w]
                        return face_cropped

                cap = cv2.VideoCapture(0)
                img_id = 0
                while True:
                    ret, my_frame = cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id += 1
                        face = cv2.resize(face_cropped(my_frame), (450, 450))
                        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                        file_name_path = "data/user." + str(self.var_userid.get()) + "." + str(img_id) + ".jpg"
                        cv2.imwrite(file_name_path, face)
                        cv2.putText(face, str(img_id), (50, 50), cv2.FONT_ITALIC, 2, (0, 255, 0), 2)
                        cv2.imshow("Cropped Face", face)

                    if cv2.waitKey(1) == 13 or int(img_id) == 100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                global save_flag
                save_flag = -1
                messagebox.showinfo("Result", "Generating Dataset Completed!!!!", parent=self.screen)
            except Exception as es:
                messagebox.showerror("Error", f"Due to :{str(es)}", parent=self.screen)
            self.photo_flag = 0

    # Search Function
    def search_data(self):
        conn = mysql.connector.connect(host="localhost",
                                       user="root",
                                       password="root",
                                       database="attendance_system"
                                       )
        my_cursor = conn.cursor()
        my_cursor.execute("select * from users where Userid= " + str(self.var_searchentry.get()) + "")
        data = my_cursor.fetchall()

        if len(data) != 0:
            self.user_table.delete(*self.user_table.get_children())
            for i in data:
                self.user_table.insert("", END, values=i)
            conn.commit()
        conn.close()

    def delete_photo(self, id):
        path = os.getcwd()
        for filename in os.listdir(path + '/data'):
            if filename.startswith('user.' + str(id)):
                os.remove(path + '/data/' + filename)

    def back_screen(self):
        global save_flag
        if save_flag == 0 or save_flag == 1:
            self.screenscreen.destroy()
        else:
            exit = messagebox.askyesno("Update", "Do you want to quit without saving?")
            if exit > 0:
                self.delete_photo(self.var_userid.get())
                self.screen.destroy()
            elif not exit:
                return

    def check_email(self, email):
        regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        if re.search(regex, email):
            return True
        else:
            return False

    def is_date(self, date):
        regex = "^([1-9]|1[0-2])(/|-)([1-9]|1[0-9]|2[0-9]|3[0-1])(/|-)(19[0-9][0-9]|20[0-2][0-9])$"
        if re.search(regex, date):
            return True
        else:
            return False


if __name__ == "__main__":
    screen = Tk()
    obj = User_Details(screen)


    def on_closing():
        if save_flag == 0 or save_flag == 1:
            screen.destroy()
        else:
            exit = messagebox.askyesno("Update", "Do you want to quit without saving?")
            if exit > 0:
                obj.delete_photo(obj.var_userid.get())
                screen.destroy()
            elif not exit:
                return


    screen.protocol("WM_DELETE_WINDOW", on_closing)
    screen.mainloop()
