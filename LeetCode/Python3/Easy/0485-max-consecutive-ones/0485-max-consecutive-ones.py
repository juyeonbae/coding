class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        cnt, mx = 0, 0
        for i in nums:
            if i == 0:
                cnt = 0
            else:
                cnt += 1

            if mx < cnt:
                    mx = cnt
                    
        return mx