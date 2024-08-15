s = input()

st, tot = [], 0  # 스택과 결과를 저장할 변수
valid = True  # 입력 문자열의 유효성을 확인하기 위한 변수

for i in s:
    if i == '(' or i == '[':  # '(' 또는 '['가 입력되면 스택에 추가
        st.append(i)

    elif i == ')':  # ')'가 입력된 경우
        if len(st) == 0 or '(' not in st:  # 스택이 비어있거나 짝이 맞지 않는 경우
            valid = False
            break
        elif st[-1] == '(':  # 스택의 최상단이 '('이면
            st.pop()  # '('를 제거하고
            st.append(2)  # 2를 스택에 추가
        else:  # 스택의 최상단이 숫자인 경우
            tmp = 0
            while len(st) != 0:
                top = st.pop()
                if str(top).isdigit():  # 숫자를 만나면
                    tmp += top  # 임시 변수에 더해줌
                elif top == '(':  # '('를 만나면
                    tmp *= 2  # 2를 곱한 후
                    st.append(tmp)  # 계산 결과를 스택에 추가
                    break  # 루프 종료
                else:  # '['를 만나거나 잘못된 입력인 경우
                    valid = False
                    break

    elif i == ']':  # ']'가 입력된 경우
        if len(st) == 0 or '[' not in st:  # 스택이 비어있거나 짝이 맞지 않는 경우
            valid = False
            break
        elif st[-1] == '[':  # 스택의 최상단이 '['이면
            st.pop()  # '['를 제거하고
            st.append(3)  # 3을 스택에 추가
        else:  # 스택의 최상단이 숫자인 경우
            tmp = 0
            while len(st) != 0:
                top = st.pop()
                if str(top).isdigit():  # 숫자를 만나면
                    tmp += top  # 임시 변수에 더해줌
                elif top == '[':  # '['를 만나면
                    tmp *= 3  # 3을 곱한 후
                    st.append(tmp)  # 계산 결과를 스택에 추가
                    break  # 루프 종료
                else:  # '('를 만나거나 잘못된 입력인 경우
                    valid = False
                    break

# 모든 처리가 끝난 후 스택에 '(' 또는 '['가 남아 있으면 잘못된 입력으로 간주
if not valid or any(c in st for c in '(['):
    tot = 0
else:
    tot = sum(st)  # 스택에 남아 있는 숫자들을 더해서 결과를 구함

print(tot)  # 최종 결과 출력
