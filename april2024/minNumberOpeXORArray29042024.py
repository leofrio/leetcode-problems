from functools import reduce
from operator import xor
import time
from typing import List


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        return (reduce(xor, nums)^k).bit_count()
                


    # def padBinaryListAndK(self,bList:List[str],bK:str): 
    #     largestLen= len(max(bList,key=len)) 

    #     return [b.rjust(largestLen,'0') for b in bList],bK.rjust(largestLen,'0'),largestLen
        
    # def findXorResult(self,bArr:List[str],largestLen:int) -> int:  
    #     decList=[int(bNum,2) for bNum in bArr]
    #     binaryResult =None 
    #     prevNum=None
    #     for num in decList:  
    #         if prevNum != None: 
    #             binaryResult= prevNum^num  
    #         prevNum=binaryResult if binaryResult != None else num  
    #     return bin(binaryResult)[2:].rjust(largestLen,'0')
    # def flipBinaryNum(self,bNum:str,pos:int)-> str: 
    #     invertedNum='0' if bNum[pos] == '1' else '1' 
        return bNum[:pos] + invertedNum + bNum[pos+1:]  




         
        


        


         

print("running script") 
case1= Solution().minOperations(nums = [2,1,3,4], k = 1) 
case2= Solution().minOperations(nums = [2,0,2,0], k = 0)  
print(f'case 1 is {case1} ')
print(f'case 2 is {case2} ') 

