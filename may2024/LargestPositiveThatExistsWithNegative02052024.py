from typing import List


class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        biggest = -1
        for num in nums: 
            if num > biggest and (num * -1) in nums and num >=0:
                biggest = num 
        return biggest


print("running script") 
case1= Solution().findMaxK(nums = [-1,2,-3,3]) 
case2= Solution().findMaxK(nums = [-1,10,6,7,-7,1]) 
case3= Solution().findMaxK(nums = [-10,8,6,7,-2,-3]) 
print(f'case 1 is {case1} ') 
print(f'case 2 is {case2} ') 
print(f'case 3 is {case3} ') 
