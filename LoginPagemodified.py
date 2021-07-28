from tkinter import *
import tkinter.messagebox
from sidmodified import *
def login():
    global password
    global username
    user=username.get()
    data=password.get()
    try:
        f=open(user,"r")
        l=f.read()
        if l!=data:
            tkinter.messagebox.showwarning("Alert Box",'Please Enter a Valid Password!')
        else:
            class minimize:
                def __init__(self):
                    pass
                def hide(self):
                    root.withdraw()                
            minimize.hide(root)
            fun()
            root1.geometry('500x500')
            root1.mainloop()
    except FileNotFoundError:
        tkinter.messagebox.showwarning("Username Not Found",'Please Enter a Valid Username!')
    
def register():
    root2=Tk()
    labell0=Label(root2,text='Registration of New User').grid(row=0,column=0)
    labell2=Label(root2,text='New Username* :').grid(row=1,column=0,sticky='E')
    entry1=Entry(root2)
    entry1.grid(row=1,column=1)
    labell3=Label(root2,text='New Password* :').grid(row=2,column=0,sticky='E')
    entry2=Entry(root2)
    entry2.grid(row=2,column=1)
    labell4=Label(root2,text='Confirm Password :').grid(row=3,column=0,sticky='E')
    entry3=Entry(root2,show='*')
    entry3.grid(row=3,column=1)
    root2.geometry('500x500')
    def rc():
        if entry2.get()!=entry3.get() or len(entry2.get())==0 or len(entry3.get())==0:
            tkinter.messagebox.showwarning("Alert Box","Registration Failed! Password Mismatched, Register Again ! ")
        else:
            tkinter.messagebox.showinfo("Alert Box","Registration Successful ! Thank You ")
            user=entry1.get()
            data=entry2.get()
            f1=open(user,"w")
            f1.write(data)
            root2.destroy()
    buttonn0=Button(root2,text='Register Now',fg='White',bg='Blue',command=rc) .grid(row=4,column=1)
    root2.mainloop()

root=Tk()
label1=Label(root,text="Username: ")
label1.grid(row=0,column=0,sticky="E")
username=StringVar()
password=StringVar()
label2=Entry(root,textvariable=username)
label2.grid(row=0,column=1)
label3=Label(root,text="Password: ")
label3.grid(row=1,column=0,sticky="E")
label4=Entry(root,show="*",textvariable=password)
label4.grid(row=1,column=1)
label5=Checkbutton(root,text="Remember passcode?")
label5.grid(columnspan=2)
label6=Button(root,text="Log in",command=login)
label6.grid(row=6,column=1)
balwl8=Label(root,text='If you are a New User, Please Register First!').grid(row=5,column=1)
label7=Button(root,text='Register',command=register).grid(row=6,column=0)
root.geometry('500x500')
root.title("E-Shopping Mall")
root.iconbitmap(r'C:/Users/shash/Downloads/iphone.ico')
#total=cart_total1+cart_total2+cart_total3+cart_total4

root.mainloop()
