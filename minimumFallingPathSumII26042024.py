import time
from typing import List


class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid) 
        found_combinations=[] 
         
        newCombination=[]
        start=time.time() 
        if n ==1: 
            print('finding combinations took no time at all') 
            return grid[0][0]
        while newCombination != None: 
            if newCombination != []: 
                found_combinations.append(newCombination) 
            newCombination=self.findCombination(grid,n,found_combinations)   
        end=time.time() 
        time_it_took=end-start 
        print(f'finding combinations took {time_it_took}s') 
        sums=[] 
        for comb in found_combinations: 
            currentSum=0
            for element in comb: 
                currentSum += element 
            sums.append(currentSum)
        sums.sort()   
        return sums[0]

             

    def findCombination(self,grid,n,existing_combinations:List[List[int]],step=0,currentComb:List[int]=[],previousRow:List[int]=[-1],previousCol=-1): 
        addon=previousRow[len(previousRow)-1] if len(previousRow) > 1 else 0 
        if n-1 == step:  
            for i in range(addon,n): 
                if i in previousRow: 
                    continue
                for j in range(n): 
                    
                    if j == previousCol: 
                        continue                   
                    auxComb= currentComb.copy() 
                    auxComb.append(grid[i][j])  
                    # print(f" checked for {auxComb}") 
                    if auxComb not in existing_combinations :
                        return auxComb 
            return  None 
        else : 
            for row in range(addon,n):  
                if row in previousRow: 
                    continue
                for col in range(n):  
                    if col == previousCol:
                        continue 
                    if len(previousRow)-1 <row: 
                        return None  
                    auxComb=currentComb.copy() 
                    auxComb.append(grid[row][col])  
                    auxRow=previousRow.copy() 
                    auxRow.append(row)
                    nextComb=self.findCombination(grid,n,existing_combinations,step+1,auxComb,auxRow,col)  
                    if nextComb == None:  
                        continue 
                    if nextComb not in existing_combinations: 
                        return nextComb 
            return None
    # def checkIfNeedsToLoop(self,current_comb,n,existing_combinations):
    #     e_c_copy=existing_combinations.copy() 
    #     onlyLast=list(map(lambda e: e[:-1],e_c_copy)   )
    #     amt=onlyLast.count(current_comb) 
    #     if amt >= n-1: 
    #         return False 
    #     return True


        


         

print("running script") 
case1= Solution().minFallingPathSum(grid = [[1,2,3],[4,5,6],[7,8,9]]) 
case2= Solution().minFallingPathSum(grid = [[7]])  
case3= Solution().minFallingPathSum(grid= [[11,28,-35,-96,73],[15,-83,82,-51,-11],[-49,1,42,-95,53],[63,52,-19,15,-89],[-80,60,90,25,-50]])
case4 =Solution().minFallingPathSum(grid=[[-73,61,43,-48,-36],[3,30,27,57,10],[96,-76,84,59,-15],[5,-49,76,31,-7],[97,91,61,-46,67]] )
print(f'case 1 is {case1} ')
print(f'case 2 is {case2} ') 
print(f'case 3 is {case3} ')  
print(f'case 4 is {case4}')

