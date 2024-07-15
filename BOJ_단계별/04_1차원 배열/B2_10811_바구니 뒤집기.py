n,m = map(int,input().split())
basket = []

for x in range(1,n+1):
    basket.append(x)

for x in range(m):
    i, j = map(int,input().split())
    basket = basket[:i-1] + basket[i-1:j][::-1] + basket[j:]

for x in range(len(basket)):
    print(basket[x],end=' ')
