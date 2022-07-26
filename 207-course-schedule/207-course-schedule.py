class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
       #map each course to prerequistes list 
        preMap = {i: [] for i in range(numCourses)}
        for crs,  pre in prerequisites:
            preMap[crs].append(pre)
    
        #visitSet: stores all the nodes you've visited aka courses along the DFS path
        visitSet = set()
        
        def dfs(crs):
            #if course is already in visitSet that means theres a loop in the graph 
            if crs in visitSet:
                return False
            #if prequisites of this course are empty list it tells us course has no                prereq
            if preMap[crs] == []:
                return True
            
            visitSet.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre): return False  
            visitSet.remove(crs)
            preMap[crs] = []
            return True
        
        for crs in range(numCourses):
            if not dfs(crs): return False
        return True