class bill:
    item=[]
    item_price=[]
    qty=[]
    Bill_Amount=[]
    def __init__(self):
        bill.item.append(input('Enter a Product : '))
        bill.item_price.append(int(input("Enter it's Price : ")))
        bill.qty.append(int(input("Enter it's Quantity : ")))
        bill.Bill_Amount.append(bill.qty[i]*bill.item_price[i])
    def display(self):
        print('________________________BILL_________________________ ')
        for i in range(len(bill.item)):
            print('Product : ',bill.item[i],end='\t\t')
            print('Price : ',bill.item_price[i],end='\t\t')
            print('Quantity : ',bill.qty[i])
        print('Total Bill Amount : ',sum(bill.Bill_Amount))
class pay_by_cash(bill):
    def __init__(self):
        print('Cash to be Paid : ',sum(bill.Bill_Amount))
        cash_recieved=int(input('Enter Cash amount to be given : '))
        if cash_recieved>sum(bill.Bill_Amount):
            print('Cash Returned : ',cash_recieved-sum(bill.Bill_Amount))
    def display(self):
        super().display()

class pay_by_card(bill):
    def __init__(self):
        print('Cash to be Paid : ',sum(bill.Bill_Amount))
        Card_Number=int(input('Enter Debit/Credit Card Number : '))
        cvv=int(input('Enter CVV of Card : '))
    def display(self):
        super().display()

class pay_by_cheque(bill):
    def __init__(self):
        print('Cash to be Paid : ',sum(bill.Bill_Amount))
        Bank=input('Choose Your Bank : ')
        account_no=int(input('Enter Bank Account No.'))
        authentication=input("Enter Authorised person's name : ")

n=int(input('Enter no. of items : '))
for i in range(n):
    b=bill()
print('Total Bill Amount : ',sum(bill.Bill_Amount))
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
class bill:
    item=[]
    item_price=[]
    qty=[]
    Bill_Amount=[]
    def __init__(self):
        bill.item.append(input('Enter a Product : '))
        bill.item_price.append(int(input("Enter it's Price : ")))
        bill.qty.append(int(input("Enter it's Quantity : ")))
        bill.Bill_Amount.append(bill.qty[i]*bill.item_price[i])
    def display(self):
        print('________________________BILL_________________________ ')
        for i in range(len(bill.item)):
            print('Product : ',bill.item[i],end='\t\t')
            print('Price : ',bill.item_price[i],end='\t\t')
            print('Quantity : ',bill.qty[i])
        print('Total Bill Amount : ',sum(bill.Bill_Amount))
class pay_by_cash(bill):
    def __init__(self):
        print('Cash to be Paid : ',sum(bill.Bill_Amount))
        cash_recieved=int(input('Enter Cash amount to be given : '))
        if cash_recieved>sum(bill.Bill_Amount):
            print('Cash Returned : ',cash_recieved-sum(bill.Bill_Amount))
    def display(self):
        super().display()

class pay_by_card(bill):
    def __init__(self):
        print('Cash to be Paid : ',sum(bill.Bill_Amount))
        Card_Number=int(input('Enter Debit/Credit Card Number : '))
        cvv=int(input('Enter CVV of Card : '))
    def display(self):
        super().display()

class pay_by_cheque(bill):
    def __init__(self):
        print('Cash to be Paid : ',sum(bill.Bill_Amount))
        Bank=input('Choose Your Bank : ')
        account_no=int(input('Enter Bank Account No.'))
        authentication=input("Enter Authorised person's name : ")

n=int(input('Enter no. of items : '))
for i in range(n):
    b=bill()
print('Total Bill Amount : ',sum(bill.Bill_Amount))
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
