# B1_11655_ROT13.py

s = input()

answer = ''
for i in s:
    if i.isupper():
        answer += chr((((ord(i) + 13) - 65) % 26)+65)
    elif i.islower():
        answer += chr((((ord(i) + 13) - 97) % 26)+97)
    else:
        answer += i

print(answer)
