# Write a program to find out whether a student has passed or failed if it requires a
# total of 40% and at least 33% in each subject to pass. Assume 3 subjects and
# take marks as an input from the user.
a = int(input("enter marks 1:"))
b = int(input("enter marks 2:"))
c = int(input("enter marks 3:"))

# check for percentage
total_percentage =(100*(a+b+c))/300

if(total_percentage>=40 and a>=33 and b>=33 and c>33):
    print("pass")
else:
    print("fail")