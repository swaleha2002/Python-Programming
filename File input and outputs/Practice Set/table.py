# import os

# def generateTable(n):
#     table = ""
#     for i in range(1, 11):
#         table += f"{n} X {i} = {n * i}\n"
#     # Create the directory if it doesn't exist
#     os.makedirs("File input and outputs/Practice Set", exist_ok=True)
#     with open(f"File input and outputs/Practice Set/table_{n}.txt", "w") as f:
#         f.write(table)

# for i in range(1, 11):
#     generateTable(i)

def generateTable(n):
    table = ""
    for i in range(1, 11):
        table += f"{n} X {i} = {n * i}\n"
        with open(f"File input and outputs/Practice Set/table_{n}.txt", "w") as f:
            f.write(table)
            
for i in range(1, 11):
 generateTable(i)
