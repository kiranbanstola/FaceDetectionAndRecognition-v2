from tkinter import *
from tkinter import ttk, filedialog
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv

# Global variable
myData = []


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

        # Button for Back
        self.Back_icon = ImageTk.PhotoImage(
            Image.open(r"D:\FaceDetectionAndRecognition-v2\icons\Back_Frame.png"))
        back_btn = ttk.Button(bg_img,
                              text="Back",
                              command=self.back_screen,
                              cursor="hand2",
                              image=self.Back_icon,
                              compound=LEFT)
        back_btn.place(x=50, y=30, width=100, height=35)

        # Variables Define
        self.var_attenid = StringVar()
        #self.var_attenname = StringVar()
        self.var_date = StringVar()
        #self.var_time = StringVar()
        #self.var_status = StringVar()

        Label(screen, text="Attendance Details", font=("Print Bold", 36), fg="SteelBlue4").place(relx=0.35, rely=0.01)

        main_frame = Frame(self.screen, bg="white", highlightthickness=2, highlightbackground="black")
        main_frame.place(x=50, y=100, width=1180, height=580)

        # Upper Frame
        Upper_frame = LabelFrame(main_frame, bd=2, text="Search Attendance Details of User", font=("Print Bold", 18),
                                 labelanchor="n",
                                 bg="white")
        Upper_frame.place(x=20, y=20, width=1140, height=150)

        # Reset Buttons
        Import_btn = ttk.Button(Upper_frame, text="Import Data", command=self.import_csv, width=15, cursor="hand2")
        Import_btn.grid(row=0, column=1, padx=50, pady=20)

        # Search By ID
        # Attendance Label
        Attendance_id_label = Label(Upper_frame, text="User ID:", font=("Montserrat semi-bold", 12), bg="white")
        Attendance_id_label.grid(row=0, column=3, pady=10)
        # Attendance ID Entry
        Attendance_id_entry = ttk.Entry(Upper_frame, width=10,
                                        font=("Montserrat semi-bold", 12),
                                        textvariable=self.var_attenid
                                        )
        Attendance_id_entry.grid(row=0, column=4, padx=20, pady=10)

        # Search By DATE
        # Attendance Label
        Attendance_date_label = Label(Upper_frame, text="Attendance Date (dd/mm/yyy):",
                                      font=("Montserrat semi-bold", 12), bg="white")
        Attendance_date_label.grid(row=1, column=3, pady=10)
        # Attendance ID Entry
        Attendance_date_entry = ttk.Entry(Upper_frame, width=10,
                                          font=("Montserrat semi-bold", 12),
                                          textvariable=self.var_date
                                          )
        Attendance_date_entry.grid(row=1, column=4, padx=20, pady=10)

        # Search Buttons
        Search_btn = ttk.Button(Upper_frame, text="Search by ID",
                                command=self.search_databyID,
                                width=15, cursor="hand2")
        Search_btn.grid(row=0, column=5, padx=10, pady=10)

        # Search Buttons
        Search_btn = ttk.Button(Upper_frame, text="Search by Date",
                                command=self.search_databyDATE,
                                width=15, cursor="hand2")
        Search_btn.grid(row=1, column=5, padx=10, pady=10)

        # Reset Buttons
        Reset_btn = ttk.Button(Upper_frame, text="Reset Search", command=self.reset_search, width=15, cursor="hand2")
        Reset_btn.grid(row=1, column=6, padx=10, pady=10)

        # Lower Frame
        Lower_frame = LabelFrame(main_frame, bd=2, text="Attendance Details of User", font=("Print Bold", 18),
                                 labelanchor="n",
                                 bg="white")
        Lower_frame.place(x=20, y=200, width=1140, height=350)

        # Search System
        User_Details_frame = Frame(Lower_frame, bg="white")
        User_Details_frame.place(x=10, y=10, width=1120, height=310)

        # Scroll Bar
        scroll_x = ttk.Scrollbar(User_Details_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(User_Details_frame, orient=VERTICAL)

        self.Attendance_Report_tbl = ttk.Treeview(User_Details_frame, columns=(
            "userid", "username", "time", "date", "status"), xscrollcommand=scroll_x.set,
                                                  yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.Attendance_Report_tbl.xview)
        scroll_y.config(command=self.Attendance_Report_tbl.yview)

        self.Attendance_Report_tbl.heading("userid", text="User ID")
        self.Attendance_Report_tbl.heading("username", text="Attendance Name")
        self.Attendance_Report_tbl.heading("time", text="Attendance Time")
        self.Attendance_Report_tbl.heading("date", text="Attendance Date")
        self.Attendance_Report_tbl.heading("status", text="Attendance Status")

        self.Attendance_Report_tbl["show"] = "headings"
        self.Attendance_Report_tbl.column("userid", width=30)
        self.Attendance_Report_tbl.column("username", width=100)
        self.Attendance_Report_tbl.column("time", width=50)
        self.Attendance_Report_tbl.column("date", width=50)
        self.Attendance_Report_tbl.column("status", width=75)
        self.Attendance_Report_tbl.pack(fill=BOTH, expand=1)



    # To get data to the entry field
    def reset_search(self):
        global myData
        myData.clear()
        with open('attendance.csv', mode='r') as file:
            csvRead = csv.reader(file, delimiter=",")
            for i in csvRead:
                    myData.append(i)
            self.fetchData(myData)

    # Button Function
    def fetchData(self, rows):
        self.Attendance_Report_tbl.delete(*self.Attendance_Report_tbl.get_children())
        for i in rows:
            self.Attendance_Report_tbl.insert("", END, values=i)

    # To insert from csv file
    def import_csv(self):
        global myData
        myData.clear()
        file_name = filedialog.askopenfilename(initialdir=os.getcwd(), title="Open CSV",
                                               filetypes=(("CSV File", "*.csv"), ("All File", "*.*")),
                                               parent=self.screen)
        with open(file_name) as myFile:
            csvRead = csv.reader(myFile, delimiter=",")
            for i in csvRead:
                myData.append(i)
            self.fetchData(myData)

    # Search BY ID Function
    def search_databyDATE(self):
        global myData
        myData.clear()
        with open('attendance.csv', mode='r') as file:
            csvRead = csv.reader(file, delimiter=",")
            for i in csvRead:
                if i[3] == self.var_date.get():
                    myData.append(i)
            self.fetchData(myData)
            if i[3] != self.var_date.get():
                messagebox.showerror("Error", "Date Not Valid!!")

    # Search BY ID Function
    def search_databyID(self):
        global myData
        myData.clear()
        with open('attendance.csv', mode='r') as file:
            csvRead = csv.reader(file, delimiter=",")
            for i in csvRead:
                if i[0] == self.var_attenid.get():
                    myData.append(i)
            self.fetchData(myData)
            if i[0] != self.var_attenid.get():
                messagebox.showerror("Error", "User not found!!")

    def back_screen(self):
        self.screen.destroy()


if __name__ == "__main__":
    screen = Tk()
    obj = Attendance_Details(screen)
    screen.mainloop()
