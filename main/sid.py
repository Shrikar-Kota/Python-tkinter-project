from tkinter import *
from electronics_subcategories import *
def fun():
    root10=Toplevel()
    root10.title('E-Shopping Mall')
    root10.geometry('600x300')
    electronics=PhotoImage(file='002-computer.png')
    def elec():
        print('Electronics')
    belectronics=Button(root10,image=electronics, command=electronics1)
    belectronics.grid(row=2,column=2)
    clothes=PhotoImage(file='001-tshirt.png')
    def cloth():
        print('CLOTHES')
    bclothes=Button(root10,image=clothes, command=cloth)
    bclothes.grid(row=2,column=4)
    appliances=PhotoImage(file='004-appliances.png')
    def appli():
        print('Appliances')
    bappliances=Button(root10,image=appliances, command=appli)
    bappliances.grid(row=2,column=6)
    grocery=PhotoImage(file='003-basket.png')
    def groce():
        print('Grocery')
    bgrocery=Button(root10,image=grocery, command=groce)
    bgrocery.grid(row=2,column=8)
    telectronics=Label(root10,text='Electronics')
    telectronics.grid(row=3,column=2)
    tclothes=Label(root10,text='Clothes')
    tclothes.grid(row=3,column=4)
    tappliances=Label(root10,text='Appliances')
    tappliances.grid(row=3,column=6)
    tgrocery=Label(root10,text='Grocery')
    tgrocery.grid(row=3,column=8)
    root10.mainloop()
    
