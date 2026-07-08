print("===== Expense Tracker =====")
print("1. Add Expense")
print("2. View Expenses")
print("3. Delete Expense")
print("4. Search Expense")
print("5.statistics")
print("6. Exit")

import tracker
x=None

while True:
    x=int(input("choice:"))
    if(x==1):
        name=str(input("enter name"))
        amount=int(input("enter amount"))
        tracker.add_expense(name,amount)
    elif(x==2):
        tracker.view_expenses()
    elif(x==3):
        name=str(input("enter name :"))
        tracker.delete_expense(name)
    elif(x==4):
        name=str(input("enter name :"))
        tracker.search_expense(name)
    elif(x==5):
        tracker.statistics()
    elif(x==6):
        tracker.save()
        break
    else:
        print("invalid input")


