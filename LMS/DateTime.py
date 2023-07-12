#Define function Date
def Date():
    import datetime
    #Print current date
    now=datetime.datetime.now
    #print("Date: ",now().date())
    return str(now().date())
#Define function Time
def Time():
    #Import datetime
    import datetime
    #print current time
    now=datetime.datetime.now
    #print("Time: ",now().time())
    return str(now().time())
