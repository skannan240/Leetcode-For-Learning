class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        result = max(nums)
        currentMi, currentMa = 1,1
        
        for i in nums:
            if i == 0:
                currentMi, currentMa = 0,0
                continue
            temp = currentMa * i
            currentMa = max(i * currentMa, i * currentMi, i)
            currentMi = min(temp, i * currentMi, i)
            result = max(result, currentMa)
        return result
            