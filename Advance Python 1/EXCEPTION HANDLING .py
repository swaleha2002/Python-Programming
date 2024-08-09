# # Exception in python can be handled using a try statement. The code that handles the
# exception is written in the except clause.

try:
   a = int(input("Hey, Enter a number: "))
   print(a)
   
except Exception as e:
    print(e)
    
print("Thank you!")

