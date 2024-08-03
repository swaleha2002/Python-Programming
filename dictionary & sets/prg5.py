# Create an empty dictionary. Allow 4 friends to enter their favorite language as
# value and use key as their names. Assume that the names are unique.

d={}

n1 = input("enter your name:")
l1 = input("enter your favourite language 1:")
d.update({n1:l1})
n2 = input("enter your name:")
l2 = input("enter your favourite language 2:")
d.update({n2:l2})
n3 = input("enter your name:")
l3 = input("enter your favourite language 3:")
d.update({n3:l3})
n4 = input("enter your name:")
l4 = input("enter your favourite language 4:")
d.update({n4:l4})

print(d)