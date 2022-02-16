from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class User_Details:
    def __init__(self, screen):
        self.screen = screen
        self.screen.geometry("1280x720+150+75")
        self.screen.title("User Details")
        self.screen.resizable(False, False)

        img1 = Image.open(r"D:\FaceDetectionAndRecognition-v2\bg_gradient.jpg")
        img1 = img1.resize((1280, 720), Image.ANTIALIAS)
        self.photo_img1 = ImageTk.PhotoImage(img1)
        bg_img = Label(self.screen, image=self.photo_img1)
        bg_img.place(x=0, y=0)

        Label(screen, text="Users Details", font=("Print Bold", 36), fg="SteelBlue4").place(relx=0.4, rely=0.01)

        main_frame = Frame(self.screen, bg="white", highlightthickness=2, highlightbackground="black")
        main_frame.place(x=50, y=100, width=1180, height=580)

        # Variables Define
        self.var_faculty = StringVar()
        self.var_year = StringVar()
        self.var_sem = StringVar()
        self.var_course = StringVar()
        self.var_userid = StringVar()
        self.var_username = StringVar()
        self.var_roll = StringVar()
        self.var_email = StringVar()
        self.var_dob = StringVar()
        self.var_phone = StringVar()
        self.var_gender = StringVar()
        self.var_photoRB = StringVar()

        # Variable for Search  Option
        # self.var_searchby = StringVar()
        self.var_searchentry = StringVar()
        # self.var_searchentry = StringVar()

        # User Search Frame
        Left_frame = LabelFrame(main_frame, bd=2, text="Search User", font=("Print Bold", 18), labelanchor="n",
                                bg="white")
        Left_frame.place(x=20, y=20, width=560, height=540)

        # Content Inside Left Frame-- Button Entry Label etc
        # Left_frame = LabelFrame(Left_frame, bd=2, text="Search User", font=("Print Bold", 18), labelanchor="n",bg="white")
        # Left_frame.place(x=20, y=20, width=560, height=540)

        # Frame Containing Faculty,Year,Semester,Course
        Course_info_frame = Frame(Left_frame, bg="white")
        Course_info_frame.place(x=5, y=5, width=545, height=100)

        # Faculty Label
        Faculty_label = Label(Course_info_frame, text="Faculty:", font=("Montserrat semi-bold", 12), bg="white")
        Faculty_label.grid(row=0, column=0, padx=10, pady=10, sticky=W)
        # Faculty ComboBox
        Faculty_combo = ttk.Combobox(Course_info_frame, textvariable=self.var_faculty, font=("Montserrat medium", 10),
                                     width=14, state="readonly")
        Faculty_combo["values"] = ("Select Faculty", "BSC.CSIT", "BIT", "PROFESSOR", "STAFF")
        Faculty_combo.current(0)
        Faculty_combo.grid(row=0, column=1, padx=20, pady=10)

        # Year Label
        Year_label = Label(Course_info_frame, text="Year:", font=("Montserrat semi-bold", 12), bg="white")
        Year_label.grid(row=0, column=2, padx=10, pady=10)
        # Year ComboBox
        Year_combo = ttk.Combobox(Course_info_frame, textvariable=self.var_year, font=("Montserrat medium", 10),
                                  width=14, state="readonly")
        Year_combo["values"] = ("Select Year", "2070", "2071", "2072", "2073", "2074", "2075", "2076", "2077", "2078")
        Year_combo.current(0)
        Year_combo.grid(row=0, column=3, padx=10, pady=10)

        # Semester Label
        Semester_label = Label(Course_info_frame, text="Semester:", font=("Montserrat semi-bold", 12), bg="white")
        Semester_label.grid(row=1, column=0, padx=10, pady=10)
        # Year ComboBox
        Semester_combo = ttk.Combobox(Course_info_frame, textvariable=self.var_sem, font=("Montserrat medium", 10),
                                      width=14, state="readonly")
        Semester_combo["values"] = (
            "Select Semester", "First", "Second", "Third", "Fourth", "Fifth", "Sixth", "Seventh", "Eight")
        Semester_combo.current(0)
        Semester_combo.grid(row=1, column=1, padx=10, pady=10)

        # Course Label
        Course_label = Label(Course_info_frame, text="Course:", font=("Montserrat semi-bold", 12), bg="white")
        Course_label.grid(row=1, column=2, padx=10, pady=10)
        # Year ComboBox
        Course_combo = ttk.Combobox(Course_info_frame, textvariable=self.var_course, font=("Montserrat medium", 10),
                                    width=14, state="readonly")
        Course_combo["values"] = (
            "Select Course", "Java", "Data Mining", "Principle of Management", "Network Security")
        Course_combo.current(0)
        Course_combo.grid(row=1, column=3, pady=10)

        # End of Frame Containing Faculty,Year,Semester,Course

        # Frame Containing User Information
        User_info_frame = Frame(Left_frame, bg="white")
        User_info_frame.place(x=5, y=110, width=545, height=375)

        # User ID Label
        Userid_label = Label(User_info_frame, text="User ID:", font=("Montserrat semi-bold", 12), bg="white")
        Userid_label.grid(row=0, column=0, padx=10, pady=10)
        # User ID Entry
        Userid_entry = ttk.Entry(User_info_frame, textvariable=self.var_userid, width=10,
                                 font=("Montserrat semi-bold", 12))
        Userid_entry.grid(row=0, column=1, padx=10, pady=10)

        # User Name Label
        Username_label = Label(User_info_frame, text="User Name:", font=("Montserrat semi-bold", 12), bg="white")
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
        Gender_label.grid(row=2, column=0, padx=10, pady=10)
        # Gender Entry
        r1 = ttk.Radiobutton(User_info_frame, variable=self.var_gender, text="Male", value="male")
        r1.grid(row=2, column=1, padx=0, pady=0)
        r2 = ttk.Radiobutton(User_info_frame, variable=self.var_gender, text="Female", value="female")
        r2.grid(row=2, column=2, padx=0, pady=0)
        # r3 = ttk.Radiobutton(User_info_frame, text="Other", value="other")
        # r3.grid(row=2, column=3, padx=0, pady=0)

        # DOB Label
        dob_label = Label(User_info_frame, text="DOB:", font=("Montserrat semi-bold", 12), bg="white")
        dob_label.grid(row=3, column=0, padx=10, pady=10)
        # DOB Entry
        dob_entry = ttk.Entry(User_info_frame, textvariable=self.var_dob, width=10, font=("Montserrat semi-bold", 12))
        dob_entry.grid(row=3, column=1, padx=10, pady=10)

        # Phone Label
        Phone_label = Label(User_info_frame, text="Phone:", font=("Montserrat semi-bold", 12), bg="white")
        Phone_label.grid(row=3, column=2, padx=10, pady=10)
        # Phone Entry
        Phone_entry = ttk.Entry(User_info_frame, textvariable=self.var_phone, width=20,
                                font=("Montserrat semi-bold", 12))
        Phone_entry.grid(row=3, column=3, padx=10, pady=10)

        # Radio Buttons For Photo
        Photo_label = Label(User_info_frame, text="Photo:", font=("Montserrat semi-bold", 12), bg="white")
        Photo_label.grid(row=4, column=0, padx=10, pady=10)

        RB1 = ttk.Radiobutton(User_info_frame, variable=self.var_photoRB, text="Photo", value="Yes")
        RB1.grid(row=4, column=1, padx=20, pady=0)

        RB2 = ttk.Radiobutton(User_info_frame, variable=self.var_photoRB, text="No Photo", value="No")
        RB2.grid(row=4, column=2, padx=20, pady=20)

        # Frame Containing Buttons
        Buttons_frame = Frame(User_info_frame, bg="white")
        Buttons_frame.place(x=5, y=250, width=535, height=125)
        # Reset Buttons
        Reset_btn = ttk.Button(Buttons_frame, command=self.reset_data, text="Reset", width=15)
        Reset_btn.grid(row=0, column=1, padx=15, pady=20)
        # Update Buttons
        Update_btn = ttk.Button(Buttons_frame, command=self.update_data, text="Update", width=15)
        Update_btn.grid(row=0, column=2, padx=15, pady=20)
        # Delete Buttons
        Delete_btn = ttk.Button(Buttons_frame, command=self.delete_data, text="Delete", width=15, )
        Delete_btn.grid(row=0, column=3, padx=15, pady=20)
        # Save Buttons
        Save_btn = ttk.Button(Buttons_frame, command=self.add_data, text="Save", width=15)
        Save_btn.grid(row=0, column=4, padx=15, pady=20)
        # Take Photo Buttons
        Take_photo_btn = ttk.Button(Buttons_frame, command=self.generate_dataset, text="Take Photo", width=15)
        Take_photo_btn.grid(row=1, column=2, padx=15, pady=20)
        # Update Photo Buttons
        Update_photo_btn = ttk.Button(Buttons_frame, command=self.update_data, text="Update Photo", width=15)
        Update_photo_btn.grid(row=1, column=3, padx=15, pady=20)

        # User_Details Frame
        Right_frame = LabelFrame(main_frame, bd=2, text="User Details", font=("Print Bold", 18), labelanchor="n",
                                 bg="white")
        Right_frame.place(x=590, y=20, width=560, height=540)

        # Search System
        User_Details_frame = Frame(Right_frame, bg="white")
        User_Details_frame.place(x=5, y=10, width=545, height=50)

        # Details Label
        Details_label = Label(User_Details_frame, text="Enter ID:", font=("Montserrat semi-bold", 12), bg="white")
        Details_label.grid(row=0, column=0, padx=10, pady=10)
        # Details Combo
        # Details_combo = ttk.Combobox(User_Details_frame, textvariable=self.var_searchby, font=("Montserrat medium", 10),
        # width=10, state="readonly")
        # Details_combo["values"] = ("Select", "Rollno", "Userid")
        # Details_combo.current(0)
        # Details_combo.grid(row=0, column=1, padx=10, pady=10)

        # Details by input Entry
        Details_entry = ttk.Entry(User_Details_frame, textvariable=self.var_searchentry, width=10,
                                  font=("Montserrat semi-bold", 12))
        Details_entry.grid(row=0, column=1, padx=10, pady=10)

        # Details by input button
        Search_btn = ttk.Button(User_Details_frame, command=self.search_data, text="Search", width=10)
        Search_btn.grid(row=0, column=4, padx=10, pady=10)

        # Details by Show All  button
        Searchreset_btn = ttk.Button(User_Details_frame, command=self.fetch_data, text="Reset", width=10)
        Searchreset_btn.grid(row=0, column=5, padx=10, pady=10)

        # Table Frame
        Table_Details_frame = Frame(Right_frame, bg="white")
        Table_Details_frame.place(x=5, y=80, width=545, height=425)

        scroll_x = ttk.Scrollbar(Table_Details_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(Table_Details_frame, orient=VERTICAL)

        self.user_table = ttk.Treeview(Table_Details_frame, columns=(
            "userid", "username", "roll", "year", "sem", "course", "faculty", "email", "gender", "dob", "phone",
            "photo"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.user_table.xview)
        scroll_y.config(command=self.user_table.yview)

        # Display Text From Dommi Name
        self.user_table.heading("faculty", text="Faculty")
        self.user_table.heading("year", text="Year")
        self.user_table.heading("sem", text="Semester")
        self.user_table.heading("course", text="Course")
        self.user_table.heading("userid", text="User ID")
        self.user_table.heading("username", text="User Name")
        self.user_table.heading("roll", text="Roll No")
        self.user_table.heading("email", text="Email")
        self.user_table.heading("gender", text="Gender")
        self.user_table.heading("dob", text="Birth Date")
        self.user_table.heading("phone", text="Phone Number")
        self.user_table.heading("photo", text="Photo Sample")
        self.user_table["show"] = "headings"

        self.user_table.column("faculty", width=75)
        self.user_table.column("year", width=75)
        self.user_table.column("sem", width=75)
        self.user_table.column("course", width=75)
        self.user_table.column("userid", width=75)
        self.user_table.column("username", width=100)
        self.user_table.column("roll", width=50)
        self.user_table.column("email", width=120)
        self.user_table.column("gender", width=50)
        self.user_table.column("dob", width=100)
        self.user_table.column("phone", width=100)
        self.user_table.column("photo", width=100)

        self.user_table.pack(fill=BOTH, expand=1)
        self.user_table.bind("<ButtonRelease>", self.get_cursor)
        self.fetch_data()

    # Function Dec
    def add_data(self):
        if self.var_faculty.get() == "Select Faculty" or self.var_username.get() == "" or self.var_userid.get() == "":
            messagebox.showerror("Error", "All field Required", parent=self.screen)
        else:
            try:
                conn = mysql.connector.connect(host="localhost",
                                               user="root",
                                               password="root",
                                               database="attendance_system"
                                               )
                my_cursor = conn.cursor()
                my_cursor.execute("insert into users values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
                    self.var_userid.get(),
                    self.var_username.get(),
                    self.var_roll.get(),
                    self.var_year.get(),
                    self.var_sem.get(),
                    self.var_course.get(),
                    self.var_faculty.get(),
                    self.var_email.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_phone.get(),
                    self.var_photoRB.get(),
                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Student Details Added Successfully", parent=self.screen)

            except Exception as es:
                messagebox.showerror("Error", f"Due to :{str(es)}", parent=self.screen)

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
        self.var_year.set(data[3]),
        self.var_faculty.set(data[6]),
        self.var_sem.set(data[4]),
        self.var_course.set(data[5]),
        self.var_email.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_phone.set(data[10]),
        self.var_photoRB.set(data[11]),

    # Update Function
    def update_data(self):
        if self.var_faculty.get() == "Select Faculty" or self.var_username.get() == "" or self.var_userid.get() == "":
            messagebox.showerror("Error", "All field Required", parent=self.screen)
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
                        "update users set Username=%s, Rollno=%s, Year=%s, Faculty=%s, Semester=%s, Course=%s, Email=%s, Gender=%s, DOB=%s, Phone=%s, Photo=%s where Userid=%s ",
                        (
                            self.var_username.get(),
                            self.var_roll.get(),
                            self.var_year.get(),
                            self.var_sem.get(),
                            self.var_course.get(),
                            self.var_faculty.get(),
                            self.var_email.get(),
                            self.var_gender.get(),
                            self.var_dob.get(),
                            self.var_phone.get(),
                            self.var_photoRB.get(),
                            self.var_userid.get()
                        ))
                else:
                    if not Update:
                        return

                messagebox.showinfo("Success", "Student update Sucessfully", parent=self.screen)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error", f"Due to :{str(es)}", parent=self.screen)

    # Delete Function
    def delete_data(self):
        if self.var_userid.get() == "":
            messagebox.showerror("Error", "Student id must be required", parent=self.screen)
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
        self.var_year.set("Select Year")
        self.var_faculty.set("Select Faculty")
        self.var_sem.set("Select Semester")
        self.var_course.set("Select Course")
        self.var_email.set("")
        self.var_gender.set("")
        self.var_dob.set("")
        self.var_phone.set("")
        self.var_photoRB.set("")

    # Generate data set and take Sample using Opencv
    def generate_dataset(self):
        if self.var_faculty.get() == "Select Faculty" or self.var_username.get() == "" or self.var_userid.get() == "":
            messagebox.showerror("Error", "All field Required", parent=self.screen)
        else:
            try:
                conn = mysql.connector.connect(host="localhost",
                                               user="root",
                                               password="root",
                                               database="attendance_system"
                                               )
                my_cursor = conn.cursor()
                my_cursor.execute("select * from users")
                myresult = my_cursor.fetchall()
                id = 0
                for x in myresult:
                    id += 1
                my_cursor.execute(
                    "update users set Username=%s, Rollno=%s, Year=%s, Faculty=%s, Semester=%s, Course=%s, Email=%s, Gender=%s, DOB=%s, Phone=%s, Photo=%s where Userid=%s ",
                    (
                        self.var_username.get(),
                        self.var_roll.get(),
                        self.var_year.get(),
                        self.var_sem.get(),
                        self.var_course.get(),
                        self.var_faculty.get(),
                        self.var_email.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_phone.get(),
                        self.var_photoRB.get(),
                        self.var_userid.get() == id + 1
                    ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

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
                        file_name_path = "data/user." + str(id) + "." + str(img_id) + ".jpg"
                        cv2.imwrite(file_name_path, face)
                        cv2.putText(face, str(img_id), (50, 50), cv2.FONT_ITALIC, 2, (0, 255, 0), 2)
                        cv2.imshow("Cropped Face", face)

                    if cv2.waitKey(1) == 13 or int(img_id) == 100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result", "Generating Dataset Completed!!!!")
            except Exception as es:
                messagebox.showerror("Error", f"Due to :{str(es)}", parent=self.screen)

    # Search Function
    def search_data(self):
        conn = mysql.connector.connect(host="localhost",
                                       user="root",
                                       password="root",
                                       database="attendance_system"
                                       )
        my_cursor = conn.cursor()
        # my_cursor.execute("select * from users where " + str(self.var_searchby.get()) + " LIKE '%" + str(self.var_searchentry.get()) + "%'")
        my_cursor.execute("select * from users where Userid= " + str(self.var_searchentry.get()) + "")
        data = my_cursor.fetchall()

        if len(data) != 0:
            self.user_table.delete(*self.user_table.get_children())
            for i in data:
                self.user_table.insert("", END, values=i)
            conn.commit()
        conn.close()


if __name__ == "__main__":
    screen = Tk()
    obj = User_Details(screen)
    screen.mainloop()
