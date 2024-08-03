# Write a program to fill in a letter template given below with name and date.

letter = '''
Dear <|Name|>,
You are selected!
<|Date|>
''' 
print (letter.replace("<|Name|>","swaleha").replace("<|Date|>","5th december 2040"))