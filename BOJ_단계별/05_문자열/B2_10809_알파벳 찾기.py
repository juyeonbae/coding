s = input()
arr = [-1] * 26
for i in s:
    arr[ord(i)-97] = s.index(i)
for i in range(len(arr)):
    print(arr[i],end=' ')

# 출력 형태가 같은지 매번 놓친다. 백준은 아무래도 입출력까지 내가 작성해야해서 까먹는다!!
