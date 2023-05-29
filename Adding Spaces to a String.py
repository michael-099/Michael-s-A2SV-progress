class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        x=""
        p=0
        for i in range (len(spaces)):
            q=spaces[i]
            y=s[p:q]
            x=x+y+" "
            p=q
            # q=spaces[0]
        y=s[p:len(s)]
        x=x+y   
           
          
        return x
