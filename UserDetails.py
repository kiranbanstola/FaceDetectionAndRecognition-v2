from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk


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
        Faculty_combo = ttk.Combobox(Course_info_frame, font=("Montserrat medium", 10), width=14, state="readonly")
        Faculty_combo["values"] = ("Select Faculty", "BSC.CSIT", "BIT", "PROFESSOR", "STAFF")
        Faculty_combo.current(0)
        Faculty_combo.grid(row=0, column=1, padx=20, pady=10)

        # Year Label
        Year_label = Label(Course_info_frame, text="Year:", font=("Montserrat semi-bold", 12), bg="white")
        Year_label.grid(row=0, column=2, padx=10, pady=10)
        # Year ComboBox
        Year_combo = ttk.Combobox(Course_info_frame, font=("Montserrat medium", 10), width=14, state="readonly")
        Year_combo["values"] = ("Select Year", "2070", "2071", "2072", "2073", "2074", "2075", "2076", "2077", "2078")
        Year_combo.current(0)
        Year_combo.grid(row=0, column=3, padx=10, pady=10)

        # Semester Label
        Semester_label = Label(Course_info_frame, text="Semester:", font=("Montserrat semi-bold", 12), bg="white")
        Semester_label.grid(row=1, column=0, padx=10, pady=10)
        # Year ComboBox
        Semester_combo = ttk.Combobox(Course_info_frame, font=("Montserrat medium", 10), width=14, state="readonly")
        Semester_combo["values"] = (
            "Select Semester", "First", "Second", "Third", "Fourth", "Fifth", "Sixth", "Seventh", "Eight")
        Semester_combo.current(0)
        Semester_combo.grid(row=1, column=1, padx=10, pady=10)

        # Course Label
        Course_label = Label(Course_info_frame, text="Course:", font=("Montserrat semi-bold", 12), bg="white")
        Course_label.grid(row=1, column=2, padx=10, pady=10)
        # Year ComboBox
        Course_combo = ttk.Combobox(Course_info_frame, font=("Montserrat medium", 10), width=14, state="readonly")
        Course_combo["values"] = (
            "Select Semester", "Java", "Data Mining", "Principle of Management", "Network Security")
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
        Userid_entry = ttk.Entry(User_info_frame, width=10, font=("Montserrat semi-bold", 12))
        Userid_entry.grid(row=0, column=1, padx=10, pady=10)

        # User Name Label
        Username_label = Label(User_info_frame, text="User Name:", font=("Montserrat semi-bold", 12), bg="white")
        Username_label.grid(row=0, column=2, padx=10, pady=10)
        # User Name Entry
        Username_entry = ttk.Entry(User_info_frame, width=20, font=("Montserrat semi-bold", 12))
        Username_entry.grid(row=0, column=3, padx=10, pady=10)

        # Roll number Label
        Rollno_label = Label(User_info_frame, text="Roll no:", font=("Montserrat semi-bold", 12), bg="white")
        Rollno_label.grid(row=1, column=0, padx=10, pady=10)
        # Roll number Entry
        Rollno_entry = ttk.Entry(User_info_frame, width=10, font=("Montserrat semi-bold", 12))
        Rollno_entry.grid(row=1, column=1, padx=10, pady=10)

        # Email Label
        Email_label = Label(User_info_frame, text="Email:", font=("Montserrat semi-bold", 12), bg="white")
        Email_label.grid(row=1, column=2, padx=10, pady=10)
        # Email Entry
        Email_entry = ttk.Entry(User_info_frame, width=20, font=("Montserrat semi-bold", 12))
        Email_entry.grid(row=1, column=3, padx=10, pady=10)

        # Gender Label
        Gender_label = Label(User_info_frame, text="Gender:", font=("Montserrat semi-bold", 12), bg="white")
        Gender_label.grid(row=2, column=0, padx=10, pady=10)
        # Gender Entry
        r1 = ttk.Radiobutton(User_info_frame, text="Male", value="male")
        r1.grid(row=2, column=1, padx=0, pady=0)
        r2 = ttk.Radiobutton(User_info_frame, text="Female", value="female")
        r2.grid(row=2, column=2, padx=0, pady=0)
        # r3 = ttk.Radiobutton(User_info_frame, text="Other", value="other")
        # r3.grid(row=2, column=3, padx=0, pady=0)

        # DOB Label
        dob_label = Label(User_info_frame, text="DOB:", font=("Montserrat semi-bold", 12), bg="white")
        dob_label.grid(row=3, column=0, padx=10, pady=10)
        # DOB Entry
        dob_entry = ttk.Entry(User_info_frame, width=10, font=("Montserrat semi-bold", 12))
        dob_entry.grid(row=3, column=1, padx=10, pady=10)

        # Phone Label
        Phone_label = Label(User_info_frame, text="Phone:", font=("Montserrat semi-bold", 12), bg="white")
        Phone_label.grid(row=3, column=2, padx=10, pady=10)
        # Phone Entry
        Phone_entry = ttk.Entry(User_info_frame, width=20, font=("Montserrat semi-bold", 12))
        Phone_entry.grid(row=3, column=3, padx=10, pady=10)

        # Radio Buttons For Photo
        Photo_label = Label(User_info_frame, text="Photo:", font=("Montserrat semi-bold", 12), bg="white")
        Photo_label.grid(row=4, column=0, padx=10, pady=10)
        RB1 = ttk.Radiobutton(User_info_frame, text="Photo", value="Yes")
        RB1.grid(row=4, column=1, padx=20, pady=0)
        RB2 = ttk.Radiobutton(User_info_frame, text="No Photo", value="No")
        RB2.grid(row=4, column=2, padx=20, pady=20)

        # Frame Containing Buttons
        Buttons_frame = Frame(User_info_frame, bg="white")
        Buttons_frame.place(x=5, y=250, width=535, height=125)
        # Reset Buttons
        Reset_btn = ttk.Button(Buttons_frame, text="Reset", width=15)
        Reset_btn.grid(row=0, column=1, padx=15, pady=20)
        # Update Buttons
        Update_btn = ttk.Button(Buttons_frame, text="Update", width=15)
        Update_btn.grid(row=0, column=2, padx=15, pady=20)
        # Delete Buttons
        Delete_btn = ttk.Button(Buttons_frame, text="Delete", width=15, )
        Delete_btn.grid(row=0, column=3, padx=15, pady=20)
        # Save Buttons
        Save_btn = ttk.Button(Buttons_frame, text="Save", width=15)
        Save_btn.grid(row=0, column=4, padx=15, pady=20)
        # Take Photo Buttons
        Take_photo_btn = ttk.Button(Buttons_frame, text="Take Photo", width=15)
        Take_photo_btn.grid(row=1, column=2, padx=15, pady=20)
        # Update Photo Buttons
        Update_photo_btn = ttk.Button(Buttons_frame, text="Update Photo", width=15)
        Update_photo_btn.grid(row=1, column=3, padx=15, pady=20)

        # User_Details Frame
        Right_frame = LabelFrame(main_frame, bd=2, text="User Details", font=("Print Bold", 18), labelanchor="n",
                                 bg="white")
        Right_frame.place(x=590, y=20, width=560, height=540)

        # Search System
        User_Details_frame = Frame(Right_frame, bg="white")
        User_Details_frame.place(x=5, y=10, width=545, height=50)

        # Details Label
        Details_label = Label(User_Details_frame, text="Details by:", font=("Montserrat semi-bold", 12), bg="white")
        Details_label.grid(row=0, column=0, padx=10, pady=10)
        # Details Combo
        Details_combo = ttk.Combobox(User_Details_frame, font=("Montserrat medium", 10), width=10, state="readonly")
        Details_combo["values"] = ("Select", "Roll No", "ID")
        Details_combo.current(0)
        Details_combo.grid(row=0, column=1, padx=10, pady=10)

        # Details by input Entry
        Details_entry = ttk.Entry(User_Details_frame, width=10, font=("Montserrat semi-bold", 12))
        Details_entry.grid(row=0, column=2, padx=10, pady=10)

        # Details by input button
        Search_btn = ttk.Button(User_Details_frame, text="Search", width=10)
        Search_btn.grid(row=0, column=3, padx=10, pady=10)

        # Table Frame
        Table_Details_frame = Frame(Right_frame, bg="white")
        Table_Details_frame.place(x=5, y=80, width=545, height=425)

        scroll_x = ttk.Scrollbar(Table_Details_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(Table_Details_frame, orient=VERTICAL)

        self.student_table = ttk.Treeview(Table_Details_frame, columns=(
            "userid", "username", "roll", "year", "sem", "course", "faculty", "email", "Gender", "dob", "phone",
            "photo"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        # Desplay Text From Dommi Name
        self.student_table.heading("faculty", text="Faculty")
        self.student_table.heading("year", text="Year")
        self.student_table.heading("sem", text="Semester")
        self.student_table.heading("course", text="Course")
        self.student_table.heading("userid", text="User ID")
        self.student_table.heading("username", text="User Name")
        self.student_table.heading("roll", text="Roll No")
        self.student_table.heading("email", text="Email")
        self.student_table.heading("Gender", text="Gender")
        self.student_table.heading("dob", text="Birth Date")
        self.student_table.heading("phone", text="Phone Number")
        self.student_table.heading("photo", text="Photo Sample")
        self.student_table["show"] = "headings"

        self.student_table.column("faculty", width=75)
        self.student_table.column("year", width=75)
        self.student_table.column("sem", width=75)
        self.student_table.column("course", width=75)
        self.student_table.column("userid", width=75)
        self.student_table.column("username", width=100)
        self.student_table.column("roll", width=50)
        self.student_table.column("email", width=120)
        self.student_table.column("Gender", width=50)
        self.student_table.column("dob", width=100)
        self.student_table.column("phone", width=100)
        self.student_table.column("photo", width=100)

        self.student_table.pack(fill=BOTH, expand=1)


if __name__ == "__main__":
    screen = Tk()
    obj = User_Details(screen)
    screen.mainloop()
