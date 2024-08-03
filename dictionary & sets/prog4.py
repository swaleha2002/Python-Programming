# What will be the length of following set s:
s = set()
s.add(20)
s.add(20.0)
s.add('20') 
print(s)
# output is {20,"20"} ->because python consider 20 and20.0 as same
