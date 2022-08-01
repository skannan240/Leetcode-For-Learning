class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if(matrix[r][c]==0):
                    for i in range(len(matrix)):
                        if(matrix[i][c]==0): 
                            continue   
                        matrix[i][c]='0' 
                    for i in range(len(matrix[0])):
                        if(matrix[r][i]==0): 
                            continue   
                        matrix[r][i]='0'
            for c in range(len(matrix[0])):
                if(matrix[r][c]=='0'):
                    matrix[r][c]=0
                