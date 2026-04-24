def solution(data, ext, val_ext, sort_by):
    answer = []
    # data에서 ext 값이 val_ext보다 작은 데이터만 뽑기
    num = {'code': 0, 'date': 1, 'maximum': 2, 'remain': 3}
    x = num[ext]  # 
    for i in range(len(data)):
        if data[i][x] < val_ext:
            answer.append(data[i])
        
    # sort_by에 해당하는 값을 기준으로 오른차순 정렬 
    y = num[sort_by]
    answer = sorted(answer, key=lambda x: x[y])

    return answer