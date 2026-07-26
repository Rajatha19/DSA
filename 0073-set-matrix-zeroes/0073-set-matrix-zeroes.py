class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
       m,n=len(matrix),len(matrix[0])
       first_r0=False
       first_c0=False
       for row in range(m):
        for col in range(n):
            if matrix[row][col]==0:
                if row==0:
                    first_r0=True
                if col==0:
                    first_c0=True
                matrix[row][0]=matrix[0][col]=0
       for row in range(1,m):
        for col in range(1,n):
            matrix[row][col]=0 if matrix[0][col]==0 or matrix[row][0]==0 else matrix[row][col]
       if first_r0:
        for col in range(n):
            matrix[0][col]=0
       if first_c0:
        for row in range(m):
            matrix[row][0]=0  
                