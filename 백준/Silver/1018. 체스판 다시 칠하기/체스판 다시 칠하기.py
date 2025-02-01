import sys

input = sys.stdin.readline

N, M = map(int, input().split())

board = []
for i in range(N):
  st = input()
  board.append(st)
  
  
def in_range(x, y):
  return 0 <= x + 7 < N and 0 <= y + 7 < M
  
    
def chk(x, y):
  wh = ['WBWBWBWB',
        'BWBWBWBW',
        'WBWBWBWB',
        'BWBWBWBW',
        'WBWBWBWB',
        'BWBWBWBW',
        'WBWBWBWB',
        'BWBWBWBW']
        
  bl = ['BWBWBWBW',
        'WBWBWBWB',
        'BWBWBWBW',
        'WBWBWBWB',
        'BWBWBWBW',
        'WBWBWBWB',
        'BWBWBWBW',
        'WBWBWBWB']
        
  wh_cnt, bl_cnt = 0, 0
        
  for i in range(8):
    for j in range(8):
      
      cur = board[x+i][y+j]
      
      if cur != wh[i][j]:
        wh_cnt += 1
      
      if cur != bl[i][j]:
        bl_cnt += 1
        
  return min(wh_cnt, bl_cnt)
  
  
lst, cnt = [], 0
for i in range(N):
  for j in range(M):
    if in_range(i, j):
      cnt = chk(i, j)
      lst.append(cnt)
      
print(min(lst))