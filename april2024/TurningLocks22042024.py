from collections import deque
from typing import List


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:  
        if '0000' in deadends: 
            return -1
        deadends = set(deadends)
        queue=deque([('0000',0)])  
        visited_combinations=set('0000')
        while queue:
            current_combination,moves= queue.popleft()  
            if target == current_combination: 
                return moves
            for i in range(4): 
                for addOn in [-1,1]:  
                    next_digit=(int(current_combination[i])+ addOn) % 10
                    next_combination=(
                        current_combination[:i] + str(next_digit)+ current_combination[i+1:]
                    ) 
                    if next_combination not in visited_combinations and next_combination not in deadends: 
                        visited_combinations.add(next_combination)
                        queue.append(((next_combination,moves+1)))
        return -1






         

print("running script") 
case1= Solution().openLock(deadends = ["0201","0101","0102","1212","2002"], target = "0202") 
case2= Solution().openLock(deadends = ["8888"], target = "0009") 
case3= Solution().openLock(deadends = ["8887","8889","8878","8898","8788","8988","7888","9888"], target = "8888") 
case4=Solution().openLock(deadends =["0000"],target ="8888")
print(f'case 1 is {case1} ') 
print(f'case 2 is {case2} ') 
print(f'case 3 is {case3} ') 
print(f'case 4 is {case4} ') 