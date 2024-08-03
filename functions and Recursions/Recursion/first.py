# Recursion is a function which calls itself.

# factorial of n
def factorial(n):
    if(n==1 or n==0):
        return 1
    return n*factorial(n-1)
n = int(input("Enter a number:"))
print("factorial of a number is:",factorial(n))