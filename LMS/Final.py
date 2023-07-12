import Return
import ListSplit
import DateTime
import Borrow

def Final():
    while(True):
        print("        Welcome to the library management system     ")
        print("------------------------------------------------------")
        print("Enter 1. To Display")
        print("Enter 2. To Borrow a book")
        print("Enter 3. To return a book")
        print("Enter 4. To exit")
        try:
            a=int(input("Select a choice from 1-4: "))
            print()
            if(a==1):
                f= open("BookStock.txt","r")
                lines=f.read()
                print(lines)
                print ()
   
            elif(a==2):
                ListSplit.list()
                Borrow.BorrowBooks()
            elif(a==3):
                ListSplit.list()
                Return.ReturnBooks()
            elif(a==4):
                print("Thank you for using LIBRARY MANAGEMENT SYSTEM\t COME AGAIN!!!")
                break
            else:
                print("Enter a valid number from 1-4")
        except ValueError:
            print("Please input as suggested.")
Final()
