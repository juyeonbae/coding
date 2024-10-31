s = input()

arr = []
for i in range(len(s)):
    for j in range(len(s)):
        if i + j < len(s):
            arr.append(s[j:i+j+1])

print(len(set(arr)))