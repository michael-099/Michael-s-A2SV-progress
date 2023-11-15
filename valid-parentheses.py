class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        dic={"}":"{",")":"(","]":"["}
        for i in range(len(s)):
            if(s[i]=="(" or s[i]=="{" or s[i]=="["):
                stack.append(s[i])
            elif(s[i]==")" or s[i]=="}" or s[i]=="]"):
                if(len(stack)==0  or dic[s[i]]!=stack[-1] ) :return False 
                elif(dic[s[i]]==stack[-1]):
                    stack.pop()
                  
                
        return True if len(stack)==0 else False