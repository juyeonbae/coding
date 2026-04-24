def solution(id_list, report, k):
    # 이용자 ID / 신고한 이용자 ID / 정지 기준 신고 횟수 
    answer = []
    
    # 한 번에 한 명의 유저만 신고 / 신고 횟수 제한 없음
    # 한 유저를 여러 번 신고 가능하나, 동일한 유저에 대한 신고는 1회 처리
    
    id = {}  # id = {'muzi': 0, 'frodo': 1, 'apeach': 2, 'neo': 3}
    for idx, name in enumerate(id_list):
        id[name] = idx
     
    report_set = set(report)
    print(report_set)
    for r in report:
        x, y = r.split("")
    
    # k번 이상 신고된 유저는 정지/신고한 사람에게 정지 메일 보냄 
    
    return answer