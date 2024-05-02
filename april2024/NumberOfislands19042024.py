from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m= len(grid) 
        n=len(grid[0]) 
        island_dic={} 
        island_index=0
        for i in range(m):
            for j in range(n):  
                if grid[i][j] == '1':  
                    is_already_there=False 
                    if i == 2 and j == 0:
                        print('here')
                    for key, values in island_dic.items():
                        for value in values:
                            if value == f'{i}-{j}':
                                is_already_there =True 
                                break 
                        if is_already_there:
                            break 
                    if not is_already_there: 
                        island_index += 1
                        island_dic[island_index]= self.getneighboors(i,j,m,n,grid) 
                        island_dic[island_index] = self.takeAwayRepetitive(island_dic[island_index])                 
        return len(island_dic)
    def getneighboors(self,i,j,m,n,grid,cNeighboors:List[str]=[]):  
        if i >= n or j >= m : 
            return [] 
        else: 
            if grid[i][j] == '0': 
                return []
            cNeighboors.append(f'{i}-{j}') 
            if self.getneighboors(i+ 1,j,m,n,grid,cNeighboors) != 'stop': 
                cNeighboors.extend(self.getneighboors(i+ 1,j,m,n,grid,cNeighboors))   
            cNeighboors.extend(self.getNeighboorsHorizontal(i,j,m,n,grid,cNeighboors))
            return cNeighboors 
    def getNeighboorsHorizontal(self,i,j,m,n,grid,cNeighboors):
        if i >= n or j >= m: 
            return [] 
        else:  
            if grid[i][j] == '0': 
                return 'stop'
            cNeighboors.append(f'{i}-{j}')  
            if self.getNeighboorsHorizontal(i,j + 1,m,n,grid,cNeighboors) != 'stop':
                cNeighboors.extend(self.getNeighboorsHorizontal(i,j + 1,m,n,grid,cNeighboors))   
            if self.getNeighboorsVertical(i+1,j,m,n,grid,cNeighboors) != 'stop':    
                cNeighboors.extend(self.getNeighboorsVertical(i+1,j,m,n,grid,cNeighboors))
            return cNeighboors 
    def getNeighboorsVertical(self,i,j,m,n,grid,cNeighboors): 
        if i >= n or j >= m: 
            return [] 
        else:   
            if grid[i][j] == '0': 
                return 'stop'
            cNeighboors.append(f'{i}-{j}')  
            if self.getNeighboorsVertical(i,j+1,m,n,grid,cNeighboors) != 'stop':
                cNeighboors.extend(self.getNeighboorsVertical(i,j+1,m,n,grid,cNeighboors))
            return cNeighboors 
    def takeAwayRepetitive(self,cNeighboors): 
        # tuple_data = [tuple(sublist) for sublist in  cNeighboors]
        unique_set = set(cNeighboors)
        unique_neighboors = list(unique_set) #[list(t) for t in unique_set] 
        return unique_neighboors

    # def getHorizontalAndVerticalNeighboors(self,i,j,m,n,grid,cMembers=[]): 
    #     cMembers.append([f'{i}-{j}'])   
    #     if i < n and j < m and  grid[i][j] == '1': 
    #         cMembers.extend(self.getHorizontalAndVerticalNeighboors(i+1,j+1,m,n,grid,cMembers))
    #     else: 
    #         return []
    #     return cMembers
        # while addOnI + i+1 < m: 
        #     addOnJ=0 
        #     while addOnJ + j+1 < n: 
        #         if grid[addOnI + i][addOnJ + j] == '1': 
        #             cMembers.extend(self.getHorizontalAndVerticalNeighboors(i+ addOnI+1,j+ addOnJ+1,m,n,grid,cMembers))
        #         addOnJ +=1
        #     addOnI += 1
        # return cMembers
    #                 if not self.isPosInListAlready(i,j,islandsFound): 
    #                     addOnI=0 
    #                     currentIsland=[]   
    #                     zeroCounter=0
    #                     while i + addOnI < m:
    #                         addOnJ=0  
    #                         while j+ addOnJ < n: 
    #                             if grid[i + addOnI][j+ addOnJ] == '1': 
    #                                 currentIsland.append([i+ addOnI,j+ addOnJ]) 
    #                             elif   
    #                             addOnJ += 1
    #                         addOnI += 1  
    #                     islandsFound.append(currentIsland)  
    #     print('this is the islands found for this case') 
    #     print(islandsFound)
    #     return len(islandsFound)     
    # def isPosInListAlready(self,i,j,islandsFound:List[List[List[str]]]): 
    #     for island in islandsFound: 
    #         for pos in island: 
    #             if i == pos[0] and j == pos[1]: 
    #                 return True 
    #     return False



        
        


         

print("running script") 
case1= Solution().numIslands([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]) 
case2= Solution().numIslands([["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]) 
print(f'case 1 is {case1} ')
print(f'case 2 is {case2} ') 

# dic={'1-1':['0-1','0-2'], '1-2':['1,5']} 
# print(dic.values().get(0))
# print('0-1' in dic.values())



