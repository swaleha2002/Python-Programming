def generateTable(n):
    table = ""
    for i in range(1,11):
        table +=f"{n} X {i}={n*i}\n"
    with open("File input and outputs\Practice Set\table","w") as f:
        f.write(table)
for i in range(1,11):
        generateTable(i)