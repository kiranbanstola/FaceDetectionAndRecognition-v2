from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Attendance_Details:
    def __init__(self, screen):
        self.screen = screen
        self.screen.geometry("1280x720+150+75")
        self.screen.title("Attendance Details")
        self.screen.resizable(False, False)

        img1 = Image.open(r"D:\FaceDetectionAndRecognition-v2\bg_gradient.jpg")
        img1 = img1.resize((1280, 720), Image.ANTIALIAS)
        self.photo_img1 = ImageTk.PhotoImage(img1)
        bg_img = Label(self.screen, image=self.photo_img1)
        bg_img.place(x=0, y=0)

        Label(screen, text="Attendance Details", font=("Print Bold", 36), fg="SteelBlue4").place(relx=0.35, rely=0.01)

        main_frame = Frame(self.screen, bg="white", highlightthickness=2, highlightbackground="black")
        main_frame.place(x=50, y=100, width=1180, height=580)

        # Upper Frame
        Upper_frame = LabelFrame(main_frame, bd=2, text="Search Attendance Details of User", font=("Print Bold", 18),
                                 labelanchor="n",
                                 bg="white")
        Upper_frame.place(x=20, y=20, width=1140, height=220)

        # Lable and Entry

        # Attendance Label
        Attendance_Name_label = Label(Upper_frame, text="Attendance Name:", font=("Montserrat semi-bold", 12),
                                      bg="white")
        Attendance_Name_label.grid(row=0, column=0, padx=10, pady=10)
        # Attendance Entry
        Attendance_Name_entry = ttk.Entry(Upper_frame, width=20,
                                          font=("Montserrat semi-bold", 12))
        Attendance_Name_entry.grid(row=0, column=1, pady=10)

        # Faculty Label
        Faculty_label = Label(Upper_frame, text="Faculty:", font=("Montserrat semi-bold", 12), bg="white")
        Faculty_label.grid(row=0, column=2, padx=10, pady=10)
        # Faculty Entry
        Faculty_entry = ttk.Entry(Upper_frame, width=20,
                                  font=("Montserrat semi-bold", 12))
        Faculty_entry.grid(row=0, column=3, pady=10)

        # Attendance Label
        Attendance_id_label = Label(Upper_frame, text="Attendance ID:", font=("Montserrat semi-bold", 12), bg="white")
        Attendance_id_label.grid(row=1, column=0, padx=10, pady=10)
        # Attendance ID Entry
        Attendance_id_entry = ttk.Entry(Upper_frame, width=10,
                                        font=("Montserrat semi-bold", 12))
        Attendance_id_entry.grid(row=1, column=1, pady=10)

        # Attendance Rollno Label
        Attendance_Roll_label = Label(Upper_frame, text="Attendance Roll:", font=("Montserrat semi-bold", 12),
                                      bg="white")
        Attendance_Roll_label.grid(row=1, column=2, padx=10, pady=10)
        # Attendance ID Entry
        Attendance_Roll_entry = ttk.Entry(Upper_frame, width=10,
                                          font=("Montserrat semi-bold", 12))
        Attendance_Roll_entry.grid(row=1, column=3, pady=10)

        # Time Label
        Time_label = Label(Upper_frame, text="Time:", font=("Montserrat semi-bold", 12), bg="white")
        Time_label.grid(row=2, column=0, padx=10, pady=10)
        # Time Entry
        Time_entry = ttk.Entry(Upper_frame, width=10,
                               font=("Montserrat semi-bold", 12))
        Time_entry.grid(row=2, column=1, pady=10)

        # Date Label
        Date_label = Label(Upper_frame, text="Date:", font=("Montserrat semi-bold", 12), bg="white")
        Date_label.grid(row=2, column=2, padx=10, pady=10)
        # Date Entry
        Date_entry = ttk.Entry(Upper_frame, width=10,
                               font=("Montserrat semi-bold", 12))
        Date_entry.grid(row=2, column=3, pady=10)

        # Attendance Label
        Attendance_label = Label(Upper_frame, text="Attendance Status:", font=("Montserrat semi-bold", 12), bg="white")
        Attendance_label.grid(row=3, column=0, padx=10, pady=10)
        # Attendance Radio
        r1 = ttk.Radiobutton(Upper_frame, text="Present", value="Present")
        r1.grid(row=3, column=1, padx=0, pady=0)
        r2 = ttk.Radiobutton(Upper_frame, text="Absent", value="Absent")
        r2.grid(row=3, column=2, padx=0, pady=0)

        # Buttons Frames
        Buttons_frame = Frame(Upper_frame, bg="White")
        Buttons_frame.place(x=720, y=0, width=400, height=180)

        # Export Buttons
        Export_btn = ttk.Button(Buttons_frame, text="Export Data", width=15, cursor="hand2")
        Export_btn.place(relx=0.2, rely=0.2)

        # Reset Buttons
        Import_btn = ttk.Button(Buttons_frame, text="Import Data", width=15, cursor="hand2")
        Import_btn.place(relx=0.2, rely=0.6)

        # Update Buttons
        Update_btn = ttk.Button(Buttons_frame, text="Update Data", width=15, cursor="hand2")
        Update_btn.place(relx=0.6, rely=0.2)

        # Reset Buttons
        Reset_btn = ttk.Button(Buttons_frame, text="Reset Data", width=15, cursor="hand2")
        Reset_btn.place(relx=0.6, rely=0.6)

        # Lower Frame
        Lower_frame = LabelFrame(main_frame, bd=2, text="Attendance Details of User", font=("Print Bold", 18),
                                 labelanchor="n",
                                 bg="white")
        Lower_frame.place(x=20, y=260, width=1140, height=300)

        # Search System
        User_Details_frame = Frame(Lower_frame, bg="white")
        User_Details_frame.place(x=10, y=10, width=1120, height=250)

        # Scroll Bar
        scroll_x = ttk.Scrollbar(User_Details_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(User_Details_frame, orient=VERTICAL)

        self.Attendance_Report_tbl = ttk.Treeview(User_Details_frame, columns=(
            "userid", "username", "roll", "faculty", "time", "date", "status"), xscrollcommand=scroll_x.set,
                                                  yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.Attendance_Report_tbl.xview)
        scroll_y.config(command=self.Attendance_Report_tbl.yview)

        self.Attendance_Report_tbl.heading("userid",text="Attendance ID")
        self.Attendance_Report_tbl.heading("username",text="Attendance Name")
        self.Attendance_Report_tbl.heading("roll",text="Attendance Roll")
        self.Attendance_Report_tbl.heading("faculty",text="Attendance Faculty")
        self.Attendance_Report_tbl.heading("time",text="Attendance Time")
        self.Attendance_Report_tbl.heading("date",text="Attendance Date")
        self.Attendance_Report_tbl.heading("status",text="Attendance Status")

        self.Attendance_Report_tbl["show"]="headings"
        self.Attendance_Report_tbl.column("userid",width=50)
        self.Attendance_Report_tbl.column("username",width=150)
        self.Attendance_Report_tbl.column("roll",width=50)
        self.Attendance_Report_tbl.column("faculty",width=75)
        self.Attendance_Report_tbl.column("time",width=50)
        self.Attendance_Report_tbl.column("date",width=50)
        self.Attendance_Report_tbl.column("status",width=75)

        self.Attendance_Report_tbl.pack(fill=BOTH,expand=1)


if __name__ == "__main__":
    screen = Tk()
    obj = Attendance_Details(screen)
    screen.mainloop()
