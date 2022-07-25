class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSubArray = nums[0]
        currSum = 0
        
        for i in nums:
            if currSum < 0:
                currSum = 0
            currSum += i
            maxSubArray = max(maxSubArray, currSum)
        return maxSubArray