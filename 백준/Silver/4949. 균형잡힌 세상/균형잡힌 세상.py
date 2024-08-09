while True:
    try:
        s = input().strip('\n')
        if s == '.':
            break

        st, chk = [], True
        for i in s:
            if i == '(' or i == '[':
                st.append(i)

            elif i == ')':
                if len(st) == 0 or st[-1] != '(':
                    chk = False
                else: st.pop()
            elif i == ']':
                if len(st) == 0 or st[-1] != '[':
                    chk = False
                else: st.pop()

        if chk and not st:
            print("yes")
        else:
            print("no")

    except EOFError:
        break