# S4_3986_좋은 단어.py

n = int(input())

cnt = 0
for i in range(n):
    s = input()

    st = []
    for j in range(len(s)): # s 돌면서 스택이 비었거나 top과 다른 문자이면 push
        if len(st) == 0:
            st.append(s[j])
        elif st[-1] == s[j]: # top과 문자가 같으면 pop
            st.pop()
        else:
            st.append(s[j])

    if len(st) == 0: # 스택이 비었으면 좋은 단어이므로, cnt += 1
        cnt += 1

print(cnt)