with open("File input and outputs//Practice Set//findword.txt") as f:
    content = f.read()
with open("this_copy.txt","w") as f:
    f.write(content)