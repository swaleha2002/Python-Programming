# Write a program to filter a list of numbers which are divisible by 5.
def divisiblebyFive(n):
    if(n%5 == 0):
        return True
    return False
a = [1,2,3,4,55,50,10]

f = list(filter(divisiblebyFive,a))
print(f)