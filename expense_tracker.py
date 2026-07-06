
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
        print("5. Exit")


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
            for i in range(0,len(l1)):

                if(l1[i][1]==x):
                    l1.remove(l1[i])
                    break
                if(i==len(l1)-1 and l1[i][1]!=x):
                    print("not found")

                
            
            
        elif(x==4):
            total=0
            for i in range(0,len(l1)):
                total+=l1[i][0]
            print(f"TOTAL={total}")
        elif(x==5):
            print("PROGRAMME ENDED")
            break
        else:
            print("invalid input")



            

            

        
        
        


            


