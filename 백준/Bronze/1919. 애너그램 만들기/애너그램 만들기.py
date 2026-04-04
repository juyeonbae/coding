import sys
input = sys.stdin.readline

from collections import Counter 

a = Counter(input().strip())
b = Counter(input().strip())

result = (a | b) - (a & b)
print(sum(result.values()))
