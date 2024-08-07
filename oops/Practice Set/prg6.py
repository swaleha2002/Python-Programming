# Can you change the self-parameter inside a class to something else (say
# “harry”). Try changing self to “slf” or “harry” and see the effects.
from random import randint
class Train:
    
    def __init__(slf,trainNo):
        slf.trainNo = trainNo
        
    def book(slf,frm,to):
        print(f"Ticket is booked in train No:{slf.trainNo} from {frm} to {to}")
        
    def getStatus(slf):
       print(f"Train no: {slf.trainNo} running on time")
        
    def getFare(slf,frm,to):
        print(f"Ticlet fare in train No:{slf.trainNo} from {frm} to {to} is {randint(222,555)}")
        
t = Train(123456)
t.book("Rampur","Delhi")
t.getStatus()
t.getFare("Rampur","Delhi")
        