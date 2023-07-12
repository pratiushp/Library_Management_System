#import DateTime and ListSplit to this module
import DateTime
import ListSplit

#Define BorrowBooks Function
def BorrowBooks():
    #Use loop till user give valid info
    success=False
    while(True):
        FirstName=input("Enter the First Name: ")#Print First Name
        if FirstName.isalpha():
            break
        print("Give the first name in string")
    while(True):
        LastName=input("Enter the Last Name: ")#Print Last Name
        if LastName.isalpha():
            break
        print("Give the last name in string")
    #Create Borrow. txt file        
    Borrow="Borrow-"+FirstName+".txt"
    #Open Borrow file in reading and writing mode and store in f
    f= open(Borrow,"w+")
    f.write("               Library Management System  \n")
    f.write("                   Borrowed By: "+ FirstName+" "+LastName+"\n")
    f.write("    Date: " + DateTime.Date()+"    Time:"+ DateTime.Time()+"\n\n")
    f.write("S.N. \t\t Bookname \t      Authorname \n" )
    
    #Loop continue till user give valid info
    while success==False:
        print("Please select a option below:")#Print
        for i in range(len(ListSplit.BookName)):
            print("Enter", i, "to borrow book", ListSplit.BookName[i])
            
        #Use try block
        try:
            #input a
            a=int(input())
            try:
                if(int(ListSplit.Quantity[a])>0):
                    print("Book is available")
                    #Open Borrow file in append mode and store in f 
                    f= open(Borrow,"a")
                    f.write("1. \t\t"+ ListSplit.BookName[a]+"\t\t  "+ListSplit.AuthorName[a]+"\t\t"+ListSplit.Cost[a]+"\n")

                    ListSplit.Quantity[a]=int(ListSplit.Quantity[a])-1
                    #Open BookStock.txt file in both reading and writing mode 
                    f= open("BookStock.txt","w+")
                    #Use for loop 
                    for i in range(10):
                        f.write(ListSplit.BookName[i]+","+ListSplit.AuthorName[i]+","+str(ListSplit.Quantity[i])+","+ListSplit.Cost[i]+"\n")


                    #For multiple book borrowing code
                    loop=True
                    count=1
                    while loop==True:
                        User_choice=str(input("Do you want to borrow more books? Press y for yes and n for no."))
                        if(User_choice=="y"):
                            count=count+1
                            print("Please select an option below:")
                            for i in range(len(ListSplit.BookName)):
                                print("Enter", i, "to borrow book", ListSplit.BookName[i])
                            a=int(input())
                            if(int(ListSplit.Quantity[a])>0):
                                print("Book is available")
                                with open(Borrow,"a") as f:
                                    f.write(str(count) +". \t\t"+ ListSplit.BookName[a]+"\t\t  "+ListSplit.AuthorName[a]+"\t\t"+ListSplit.Cost[a]+"\n")

                                ListSplit.Quantity[a]=int(ListSplit.Quantity[a])-1
                                f= open("BookStock.txt","w+")
                                for i in range(10):
                                    f.write(ListSplit.BookName[i]+","+ListSplit.AuthorName[i]+","+str(ListSplit.Quantity[i])+","+"$"+ListSplit.Cost[i]+"\n")
                                    success=False
                            else:
                                loop=False
                                break
                        elif (User_choice=="n"):
                            print ("Thank you for borrowing books from us. ")
                            print("")
                            loop=False
                            success=True
                        else:
                            print("Please choose as instructed")
                        
                else:
                    print("Book is not available")
                    BorrowBooks()
                    success=False
            except IndexError:
                print("")
                print("Choose the book according to their number.")
        except ValueError:
            print("")
            print(" Choose as suggested.")
