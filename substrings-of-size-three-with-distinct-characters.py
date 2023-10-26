class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        start =0
        end=2 
        count=0
        while end<=len(s)-1:
            if s[start]!=s[start+1]and s[start]!=s[end] and s[start+1]!=s[end]:
                count=count +1 
                print (s[start:end+1])
            start=start+1 
            end =end+1 

        return count