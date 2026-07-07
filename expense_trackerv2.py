
l1=[]
try:
    with open("expense.txt","r") as file:
        for line in file:
            data=line.strip().split(",")
            l1.append([int(data[0]),data[1]])
except FileNotFoundError:
    l1=[]

        

class tracker:
    
    
    def __init__(self,amt,name):
        self.name=name
        self.amt=amt
        
    def add_expense(self,l1):
        
        l1.append([self.amt,self.name])
        print("expense added")
    def view_expense(self,l1):
        for i in range(0,len(l1)):
            print(f"name={l1[i][1]}")
            print(f"amount={l1[i][0]}")
   
   
        
x=None
while True:
        print("===== Expense Tracker =====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Delete Expense")
        print("4. Total Spent")
        print("5.Search Expense")
        print("6.Edit Expense")
        print("7.Statistics")
        print("8. Exit")


        x=int(input("enter choice"))
      
        if(x==1):
            amt=int(input("enter amount"))
            name=str(input("enter name of expense"))
            c=tracker(amt,name)
            c.add_expense(l1)
        elif(x==2):
            if(len(l1)==0):
                print("no record found")
            else:
                c=tracker(0,0)
                c.view_expense(l1)
        elif(x==3):
            x=str(input("enter expense"))
            found=False
            for i in range(0,len(l1)):

                if(l1[i][1]==x):
                    l1.remove(l1[i])
                    found=True
                    break
            if(found==False):
                    print("element not found")
                

                
            
            
        elif(x==4):
            total=0
            for i in range(0,len(l1)):
                total+=l1[i][0]
            print(f"TOTAL={total}")
        elif(x==5):
            m=str(input("enter expense"))
            found=False
            for el in l1:
                
                if(el[1]==m):
                    print(f"name={el[1]}")
                    print(f"price={el[0]}")
                    found=True
                    break
            if(found!=True):

                print("expense not found")
        elif(x==6):
            m=str(input("enter expense: "))
            for el in l1:
                if(el[1]==m):
                    el[1]=str(input("enter name"))
                    el[0]=int(input("enter amount"))

            
        elif(x==7):
            print(f"Total Expenses:{len(l1)}")
            if(len(l1)==0):
                print("no element found")
            else:
                i=0
                r=l1[0][0]
                m=l1[0][0]
                s=l1[0][1]
                k=l1[0][1]
                while i<len(l1):
                    if(l1[i][0]>r):
                        r=l1[i][0]
                        s=l1[i][1]
                    elif(l1[i][0]<m):
                        m=l1[i][0]
                        k=l1[i][1]
                    i+=1


                total=0
                

                print("maximum expense:\n")
                print(f"{r}:{s}")
                print(f"{m}:{k}")
                for el in l1:
                    total+=el[0]
                print(f"average={total/len(l1)}")

            


        elif(x==8):
            print("PROGRAMME ENDED")
            with open("expense.txt","w") as file:
                for i in range(0,len(l1)):                  
                    file.write(f"{l1[i][0]},{l1[i][1]}\n")
            break
            
        else:
            print("invalid input")



            

            

        
        
        


            


