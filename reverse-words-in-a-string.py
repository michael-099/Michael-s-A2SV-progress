class Solution:
    def reverseWords(self, s: str) -> str:
        
        s=s.split()
        start=0
        # print(s)
        end=len(s)-1 
        temp=""
        while end>=start:
            temp=s[end]
            s[end]=s[start]
            s[start]=temp
            start=start+1 
            end=end-1
        st=""

        for i in range (len(s)):
            st=st+" "+s[i]
        return st[1:len(st)]