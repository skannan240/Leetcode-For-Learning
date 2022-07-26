class Solution:
    def findMin(self, nums: List[int]) -> int:
        #variation of binary search
        result = nums[0]
        leftP = 0
        rightP = len(nums) - 1
        
        while leftP <= rightP:
            if nums[leftP] < nums[rightP]:
                result = min(result, nums[leftP])
                break
            middleValue = (leftP + rightP) // 2
            result = min(result, nums[middleValue])
            if nums[middleValue] >= nums[leftP]:
                leftP = middleValue + 1
            else:
                rightP = middleValue - 1
        return result