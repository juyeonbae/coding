s = input()

st = []
cnt = 0

for i in range(len(s)):
    if s[i] == '(':  # 여는 괄호 스택에 추가
        st.append('(')
    else:  # 닫는 괄호인 경우
        st.pop()  # 마지막 여는 괄호를 제거
        if s[i-1] == '(':  # 직전 괄호가 여는 괄호라면 레이저
            cnt += len(st)  # 스택의 크기만큼 조각 추가
        else:  # 직전 괄호가 닫는 괄호라면 막대기의 끝
            cnt += 1  # 조각 하나 추가

print(cnt)
