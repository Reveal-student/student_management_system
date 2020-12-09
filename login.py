from tkinter import *
import pymysql
from tkinter import messagebox
import sms


class loginpage():
    def __init__(self, root):
        self.root = root
        self.root.geometry("1370x700")
        self.root.title("Admin LOGIN")
        Frame_bg = Frame(self.root, bg="yellow")
        Frame_bg.place(width=2000, height=1050)
        heading = Label(text="Welcome To Student Management System", bg="yellow", font="timesnewroman 15 bold")
        heading.pack(side="top", fill=X)

        # Frame for log in
        Frame_login = Frame(self.root, bg="white")
        Frame_login.place(x=450, y=100, width=450, height=400)

        # username and password variables for backend
        self.username_var = StringVar()
        self.password_var = StringVar()

        # Log In here TEXT
        title = Label(Frame_login, text="Login Here", font="Impact 35 bold", fg="#d77337", bg="white").place(x=120,
                                                                                                             y=20)

        # Admin Login
        Admin_login = Label(Frame_login, text="Admin Login", font="Goudyoldstyle 15 bold", fg="#d77337",
                            bg="white").place(x=170, y=100)

        # user name as text
        user = Label(Frame_login, text="Username", font="Goudyoldstyle 15 bold", fg="Gray", bg="white").place(x=120,
                                                                                                              y=130)

        # user name Entry
        user_entry = Entry(Frame_login, textvariable=self.username_var, font="timesnewroman 15", bg="lightgray").place(
            x=125, y=160)

        # password as text
        user_password = Label(Frame_login, text="Password", font="Goudyoldstyle 15 bold", fg="Gray", bg="white").place(
            x=120, y=190)

        # password Entry
        user_password = Entry(Frame_login, textvariable=self.password_var, font="timesnewroman 15",
                              bg="lightgray", show="*").place(x=125, y=220)

        # Button Login
        log_button = Button(Frame_login, text="LOGIN", width=15, height=2, command=self.success_data).place(x=170,
                                                                                                            y=270)

    # database of admin
    def success_data(self):
        con = pymysql.connect(host='localhost', db='sms2', user='root', passwd='')
        cur = con.cursor()
        cur.execute("select username,password from admin")
        for (user, pas) in cur:
            if self.username_var.get() == user and self.password_var.get() == pas:
                messagebox.showinfo("Success", "Logged in Successfully")
                sms.run()
            else:
                messagebox.showerror("Error", "Check Username And Password")
        con.commit()
        con.close()


root = Tk()
obj = loginpage(root)
root.mainloop()
