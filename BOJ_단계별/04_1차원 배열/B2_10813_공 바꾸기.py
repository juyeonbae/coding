n, m = map(int,input().split())
basket = [0] * n

for x in range(1,n+1):
    basket[x-1] = x

for y in range(m):
    i,j = map(int,input().split())
    basket[i-1], basket[j-1] = basket[j-1],basket[i-1]

for z in range(len(basket)):
    print(basket[z],end=' ')

