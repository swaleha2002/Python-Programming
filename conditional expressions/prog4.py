# Write a program to find whether a given username contains less than 10
# characters or not.

username = input("enter username:")
if(len(username)<10):
    print("contains less than 10 character")
else:
    print("contains more characters")