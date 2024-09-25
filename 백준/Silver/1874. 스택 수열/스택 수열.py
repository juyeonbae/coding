n = int(input())

cnt, st, op, tmp = 1, [], [], True
for i in range(n):
    num = int(input())  # 4 3 6 8 7 5 2 1

    while cnt <= num:
        st.append(cnt)
        op.append('+')
        cnt += 1

    if st and st[-1] == num:
        op.append('-')
        st.pop()

    else:
        tmp = False
        break

if not tmp:
    print('NO')
else:
    print('\n'.join(op))
