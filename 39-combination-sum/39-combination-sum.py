class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(ind,cur,total):
            if total == target:
                res.append(cur.copy())
                return
            if total > target or ind >= len(candidates):
                return
        
            cur.append(candidates[ind])
            dfs(ind,cur,total+candidates[ind])
            cur.pop()
        
            dfs(ind+1,cur,total)
    
        dfs(0,[],0)
        return res