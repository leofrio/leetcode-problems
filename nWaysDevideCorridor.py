class Solution:
    def numberOfWays(self, corridor: str) -> int:
        print('-------------')
        n=len(corridor)  
        amtDeviders=0 
        amtOfS=0
        for space in corridor: 
            if space == 'S': 
                amtOfS += 1  
            if amtOfS >= 2: 
                

case1 = Solution().numberOfWays('SSPPSPS')
case2 = Solution().numberOfWays('PPSPSP')
case3 = Solution().numberOfWays('S')
print(f'case 1 is {case1} ')
print(f'case 2 is {case2} ')
print(f'case 3 is {case3} ')
