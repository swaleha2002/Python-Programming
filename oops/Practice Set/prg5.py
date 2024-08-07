# Write a Class ‘Train’ which has methods to book a ticket, get status (no of seats)
# and get fare information of train running under Indian Railways.
from random import randint
class Train:
    
    def __init__(self,trainNo):
        self.trainNo = trainNo
        
    def book(self,frm,to):
        print(f"Ticket is booked in train No:{self.trainNo} from {frm} to {to}")
        
    def getStatus(self):
       print(f"Train no: {self.trainNo} running on time")
        
    def getFare(self,frm,to):
        print(f"Ticlet fare in train No:{self.trainNo} from {frm} to {to} is {randint(222,555)}")
        
t = Train(123456)
t.book("Rampur","Delhi")
t.getStatus()
t.getFare("Rampur","Delhi")
        