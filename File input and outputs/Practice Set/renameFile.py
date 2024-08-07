with open("File input and outputs\Practice Set\old.txt") as f:
    content=f.read()
with open("File input and outputs\Practice Set\renamed.txt") as f:
    content=f.read(content)