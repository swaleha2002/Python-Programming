word = "Donkey"
with open("File input and outputs\Practice Set\wordreplace.txt","r") as f:
    content = f.read()
contentNew = content.replace(word,"########")
with open("File input and outputs\Practice Set\wordreplace.txt","w") as f:
    f.write(contentNew)
    
# for list of words
# word = ["Donkey","bad","worst"]
# with open("File input and outputs\Practice Set\wordreplace.txt","r") as f:
#     content = f.read()
# for word in words:
#     contentNew = content.replace(word,"#"*len(word))
# with open("File input and outputs\Practice Set\wordreplace.txt","w") as f:
#     f.write(contentNew)


