#Define function list
def list():
    #Define Global variable
    global BookName
    global AuthorName
    global Quantity
    global Cost
    
    BookName=[]
    AuthorName=[]
    Quantity=[]
    Cost=[]
    #Open BookStock file in read mode 
    f= open("BookStock.txt","r")
        
    lines=f.readlines()
    lines=[x.strip('\n') for x in lines]
    
    for i in range(len(lines)):
        
        b=0
        for j in lines[i].split(','):
            
            if(b==0):
                BookName.append(j)
            elif(b==1):
                AuthorName.append(j)
            elif(b==2):
                Quantity.append(j)
            elif(b==3):
                Cost.append(j.strip("$"))
            b+=1
