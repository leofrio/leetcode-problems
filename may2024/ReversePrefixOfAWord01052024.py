from typing import List


class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        wIndex=word.find(ch) 
        return word[:wIndex+1][::-1] +word[wIndex+1:] 


print("running script") 
case1= Solution().reversePrefix(word = "abcdefd", ch = "d") 
case2= Solution().reversePrefix(word = "xyxzxe", ch = "z") 
case3= Solution().reversePrefix(word = "abcd", ch = "z") 
print(f'case 1 is {case1} ') 
print(f'case 2 is {case2} ') 
print(f'case 3 is {case3} ') 
