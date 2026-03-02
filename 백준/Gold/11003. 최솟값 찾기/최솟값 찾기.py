import sys 
import collections 
input = sys.stdin.readline 
print = sys.stdout.write 
def main() : 
    n, l = map(int, input().split()) 
    d = list(map(int, input().split())) 
    dq = collections.deque() 
    
    for i in range(n) : 
        while dq and dq[-1] > d[i] : 
            dq.pop() 
        
        dq.append(d[i]) 
        
        if i >= l and dq[0] == d[i - l] : 
            dq.popleft()
            
        print(f"{dq[0]} ") 
    
if __name__ == "__main__" : 
    main()