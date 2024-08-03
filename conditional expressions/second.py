a = int(input("enter your age:"))
if(a%2==0):
    print("a is even")
    
if(a>=18):
        print("you are eligible to vote")
elif(a<0):
    print("invalid age")
else:
    print("you are not eligible to vote")
    
print("program ended")