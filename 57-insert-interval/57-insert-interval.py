class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        for i in range(len(intervals)):
            #intervals[i][0] refers to the i'th interval in intervals and 0th is the
            #first interval within that
            #newInterval[1] compares end value of new interval with the start value of             the ith interval in intervals
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            else:
                newInterval = [min(newInterval[0], intervals[i][0]),max(newInterval[1], intervals[i][1])]
        res.append(newInterval)
        
        return res
                               