class Solution:
    def isPalindrome(self, s: str) -> bool:
        x = ''
        for i in s:
            if i.isalpha(): x += i.lower()
            elif i.isdigit(): x += i 
            else: continue

        for i in range(len(x)//2):
            if x[i] != x[-i-1]:
                return False                
        
        return True