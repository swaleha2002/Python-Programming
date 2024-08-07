with open("File input and outputs//Practice Set//findword.txt") as f:
    content1=f.read()
with open("File input and outputs/this_copy.txt") as f:
    content2=f.read()
if(content1==content2):
    print("Content match!")
else:
    print("Content do not match!")
    