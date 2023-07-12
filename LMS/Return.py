#Import ListSplit and DateTime in this module
import ListSplit
import DateTime
#Define ReturnBooks Function
def ReturnBooks():
    #Input borrower name in n variable
    n=input("Enter the Name of Borrower: ")
    #Create Borrow.txt file
    t="Borrow-"+n+".txt"
    
    #Use Try block
    try:
        #Open borrow file in read mode
        f= open(t,"r")
        lines=f.readlines()
        lines=[a.strip("$") for a in lines]
    
        f= open(t,"r")
        info=f.read()
        print(f"info:{info}")
     #Use Except block   
    except:
        print("The borrower name is incorrect")
        ReturnBooks()
    #Create Return.txt file
    Return="Return-"+n+".txt"
    #Open return file in both reading and writing mode
    f= open(Return,"w+")
    f.write("                Library Management System \n")
    f.write("                   Returned By: "+ n+"\n")
    f.write("    Date: " + DateTime.Date()+"    Time:"+ DateTime.Time()+"\n\n")
    f.write("S.N.\t\tBookname\t\tCost\n")

    #Declare Total as 0
    total=0.0
    for i in range(3):
        if ListSplit.BookName[i] in info:
            f= open(Return,"a")
            f.write(str(i+1)+"\t\t"+ListSplit.BookName[i]+"\t\t$"+ListSplit.Cost[i]+"\n")
            ListSplit.Quantity[i]=int(ListSplit.Quantity[i])+1
        total+=float(ListSplit.Cost[i])
            
    print("\t\t\t\t\t\t\t"+"$"+str(total))
    print("Is the book return date expired or not?")#print
    print("Press y for Yes or n for No")
    #Input for y or n
    stat=input()
    if(stat=="y"):
        print("By how many days was the book returned late?")
        #Declare day to store in value of day
        day=int(input("By how long the book returned date has expired?: "))
        #Add fine
        fine=2*day
        f= open(Return,"a")
        f.write("\t\t\t\t\tFine: $"+ str(fine)+"\n")
    #Add total with fine
    total=total+fine
    

    #print Total Cost
    print("Total Cost: "+ "$"+str(total))
    #Open Return file in append mode
    f= open(Return,"a")
    f.write("\t\t\t\t\tTotal Cost: $"+ str(total))
    
    #Open BookStock file in reading and writing mode and store in f    
    f =open("BookStock.txt","w+")
    for i in range(3):
        #Write in f file 
        f.write(ListSplit.BookName[i]+","+ListSplit.AuthorName[i]+","+str(ListSplit.Quantity[i])+","+"$"+ListSplit.Cost[i]+"\n")
