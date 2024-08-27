# List Comprehension: Write a list comprehension to create a list of squares of numbers from 1 to 10.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
newlist = [x**2 for x in numbers]
print(newlist)