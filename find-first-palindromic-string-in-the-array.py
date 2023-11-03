class Solution:
    def chake (self,st:str)->bool:
            if len(st)==1:return True 
            start=0
            end=len(st)-1
            while end>=start:
              
               if(st[start]!=st[end]):
                   return False 
               end=end-1
               start=start+1
            return True 


    def firstPalindrome(self, words: List[str]) -> str:
        for i in range (len(words)):
           if self.chake(words[i]):
               return words[i]
        return ""