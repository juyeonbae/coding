import sys
input = sys.stdin.readline

a,b,c,d,e,f = map(int,input().split())
print((c*e-b*f)//(a*e-b*d), (a*f-d*c)//(a*e-b*d))

'''
연립방정식
ax + by = c
dx + ey = f

aex + bey = ce
bdx + bey = bf

(ae-bd)x = ce-bf
x = (ce-bf)/(ae-bd)
y = (af-dc)/(ae-bd)
'''
