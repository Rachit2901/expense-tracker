import json
try:
    with open("expenses.json","r") as file:
        expenses=json.load(file)
except FileNotFoundError:
    expenses=[]
def add_expense(name,amt):
    d1={
        "name":name,
        "amount":amt
    }
    expenses.append(d1)
def view_expenses():
    if(len(expenses)==0):
        print("NO EXPENSES")
    else:
        for expense in expenses:
            print(f"{expense['name']}:{expense['amount']}")
def delete_expense(n):
    found=False
    for expense in expenses:
        if(expense['name']==n):
            expenses.remove(expense)
            found=True
            break
    if(found==False):
            print("element not found")
def search_expense(n):
    found=False
    for expense in expenses:
        if(expense['name']==n):
            print(f"{n}:{expense['amount']}")
            found=True
    if(found==False):
            print("element no there")

def statistics():
    if(len(expenses)==0)    :
        print("no data")
    else:
    
        total=0
        x=0
        s=None
        l=None
        m=expenses[0]["amount"]
        for expense in expenses:
            total+=expense["amount"]
            x=max(x,expense["amount"])
            m=min(m,expense["amount"])
        avg=total/len(expenses)
        print(f"average is {avg}")
        print(f"MAXIMUM PURCHASE")
        for expense in expenses:
            if(expense["amount"]==x):
                s=expense["name"]
            if(expense["amount"]==m):
                    l=expense["name"]
        print(f"{s}-{x}")
        print(f"{l}-{m}")
            
    

            
def save():
    with open("expenses.json","w") as file:
        json.dump(expenses,file,indent=4)
    


    
