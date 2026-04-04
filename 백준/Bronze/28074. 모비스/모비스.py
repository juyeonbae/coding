s = set(input().strip())
chk = set(('M', 'O', 'B', 'I', 'S')) 

answer = s & chk 

for c in chk:
    if c not in answer:
        print("NO")
        break

else:
    print("YES")