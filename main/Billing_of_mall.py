from sidmodified import *
def money():
    class bill:
        total=cart_total1+cart_total2+cart_total3+cart_total4
        def __init__(self):
            pass
        def display(self):
            print('________________________BILL_________________________ ')
            #for i in range(len(bill.item)):
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
