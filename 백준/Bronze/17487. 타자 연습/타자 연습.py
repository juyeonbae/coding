import sys
input = sys.stdin.readline

right = ('u', 'i', 'o', 'p', 'h', 
         'j', 'k', 'l', 'n', 'm')
left = ('q', 'w', 'e', 'r', 't', 'y',
       'a', 's', 'd', 'f', 'g', 
       'z', 'x', 'c', 'v', 'b')

s = input().strip()

l, r = 0, 0
for i in s:

    if i.lower() in right:
        r += 1
    if i.lower() in left:
        l += 1

    if i == ' ' or i.isupper():
        if l <= r: l += 1
        else: r += 1
            
print(l, r)
            
        
