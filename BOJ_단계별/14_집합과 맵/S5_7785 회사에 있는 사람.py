import sys
input = sys.stdin.readline

n = int(input())

log = {}
for i in range(n):
    name, state = map(str, input().split())
    log[name] = state
    
    if state == 'leave':
        del(log[name])

print('\n'.join(sorted(log, reverse=True)))
