# 6. Write a python function which converts inches to cms
def inch_to_cms(inch):
    return inch * 2.54
n = int(input("Enter value in inches:"))
print("the corresponding value in cms is",inch_to_cms(n))
