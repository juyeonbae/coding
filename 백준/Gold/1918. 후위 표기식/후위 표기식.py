import sys
input = sys.stdin.readline

s = input().strip()
st = []
answer = ''

x = {'+': 1, '-': 1, '*': 2, '/': 2, '(': 0}

for i in s:
    # 문자를 만나면 answer에 추가
    if i.isalpha():
        answer += i 
    
    elif i == '(':
        st.append(i)

    elif i == ')':
        while st and st[-1] != '(':
            answer += st.pop()
        st.pop()

    elif i in x:
        # st.top에 있는 연산자의 우선순위가 현재 연산자보다 크거나 같으면 계속 pop
        while st and x[st[-1]] >= x[i]:
            answer += st.pop()
        st.append(i)

# 스택에 남은 연산자들 모두 처리 
while st:
    answer += st.pop()

print(answer)

