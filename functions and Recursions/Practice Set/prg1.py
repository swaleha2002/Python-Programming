# Write a program using functions to find greatest of three numbers.

def greatest(a,b,c):
    if(a>b and a>c):
        print("greatest is a",a)
    elif(b>a and b>c):
        print("greatest is b",b)
    else:
        print("greatest is c",c)
a = int(input("Enter number a :"))
b = int(input("Enter number b :"))
c = int(input("Enter number c :"))
greatest(a,b,c)
    