class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        start=0 
        end=len(s)-1
        temp="" 
        while end>=start:
            temp=s[end]
            s[end]=s[start]
            s[start]=temp
            end =end-1 
            start=start+1