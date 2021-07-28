from tkinter import *
from electronics_subcategoriesmodified import *
from appliances_subcategories import *
from books_subcategories  import *
from fashion_subcategories import *
from Billing_of_mall import *
#from sidmodified import *
def billing():
    class bill:
        total=cart_total1+cart_total2+cart_total3+cart_total4
        def __init__(self):
            pass
        def display(self):
            print('________________________BILL_________________________ ')
            print('Total Bill Amount : ',bill.total)
    class pay_by_cash(bill):
        def __init__(self):
            print('Cash to be Paid : ',bill.total)
            cash_recieved=int(input('Enter Cash amount to be given : '))
            if cash_recieved>bill.total:
                print('Cash Returned : ',cash_recieved-bill.total)
        def display(self):
            super().display()

    class pay_by_card(bill):
        def __init__(self):
            print('Cash to be Paid : ',bill.total)
            Card_Number=int(input('Enter Debit/Credit Card Number : '))
            cvv=int(input('Enter CVV of Card : '))
        def display(self):
            super().display()

    class pay_by_cheque(bill):
        def __init__(self):
            print('Cash to be Paid : ',bill.total)
            Bank=input('Choose Your Bank : ')
            account_no=int(input('Enter Bank Account No.'))
            authentication=input("Enter Authorised person's name : ")

    b=bill()
    print('Total Bill Amount : ',bill.total)
    print('1. Pay By Cash')
    print('2. Pay By Credit/Debit Card')
    print('3. Pay By Cheque')
    op=int(input('Enter an option to Pay : '))
    if op==1:
        c=pay_by_cash()
        c.display()
    elif op==2:
        s=pay_by_card()
        s.display()
    elif op==3:
        p=pay_by_cheque()
        p.display()
    print('Thank You For Shopping With Us ! Please Visit again ! ')

def fun():
    root10=Toplevel()
    root10.title('E-Shopping Mall')
    root10.geometry('600x300')
    electronics=PhotoImage(file='001-pc.png')
    belectronics=Button(root10,image=electronics, command=electronics1)
    belectronics.grid(row=0,column=0)
    clothes=PhotoImage(file='003-product.png')
    bclothes=Button(root10,image=clothes, command=fashion1)
    bclothes.grid(row=0,column=1)
    appliances=PhotoImage(file='002-appliances.png')
    bappliances=Button(root10,image=appliances, command=appliances1)
    bappliances.grid(row=0,column=2)
    books=PhotoImage(file='004-books.png')
    bbooks=Button(root10,image=books, command=Books1)
    bbooks.grid(row=0,column=3)
    telectronics=Label(root10,text='Electronics',font=('Calibri',16))
    telectronics.grid(row=1,column=0)
    tclothes=Label(root10,text='Clothes',font=('Calibri',16))
    tclothes.grid(row=1,column=1)
    tappliances=Label(root10,text='Appliances',font=('Calibri',16))
    tappliances.grid(row=1,column=2)
    tbooks=Label(root10,text='Books',font=('Calibri',16))
    tbooks.grid(row=1,column=3)
    total=cart_total1+cart_total2+cart_total3+cart_total4
    def exit5():
        root10.withdraw()
        billing()
    l=Label(root10,text='Tap to Exit Mall & View Your Cart',font='16').grid(row=2,columnspan=2)
    b=Button(root10,text='CART',bg='Blue',font='20',command=exit5).grid(row=2,column=2)
    root10.attributes('-fullscreen',True)
    root10.mainloop()
fun()

