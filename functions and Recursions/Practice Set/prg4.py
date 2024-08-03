# Write a recursive function to calculate the sum of first n natural numbers.

# def sumOfN(n):
#     # Base case: if n is 1, return 1
#     if n == 1:
#         return 1
#     # Recursive case: sum of n is n plus sum of first n-1 numbers
#     else:
#         return n + sumOfN(n - 1)

# # Taking input from the user
# n = int(input("Enter a number: "))
# print("Sum of first", n, "natural numbers is:", sumOfN(n))

def sum(n):
    if(n==1):
        return 1
    return sum(n-1)+n
print(sum(4))


