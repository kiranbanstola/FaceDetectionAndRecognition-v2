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

        # Variables Define
        self.var_attenid = StringVar()
        self.var_attenname = StringVar()
        #self.var_roll = StringVar()
        #self.var_course = StringVar()
        #self.var_faculty = StringVar()
        self.var_time = StringVar()
        self.var_date = StringVar()
        self.var_status = StringVar()

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
                                          font=("Montserrat semi-bold", 12),
                                          textvariable=self.var_attenname
                                          )
        Attendance_Name_entry.grid(row=0, column=1, pady=10)

        # Attendance Label
        Attendance_id_label = Label(Upper_frame, text="Attendance ID:", font=("Montserrat semi-bold", 12), bg="white")
        Attendance_id_label.grid(row=1, column=0, padx=10, pady=10)
        # Attendance ID Entry
        Attendance_id_entry = ttk.Entry(Upper_frame, width=10,
                                        font=("Montserrat semi-bold", 12),
                                        textvariable=self.var_attenid
                                        )
        Attendance_id_entry.grid(row=1, column=1, pady=10)

        # Time Label
        Time_label = Label(Upper_frame, text="Time:", font=("Montserrat semi-bold", 12), bg="white")
        Time_label.grid(row=2, column=0, padx=10, pady=10)
        # Time Entry
        Time_entry = ttk.Entry(Upper_frame, width=10,
                               font=("Montserrat semi-bold", 12),
                               textvariable=self.var_time)
        Time_entry.grid(row=2, column=1, pady=10)

        # Date Label
        Date_label = Label(Upper_frame, text="Date:", font=("Montserrat semi-bold", 12), bg="white")
        Date_label.grid(row=2, column=2, padx=10, pady=10)
        # Date Entry
        Date_entry = ttk.Entry(Upper_frame, width=10,
                               font=("Montserrat semi-bold", 12),
                               textvariable=self.var_date)
        Date_entry.grid(row=2, column=3, pady=10)

        # Attendance Label
        Attendance_label = Label(Upper_frame, text="Attendance Status:", font=("Montserrat semi-bold", 12), bg="white")
        Attendance_label.grid(row=3, column=0, padx=10, pady=10)
        # Attendance Radio
        r1 = ttk.Radiobutton(Upper_frame, text="Present",variable=self.var_status, value="Present")
        r1.grid(row=3, column=1, padx=0, pady=0)
        r2 = ttk.Radiobutton(Upper_frame, text="Absent",variable=self.var_status, value="Absent")
        r2.grid(row=3, column=2, padx=0, pady=0)

        # Buttons Frames
        Buttons_frame = Frame(Upper_frame, bg="White")
        Buttons_frame.place(x=720, y=0, width=400, height=180)

        # Export Buttons
        Export_btn = ttk.Button(Buttons_frame, text="Export Data", command=self.export_csv, width=15, cursor="hand2")
        Export_btn.place(relx=0.2, rely=0.2)

        # Reset Buttons
        Import_btn = ttk.Button(Buttons_frame, text="Import Data", command=self.import_csv, width=15, cursor="hand2")
        Import_btn.place(relx=0.2, rely=0.6)

        # Update Buttons
        #Update_btn = ttk.Button(Buttons_frame, text="Update Data",command=self.update_data, width=15, cursor="hand2")
        #Update_btn.place(relx=0.6, rely=0.2)

        # Reset Buttons
        Reset_btn = ttk.Button(Buttons_frame, text="Reset Data",command=self.reset_data, width=15, cursor="hand2")
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
            "userid", "username",
            #"roll", "faculty",
            "time", "date", "status"), xscrollcommand=scroll_x.set,
                                                  yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.Attendance_Report_tbl.xview)
        scroll_y.config(command=self.Attendance_Report_tbl.yview)

        self.Attendance_Report_tbl.heading("userid", text="Attendance ID")
        self.Attendance_Report_tbl.heading("username", text="Attendance Name")
        #self.Attendance_Report_tbl.heading("roll", text="Attendance Roll")
        #self.Attendance_Report_tbl.heading("faculty", text="Attendance Faculty")
        self.Attendance_Report_tbl.heading("time", text="Attendance Time")
        self.Attendance_Report_tbl.heading("date", text="Attendance Date")
        self.Attendance_Report_tbl.heading("status", text="Attendance Status")

        self.Attendance_Report_tbl["show"] = "headings"
        self.Attendance_Report_tbl.column("userid", width=30)
        self.Attendance_Report_tbl.column("username", width=100)
        #self.Attendance_Report_tbl.column("roll", width=50)
        #self.Attendance_Report_tbl.column("faculty", width=75)
        self.Attendance_Report_tbl.column("time", width=50)
        self.Attendance_Report_tbl.column("date", width=50)
        self.Attendance_Report_tbl.column("status", width=75)

        self.Attendance_Report_tbl.pack(fill=BOTH, expand=1)
        self.Attendance_Report_tbl.bind("<ButtonRelease>",self.get_cursor)

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

    # To insert from csv file
    def export_csv(self):
        try:
            if len(myData) < 1:
                messagebox.showerror("Error", "No Data Found!", parent=self.screen)
                return False
            file_name = filedialog.asksaveasfilename(initialdir=os.getcwd(), title="Open CSV",
                                                     filetypes=(("CSV File", "*.csv"), ("All File", "*.*")),
                                                     parent=self.screen)
            with open(file_name, mode="w", newline="") as myFile:
                exp_write = csv.writer(myFile, delimiter=",")
                for i in myData:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export", "Data Export to '" + os.path.basename(file_name) + "' Successfully")
        except Exception as es:
            messagebox.showerror("Error", f"Due to :{str(es)}", parent=self.screen)

    # To get data to the entry field
    def get_cursor(self,event=""):
        cursor_row=self.Attendance_Report_tbl.focus()
        context=self.Attendance_Report_tbl.item(cursor_row)
        rows=context["values"]
        self.var_attenid.set(rows[0])
        self.var_attenname.set(rows[1])
        self.var_time.set(rows[2])
        self.var_date.set(rows[3])
        self.var_status.set(rows[4])

    # Update Function


    # Reset Variable
    def reset_data(self):
        self.var_attenid.set("")
        self.var_attenname.set("")
        self.var_time.set("")
        self.var_date.set("")
        self.var_status.set("")

if __name__ == "__main__":
    screen = Tk()
    obj = Attendance_Details(screen)
    screen.mainloop()
