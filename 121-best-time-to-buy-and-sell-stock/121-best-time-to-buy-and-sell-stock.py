class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #sliding window approach
        left, right = 0, 1 #l = buy, R = sell
        maxProfit = 0
    
        while(right < len(prices)):
            if(prices[left] < prices[right]):
                profit = prices[right] - prices[left]
                maxProfit = max(maxProfit, profit)
            if(prices[left] > prices[right]):
                left = right
            right += 1
    
        return maxProfit
        
            
    
    