def solution(players, callings):
    # {player:현재 인덱스} 저장하는 딕셔너리
    p_dict = {player: i for i, player in enumerate(players)}

    for call in callings:
        # 호출된 플레이어의 현재 인덱스
        idx = p_dict[call]

        # 리스트에서 바로 앞 플레이어와 위치 교환
        prev = players[idx-1]
        players[idx-1], players[idx] = players[idx], players[idx-1]

        # 딕셔너리에서도 위치 갱신
        p_dict[call] -= 1
        p_dict[prev] += 1

    return players
