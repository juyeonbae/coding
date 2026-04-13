class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}

        for i in range(len(nums)):
            tmp = target - nums[i]
            if tmp in d:
                return [d[tmp], i]
            d[nums[i]] = i 
    
            