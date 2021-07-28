from tkinter import *
import tkinter.messagebox
cart11=[]
def womenclothes():
    womenclothes=Toplevel()
    womenclothes.title('Women Clothes')
    womenclothes['bg']='White'
    price=[1250,899,1289,959]
    def Zara():
        cart11.append(price[0])
        tkinter.messagebox.showinfo("Alert Box","Added To CART! Continue Shopping")
    def FabIndia():
        cart11.append(price[1])
        tkinter.messagebox.showinfo("Alert Box","Added To CART! Continue Shopping")
    def Levis():
        cart11.append(price[2])
        tkinter.messagebox.showinfo("Alert Box","Added To CART! Continue Shopping")
    def Globus():
        cart11.append(price[3])
        tkinter.messagebox.showinfo("Alert Box","Added To CART! Continue Shopping")
    mi1=PhotoImage(file='w1.png')
    mi2=PhotoImage(file='w5.png')
    mi3=PhotoImage(file='w3.png')
    mi4=PhotoImage(file='ws.png')
    l1=Label(womenclothes, image=mi1).grid(row=0,column=0)
    l2=Label(womenclothes, image=mi2).grid(row=2,column=0)
    l3=Label(womenclothes, image=mi3).grid(row=0,column=2)
    l4=Label(womenclothes, image=mi4).grid(row=2,column=2)
    b1=Button(womenclothes, text='Zara\nColour: Red\nPrice: Rs.1250\n____________________\nAdd to Cart',command=Zara,font='20').grid(row=0,column=1)
    b2=Button(womenclothes, text='FabIndia\nColour: Black\nPrice: Rs.899\n____________________\nAdd to Cart',command=FabIndia,font='20').grid(row=2,column=1)
    b3=Button(womenclothes, text='Levis\nColour: Blue\nPrice: Rs.1289\n____________________\nAdd to Cart',command=Levis,font='20').grid(row=0,column=3)
    b4=Button(womenclothes, text='Globus\nColour: Dark Blue\nPrice: Rs.959\n____________________\nAdd to Cart',command=Globus,font='20').grid(row=2,column=3)
    def Back():
        womenclothes.destroy()
    label=Label(womenclothes,text='Go Back to Clothing Category',font=('Calibri',16),bg='White').grid(row=4,column=0)
    button=Button(womenclothes,text='Go Back',bg='Blue',fg='White',font=('Calibri',16),command=Back).grid(row=4,column=2)
    womenclothes.attributes('-fullscreen',True)
    womenclothes.mainloop()



    
    

