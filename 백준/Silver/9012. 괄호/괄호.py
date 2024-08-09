T = int(input())
for tc in range(T):
    s = input()

    st, chk = [], True
    for i in s:
        if i == '(':
            st.append(i)
        else:
            if len(st) == 0:
                chk = False
                break
            else:
                if st[-1] == '(':
                    st.pop()

    if chk and not st:
        print("YES")
    else:
        print("NO")