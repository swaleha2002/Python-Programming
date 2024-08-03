# Write a program to find the greatest of four numbers entered by the user.
a = int(input("enter your number 1:"))
b = int(input("enter your number 2:"))
c = int(input("enter your number 3:"))
d = int(input("enter your number 4:"))

if(a>b and a>c and a>d):
    print("number a is the greatest")
elif(b>a and b>c and b>d):
    print("number b is the greatest")
elif(c>a and c>b and c>d):
    print("number c is the greatest")
else:
    print("d is the greatest")
