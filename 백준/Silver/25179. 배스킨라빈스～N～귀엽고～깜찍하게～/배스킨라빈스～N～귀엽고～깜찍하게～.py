n, m = map(int, input().split())
print("Can win" if 0 < (n-1) % (m+1) <= m else "Can't win")