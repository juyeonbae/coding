import sys
input = sys.stdin.readline
N = int(input())
lst = [list(input().strip().split()) for _ in range(N)]

groups = {}
for x in lst:
    if x[0] not in groups:
        groups[x[0]] = []
    groups[x[0]].append(x[1])

result = []
for key in sorted(groups.keys()):  # x[0] 오름차순
    sorted_second = sorted(groups[key], reverse=True)  # x[1] 내림차순
    for val in sorted_second:
        result.append([key, val])

for l in result:
    print(*l)