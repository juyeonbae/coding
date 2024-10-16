def dfs(computers, visited, v):
    visited[v] = True

    for i in range(len(computers)):
        if computers[v][i] == 1 and not visited[i]:
            dfs(computers, visited, i)


def solution(n, computers):
    visited = [False] * n
    network_cnt = 0

    for i in range(n):
        if not visited[i]:
            dfs(computers, visited, i)
            network_cnt += 1

    return network_cnt