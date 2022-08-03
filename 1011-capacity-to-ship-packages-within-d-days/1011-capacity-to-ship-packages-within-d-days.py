class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = max(weights)
        r = sum(weights)
        
        while l < r:
            mid = (l + r) // 2
            
            if self.can_ship(mid, weights,days):
                r = mid
            else:
                l = mid + 1
        return r
    
    
    def can_ship(self, candidate, weights, days):
        cur_weight = 0
        days_taken = 1
        
        for weight in weights:
            cur_weight += weight
            
            if cur_weight > candidate:
                days_taken += 1
                cur_weight = weight
                
        return days_taken <= days
            