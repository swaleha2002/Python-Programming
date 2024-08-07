with open("File input and outputs//Practice Set//findword.txt")as f:
    content = f.read()
if("Python" in content):
    print("Yes python is present")
else:
    print("not present")