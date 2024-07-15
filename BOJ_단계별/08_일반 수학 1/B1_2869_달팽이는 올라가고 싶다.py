import math
a,b,v = map(int,input().split())
print(math.ceil((v-b)/(a-b)))

'''
반올림 : round()
올림 : import math / math.ceil() 
내림 : import math / math.floor()
'''
