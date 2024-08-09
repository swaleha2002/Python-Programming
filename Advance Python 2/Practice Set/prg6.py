# . Write a program to find the maximum of the numbers in a list using the reduce
# function.
import reduce
a = [1,2,3,4,55,65,50,111,23546]

def greater(a,b):
    if(a>b):
        return a
    return b
print(reduce(greater,1))