from typing import List


class Solution: 
    def islandPerimeter(self, grid: List[List[int]]) -> int: 
        row=len(grid) 
        col=len(grid[0])
        perimeter = 0 
        for i in range(row):
            for j in  range(col): 
                if grid[i][j] == 1: 
                    resultToAdd=0
                    #checking if its empty top 
                    resultToAdd += 1 if i-1 < 0 or (i-1 >= 0 and  grid[i-1][j] ==0) else 0
                    #checking if its empty bottom 
                    resultToAdd += 1 if i+1 == row or (i+1 < row and grid[i+1][j] ==0) else 0 
                    #checking if its empty left 
                    resultToAdd += 1 if j-1 < 0 or (j-1 >= 0 and grid[i][j-1] == 0) else 0 
                    #checking if its empty right 
                    resultToAdd += 1 if j+1 == col or (j+1 < col and grid[i][j+1] ==0) else 0  
                    perimeter += resultToAdd
        return perimeter
        


         

print("running script") 
case1= Solution().islandPerimeter([[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]) 
case2= Solution().islandPerimeter([[1]]) 
case3= Solution().islandPerimeter([[1,0]]) 
print(f'case 1 is {case1} ')
print(f'case 2 is {case2} ')
print(f'case 3 is {case3} ')
