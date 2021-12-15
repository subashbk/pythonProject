from tkinter import *
from tkinter import messagebox
import string
class Window():
    def __init__(self):
        self.master=Tk()
        self.master.geometry('550x550+45+45')
        self.master.resizable(False, False)
        self.master.title("Registration Form")
        photo = PhotoImage(file="Registation.png")
        w=Label(self.master, image=photo)
        w.pack()
        ent= Entry(self.master)
        ent.pack()
        ent.focus()
        label0 = Label(self.master,text="Registration Form",width=20, font="Aerial,20")
        label0.place(x=120, y=0)

        label1 = Label(self.master, text="First name ", font=0.10)
        label1.place(relx=0.10, rely=0.08)

        self.efirstname =Entry(self.master)
        self.efirstname.place(relx=0.42, rely=0.09)



        label2 = Label(text="Last name", font=0.10)
        label2.place(relx=0.10, rely=0.15)

        self.elastname = Entry(self.master)
        self.elastname.place(relx=0.42, rely=0.16)

        label3 = Label(self.master, text=" Username ", font=0.10)
        label3.place(relx=0.10, rely=0.22)

        self.eusername = Entry(self.master)
        self.eusername.place(relx=0.42, rely=0.23)


        label4 = Label(self.master, text="E-mail ", font=0.10)
        label4.place(relx=0.10, rely=0.30)
        self.eemail= Entry(self.master)
        self.eemail.place(relx=0.42, rely=0.31)
        label5 = Label(self.master, text="Address", font=0.10)
        label5.place(relx=0.10, rely=0.38)
        self.eaddress= Entry(self.master)
        self.eaddress.place(relx=0.42, rely=0.39)



        label5 = Label(self.master, text="Phone Number", font=0.10)
        label5.place(relx=0.10, rely=0.45)

        self.emobilenum = Entry(self.master)
        self.emobilenum.place(relx=0.42, rely=0.46)

        label8 = Label(self.master, text="Password", font=0.10)
        label8.place(relx=0.10, rely=0.52)
        self.epassword= Entry(self.master,  show='*')
        self.epassword.place(relx=0.42, rely=0.53)

        label9 = Label(self.master, text="Confirm Password", font=0.10)
        label9.place(relx=0.10, rely=0.59)
        self.erepassword = Entry(self.master, show='*')
        self.erepassword.place(relx=0.42, rely=0.60)

        Button(self.master, text="Submit", width=20, command=self.register, bg='red', fg='white').place(relx=0.38, rely=0.85)
        self.master.mainloop()
    def register(self):
        if self.eusername.get() != '' and self.efirstname.get() != '' and self.elastname.get() != '' and self.eaddress.get() != '' and self.eemail.get() != '' and self.emobilenum.get() != '' and self.epassword.get() != '':
            self.username = []

            with open('users.txt', 'r') as fh:
                for line in fh:
                    key, value = list(line.split(':'))
                    self.username.append(key)
                if str(self.efirstname.get()).isalpha() and str(self.elastname.get()).isalpha():

                    if self.eusername.get() in self.username:
                            messagebox.showerror("Error", "this user already exist")

                    else:
                        if str(self.emobilenum.get()).isnumeric():
                            if len( self.epassword.get()) >= 8:
                                if self.epassword.get() != self.erepassword.get():
                                        messagebox.showerror("Error", "Sorry! Your password didn't match")
                                else:
                                        messagebox.showinfo("Update", "Registration Successful")
                                        line = self.eusername.get() + ':' + self.efirstname.get() + ',' + self.elastname.get() + ',' + self.eaddress.get() + ',' + self.eemail.get() + ',' + self.emobilenum.get() + ',' + self.epassword.get() + ',' + '\n'
                                with open('users.txt', 'a') as userfile:
                                     userfile.write(line)
                            else:
                                messagebox.showerror("Error","your password should contains 8 character")
                        else:
                            messagebox.showerror("Error"," Your contact number should be number")
                else:
                    messagebox.showerror("Error", " your first and last name should not contain numbers")
        else:
            messagebox.showerror("Error", "All Fields are mandatory")




























Window()

