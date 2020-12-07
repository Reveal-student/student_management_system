# yaha par ham tkinter python ka module use kar rahe hai gui banane ke liye
from tkinter import *
from tkinter import ttk, messagebox
# yaha par database ke liye pymysql import kar rahe hai
import pymysql


# yaha par student class banayi he puri desktop frame ko represent karne ke liye
class Student():
    def __init__(self, root):
        self.root = root
        self.root.title("Student Management System")
        # ye desktop screen ka size he(widthxlength+position+position)
        self.root.geometry("1370x700+0+0")
        # ye screen ki labelling ,uska color,uska font ye sab chize bata rahi hai
        title = Label(self.root, text="Student Management System", bd=9, relief=GROOVE,
                      font=("times new roman", 50, "bold"), bg="blue", fg="black")
        title.pack(side=TOP, fill=X)

        # All Variables for backend purpose
        self.Roll_No_Var = StringVar()
        self.name_Var = StringVar()
        self.email_Var = StringVar()
        self.gender_Var = StringVar()
        self.contact_Var = StringVar()
        self.dob_Var = StringVar()
        self.search_by = StringVar()
        self.search_txt = StringVar()

        # ye left side me jo student data milne vali frame bata rahi hai,manage student namaki frame left side wali
        Manage_Frame = Frame(self.root, bd=4, relief=RIDGE, bg="yellow")
        Manage_Frame.place(x=20, y=100, width=450, height=585)
        # jo "manage student" jo label hai,uski characteristic and position bata rahi hai
        m_title = Label(Manage_Frame, text="Manage Student", bg="yellow", fg="black",
                        font=("times new roman", 40, "bold"))
        m_title.grid(row=0, columnspan=2, pady=20)
        # manage student frame wali jo input filed "Roll No" hai uske bare mai hai,uska sabkuch
        lbl_roll = Label(Manage_Frame, text="Roll No", bg="blue", fg="white", font=("times new roman", 20, "bold"))
        lbl_roll.grid(row=1, column=0, pady=10, padx=20, sticky="w")
        txt_Roll = Entry(Manage_Frame, textvariable=self.Roll_No_Var, font=("times new roman", 15, "bold"), bd=5,
                         relief=GROOVE)
        txt_Roll.grid(row=1, column=1, pady=10, padx=20, sticky="w")
        # manage student frame wali jo input filed "Name:" hai uske bare mai hai,uska sabkuch
        lbl_name = Label(Manage_Frame, text="Name:", bg="blue", fg="white", font=("times new roman", 20, "bold"))
        lbl_name.grid(row=2, column=0, pady=10, padx=20, sticky="w")
        txt_name = Entry(Manage_Frame, textvariable=self.name_Var, font=("times new roman", 15, "bold"), bd=5,
                         relief=GROOVE)
        txt_name.grid(row=2, column=1, pady=10, padx=20, sticky="w")
        # manage student frame wali jo input filed "Email:" hai uske bare mai hai,uska sabkuch
        lbl_Email = Label(Manage_Frame, text="Email:", bg="blue", fg="white", font=("times new roman", 20, "bold"))
        lbl_Email.grid(row=3, column=0, pady=10, padx=20, sticky="w")
        txt_Email = Entry(Manage_Frame, textvariable=self.email_Var, font=("times new roman", 15, "bold"), bd=5,
                          relief=GROOVE)
        txt_Email.grid(row=3, column=1, pady=10, padx=20, sticky="w")
        # manage student frame wali jo input filed "Gender" hai uske bare mai hai,uska sabkuch
        lbl_gender = Label(Manage_Frame, text="Gender:", bg="blue", fg="white", font=("times new roman", 20, "bold"))
        lbl_gender.grid(row=4, column=0, pady=10, padx=20, sticky="w")
        # yaha pe hum combobox use kar rahe hai drop down list ke liye "Gender" Category
        combo_gender = ttk.Combobox(Manage_Frame, textvariable=self.gender_Var, font=("times new roman", 13, "bold"),
                                    state="readonly")
        combo_gender['values'] = ("male", "female", "other")
        combo_gender.grid(row=4, column=1, padx=20, pady=10)
        # manage student frame wali jo input filed "Contact" hai uske bare mai hai,uska sabkuch
        lbl_Contact = Label(Manage_Frame, text="Contact:", bg="blue", fg="white", font=("times new roman", 20, "bold"))
        lbl_Contact.grid(row=5, column=0, pady=10, padx=20, sticky="w")
        txt_Contact = Entry(Manage_Frame, textvariable=self.contact_Var, font=("times new roman", 15, "bold"), bd=5,
                            relief=GROOVE)
        txt_Contact.grid(row=5, column=1, pady=10, padx=20, sticky="w")
        # manage student frame wali jo input filed "Date of birth" hai uske bare mai hai,uska sabkuch
        lbl_Dob = Label(Manage_Frame, text="D.O.B:", bg="blue", fg="white", font=("times new roman", 20, "bold"))
        lbl_Dob.grid(row=6, column=0, pady=10, padx=20, sticky="w")
        txt_Dob = Entry(Manage_Frame, textvariable=self.dob_Var, font=("times new roman", 15, "bold"), bd=5,
                        relief=GROOVE)
        txt_Dob.grid(row=6, column=1, pady=10, padx=20, sticky="w")
        # manage student frame wali jo input filed "Address" hai uske bare mai hai,uska sabkuch
        lbl_Address = Label(Manage_Frame, text="Address:", bg="blue", fg="white", font=("times new roman", 20, "bold"))
        lbl_Address.grid(row=7, column=0, pady=10, padx=20, sticky="w")
        self.txt_Address = Text(Manage_Frame, width=30, height=3, font=("times new roman", 10, "bold"))
        self.txt_Address.grid(row=7, column=1, pady=10, padx=20, sticky="w")

        # button frame left side me jo student ka data(manage student) jo lene wale hai usme se jo button hai add,
        # delete,update,clear uska frame hai
        btn_frame = Frame(Manage_Frame, bd=3, relief=RIDGE, bg="black")
        btn_frame.place(x=15, y=525, width=420)
        # har ek button ka position,uska naam ,uske baare me
        Addbtn = Button(btn_frame, text="Add", width=10, command=self.add_students).grid(row=0, column=0, padx=10,
                                                                                         pady=10)
        updatebtn = Button(btn_frame, text="update", width=10, command=self.update_data).grid(row=0, column=1, padx=10,
                                                                                              pady=10)
        deletebtn = Button(btn_frame, text="Delete", width=10, command=self.delete_data).grid(row=0, column=2, padx=10,
                                                                                              pady=10)
        clearbtn = Button(btn_frame, text="Clear", width=10, command=self.clear).grid(row=0, column=3, padx=10, pady=10)

        # Details Frame right side wali jo frame hai jisme student ka data show hone wala hai uska position,
        # background color bata raha hai
        Details_Frame = Frame(self.root, bd=4, relief=RIDGE, bg="yellow")
        Details_Frame.place(x=500, y=100, width=1200, height=585)
        # yaha par search kis hisab se karna hai matlab name,roll no,contact se search karna hai ye bata raha hai
        lbl_search = Label(Details_Frame, text="Search By", bg="blue", fg="white",
                           font=("times new roman", 20, "bold"))
        lbl_search.grid(row=0, column=0, pady=10, padx=20, sticky="w")
        # yaha par hamne combobox ka use dropdown list ke liye kiya hai search by name,roll no,contact
        combo_search = ttk.Combobox(Details_Frame, textvariable=self.search_by, font=("times new roman", 13, "bold"),
                                    width=10, state="readonly")
        combo_search['values'] = ("Roll_no", "Name", "Contact")
        combo_search.grid(row=0, column=1, padx=20, pady=10)
        txt_search = Entry(Details_Frame, textvariable=self.search_txt, font=("times new roman", 10, "bold"), width=20,
                           bd=5, relief=GROOVE)
        txt_search.grid(row=0, column=2, pady=10, padx=20, sticky="w")
        # ye search aur show all button ke baare mei bata raha hai...
        searchbtn = Button(Details_Frame, text="Search", width=10, pady=5, command=self.search_data).grid(row=0,
                                                                                                          column=3,
                                                                                                          padx=10,
                                                                                                          pady=10)
        searchbtn = Button(Details_Frame, text="Show All", width=10, pady=5, command=self.fetch_data).grid(row=0, column=4, padx=10, pady=10)

        # Table Frame
        # ye table frame ko bata raha hai jisme student ka pura data show ho raha hai
        Table_Frame = Frame(Details_Frame, bd=4, relief=RIDGE, bg="crimson")
        Table_Frame.place(x=10, y=70, width=830, height=500)
        # yaha par hamne scroll bar banaye hai
        scroll_x = Scrollbar(Table_Frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(Table_Frame, orient=VERTICAL)

        self.Student_table = ttk.Treeview(Table_Frame,
                                          column=("roll", "name", "email", "gender", "contact", "dob", "Address"),
                                          xscrollcommand=scroll_y, yscrollcommand=scroll_x)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config()
        scroll_y.config()
        # yaha par jo student ka data show hone wala hai uska heading aur uska column width bataya hai
        self.Student_table.heading("roll", text="Roll No.")
        self.Student_table.heading("name", text="Name")
        self.Student_table.heading("email", text="Email")
        self.Student_table.heading("gender", text="Gender")
        self.Student_table.heading("contact", text="Contact")
        self.Student_table.heading("dob", text="D.O.B")
        self.Student_table.heading("Address", text="Address")

        self.Student_table['show'] = 'headings'
        self.Student_table.column("roll", width=100)
        self.Student_table.column("name", width=100)
        self.Student_table.column("email", width=100)
        self.Student_table.column("gender", width=100)
        self.Student_table.column("contact", width=100)
        self.Student_table.column("dob", width=100)
        self.Student_table.column("Address", width=150)

        self.Student_table.pack(fill=BOTH, expand=1)
        self.Student_table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()

        # add button ka function add_students database ke liye

    def add_students(self):
        # yaha par hum jb user rollno aur name enter nahi karega to usko message de rahe hai,uske alava hum message box
        # notification dene ke liye use kar rahe hai
        if self.Roll_No_Var.get() == "" or self.name_Var.get() == "":
            messagebox.showerror("Error", "All fields are required to fill")
        else:
            con = pymysql.connect(host='localhost', db='sms2', user='root', passwd='')
            cur = con.cursor()
            cur.execute("insert into students values (%s, %s, %s, %s, %s, %s, %s)", (self.Roll_No_Var.get(),
                                                                                     self.name_Var.get(),
                                                                                     self.email_Var.get(),
                                                                                     self.gender_Var.get(),
                                                                                     self.contact_Var.get(),
                                                                                     self.dob_Var.get(),
                                                                                     self.txt_Address.get('1.0', END)))
            con.commit()
            self.fetch_data()
            self.clear()
            con.close()
            messagebox.showinfo("Success", "Record has been inserted")

    # ye function hum database se data fetch karke table me display karenge
    def fetch_data(self):
        con = pymysql.connect(host='localhost', db='sms2', user='root', passwd='')
        cur = con.cursor()
        cur.execute("select * from students")
        rows = cur.fetchall()
        if len(rows) != 0:
            self.Student_table.delete(*self.Student_table.get_children())
            for row in rows:
                self.Student_table.insert('', END, values=row)
            con.commit()
        con.close()

    def get_cursor(self, ev):
        cursor_row = self.Student_table.focus()
        contents = self.Student_table.item(cursor_row)
        row = contents['values']
        self.Roll_No_Var.set(row[0])
        self.name_Var.set(row[1])
        self.email_Var.set(row[2])
        self.gender_Var.set(row[3])
        self.contact_Var.set(row[4])
        self.dob_Var.set(row[5])
        self.txt_Address.delete("1.0", END)
        self.txt_Address.insert(END, row[6])

    # hum yaha par clear button ke liye function bana rahe hai...
    def clear(self):
        self.Roll_No_Var.set("")
        self.name_Var.set("")
        self.email_Var.set("")
        self.gender_Var.set("")
        self.contact_Var.set("")
        self.dob_Var.set("")
        self.txt_Address.delete("1.0", END)

    def update_data(self):
        con = pymysql.connect(host='localhost', db='sms2', user='root', passwd='')
        cur = con.cursor()
        cur.execute("update students set name=%s,email=%s,gender=%s,contact=%s,dob=%s,address=%s where roll_no=%s", (

            self.name_Var.get(),
            self.email_Var.get(),
            self.gender_Var.get(),
            self.contact_Var.get(),
            self.dob_Var.get(),
            self.txt_Address.get('1.0', END),
            self.Roll_No_Var.get()
        ))
        con.commit()
        self.fetch_data()
        self.clear()
        con.close()
        messagebox.showinfo("Success", "Record has been inserted")

    def delete_data(self):
        con = pymysql.connect(host='localhost', db='sms2', user='root', passwd='')
        cur = con.cursor()
        cur.execute("delete from students where roll_no=%s", self.Roll_No_Var.get())
        con.commit()
        con.close()
        self.fetch_data()
        self.clear()

    def search_data(self):
        con = pymysql.connect(host='localhost', db='sms2', user='root', passwd='')
        cur = con.cursor()
        cur.execute("select * from students where " + str(self.search_by.get()) + " Like '%"+str(
            self.search_txt.get())+ "%'")
        rows = cur.fetchall()
        if len(rows) != 0:
            self.Student_table.delete(*self.Student_table.get_children())
            for row in rows:
                self.Student_table.insert('', END, values=row)
            con.commit()
        con.close()


class Student():
    pass
    root = Tk()
    obj = Student(root)
    root.mainloop()
