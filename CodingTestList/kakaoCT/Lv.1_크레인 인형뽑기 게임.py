# Lv.1 크레인 인형뽑기 게임.py

def solution(board, moves):
    answer = 0  # 사라진 인형 개수
    lng_board = len(board)  # board 크기
    st = []  # 바구니

    for idx in moves:
        for i in range(lng_board):
            if board[i][idx - 1] != 0:
                # board 에서 값을 빼줌
                tmp = board[i][idx - 1]
                board[i][idx - 1] = 0

                # 스택이 비지 않고, top == tmp 인 경우
                if len(st) != 0 and st[-1] == tmp:
                    st.pop()
                    answer += 2
                else:
                    st.append(tmp)
                break # 한 번에 한 개만
    return answer


board = [[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]]
moves = [1, 5, 3, 5, 1, 2, 1, 4]

print(solution(board, moves))
