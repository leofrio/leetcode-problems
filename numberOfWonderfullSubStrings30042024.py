from typing import List


class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        subStringDic={} 
        count=0
        subStrings=self.getAllSubstrings(word) 
        for substring in subStrings: 
            subStringDic[substring] ={}  
            if len(substring) > 1: 
                for char in substring: 
                    if char not in subStringDic[substring]: 
                        subStringDic[substring][char]=1
                    else: 
                        subStringDic[substring][char] +=1  
                if len(subStringDic[substring]) > 1: 
                    oddAmount= len([value for value in subStringDic[substring].values() if value %2 != 0]) 
                    if oddAmount == 1 or oddAmount == 0: 
                        count += 1   
                else: 
                    count += 1

            else: 
                count += 1    
        return count            

        # char_count={} 
        # for char in word: 
        #     if char not in char_count: 
        #         char_count[char]  =1 
        #     else: 
        #         char_count[char] += 1

    def getAllSubstrings(self,word:str)-> List[str]: 
        return [word[i: j] for i in range(len(word)) for j in range(i + 1, len(word) + 1)] 


case1 = Solution().wonderfulSubstrings(word = "aba")
case2 = Solution().wonderfulSubstrings(word = "aabb")
case3 = Solution().wonderfulSubstrings(word = "he")
case4 = Solution().wonderfulSubstrings(word = "ghffghcdigdgbfhaiejibbcidgfjahegedjecfhdjchdcaefeefiabebefjccdhdchacehfdjibcgcedjhhbadfgejhceghgjjegihhbfagciecdadhcjgdajgbhegjhicbifeefcaficcbcijciegihidacjahahjgdjdgfjcadgaiicgiiegaeifjbcjacefffgdgibjfijiiedcaahbceebheifbgffchdcfbbhfdfajggfhhhbhhgbcgfdgcfcdggihhcfcghbgbchcgaccccaabeejdhdbjicghddaaeedciigeeiehjhhhicajbddedidecjiebbggdehbgejabcbcjadicjgbabehbjjbehfegicabighbcahijjdcgehjhcbfheecgjdfbhadgbhfdefffbcbggifgdhdgahgejeegbadbifjdiaggdcjfaiigdjjehebjdabgdecfcebcfggceihffhjcjfaadhgeahiajjdghehieiidcfdjaeiehcjghjcajhgdhcfjcagiibhdiiabghcffaijehjjjiafjcgfjeghdbggbhfjdihahjedgdhhdibcdgaaafejgbdjgdfichbijjajicdfehafjbgdbieaecagdifeggbefegeajejbcfaidjbgbbgejjebidcdaeggcefjdfacachfeehajfabfhbcdjbcjdifiehdjghdhegfgababaeacdjcegffgdhadjehiebggdiececeiihfghcecahbhgefhihahhfhgdeaejgdhihcgfecgecebdjgcjicjdbcicigdbaehhjcdajbehdeahbibeejddajiacgchbcffagbbdiechcfgafehifibifhaidaeidjbeefefcaiejdhibebghbjgbbhchfjeefdfgjiijbbbgchgjhaefdgejfgeegbajgbcjejahgchfhjbgiiggjiaigiibccidcjcgbabed")

print(f'case 1 is {case1} ') 
print(f'case 2 is {case2} ') 
print(f'case 3 is {case3} ') 
print(f'case 3 is {case4} ') 

