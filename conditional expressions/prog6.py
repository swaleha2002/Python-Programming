# . Write a program to find out whether a given post is talking about “Harry” or not.

post = input("enter the post ")

if("harry" in post.lower()):
    print("This post is talking about harry")
else:
    print("This post is not talking about harry")