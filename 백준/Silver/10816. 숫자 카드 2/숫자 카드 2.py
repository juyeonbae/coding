from collections import Counter

N = int(input())
card = list(map(int, input().split()))

M = int(input())
chk = list(map(int, input().split()))

card_count = Counter(card)
result = [card_count[c] for c in chk]

print(' '.join(map(str, result)))
