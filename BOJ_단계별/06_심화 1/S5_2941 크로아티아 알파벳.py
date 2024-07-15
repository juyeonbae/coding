s = input()
cList = ['c=','c-','dz=','d-','lj','nj','s=','z=']

for i in cList:
    s = s.replace(i,'x')
print(len(s))
