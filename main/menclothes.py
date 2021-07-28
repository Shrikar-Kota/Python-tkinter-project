from tkinter import *
import tkinter.messagebox
cart10=[]
def menclothes():
    menclothes=Toplevel()
    menclothes.title('Men Clothes')
    menclothes['bg']='White'
    price=[1999,1699,1699,1599]
    def AllenSolly():
        cart10.append(price[0])
        tkinter.messagebox.showinfo("Alert Box","Added To CART! Continue Shopping")
    def Parx():
        cart10.append(price[1])
        tkinter.messagebox.showinfo("Alert Box","Added To CART! Continue Shopping")
    def PepeJeans():
        cart10.append(price[2])
        tkinter.messagebox.showinfo("Alert Box","Added To CART! Continue Shopping")
    def USPolo():
        cart10.append(price[3])
        tkinter.messagebox.showinfo("Alert Box","Added To CART! Continue Shopping")
    mi1=PhotoImage(file='ms1.png')
    mi2=PhotoImage(file='ms2.png')
    mi3=PhotoImage(file='mp1.png')
    mi4=PhotoImage(file='mp2.png')
    l1=Label(menclothes, image=mi1).grid(row=0,column=0)
    l2=Label(menclothes, image=mi2).grid(row=2,column=0)
    l3=Label(menclothes, image=mi3).grid(row=0,column=2)
    l4=Label(menclothes, image=mi4).grid(row=2,column=2)
    b1=Button(menclothes, text='Allen Solly\nColour: Blue\nPrice: Rs.1999\n____________________\nAdd to Cart',command=AllenSolly,font='20').grid(row=0,column=1)
    b2=Button(menclothes, text='Parx\nColour: White\nPrice: Rs.1699\n____________________\nAdd to Cart',command=Parx,font='20').grid(row=2,column=1)
    b3=Button(menclothes, text='Pepe Jeans\nColour: Cream\nPrice: Rs.1699\n____________________\nAdd to Cart',command=PepeJeans,font='20').grid(row=0,column=3)
    b4=Button(menclothes, text='US Polo Assn.\nColour: Black\nPrice: Rs.1599\n____________________\nAdd to Cart',command=USPolo,font='20').grid(row=2,column=3)
    def Back():
        menclothes.destroy()
    label=Label(menclothes,text='Go Back to Clothing Category',font=('Calibri',16),bg='White').grid(row=4,column=0)
    button=Button(menclothes,text='Go Back',bg='Blue',fg='White',font=('Calibri',16),command=Back).grid(row=4,column=2)
    menclothes.attributes('-fullscreen',True)
    menclothes.mainloop()



    
    
