from tkinter import *


class Dashboard_Admin:
    def __init__(self,screen):
        self.screen = screen
        self.screen.geometry("1280x720+150+75")
        self.screen.title("Attendance System")
        self.screen.resizable(False, False)

        Label(text="Welcome to Dashboard", font=("Print Bold", 24)).pack()

        Button(text="User Details",
               bg="blue", fg="White",
               font=("Montserrat bold", 10)
               ).place(relx=0.2, rely=0.3, height=40, width=120)

        Button(text="Attendance",
               bg="black", fg="White",
               font=("Montserrat bold", 10)
               ).place(relx=0.35, rely=0.3, height=40, width=120)

        Button(text="Train Data",
               bg="black", fg="White",
               font=("Montserrat bold", 10)
               ).place(relx=0.2, rely=0.4, height=40, width=120)


if __name__ == "__main__":
    screen = Tk()
    obj = Dashboard_Admin(screen)
    screen.mainloop()
