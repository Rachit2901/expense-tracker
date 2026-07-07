try:
    with open("expense.txt","r") as file:
        print(file.read())
except:
    l1=[]