class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowel={'a','e','i','o','u'}
        start =0
        end =k-1
        count=0
        res=0
        print (len(s))
        for i in range  (0,k):
            if s[i] in vowel:
                count=count+1
            res=count
            # end=end+1
            print(end)
        while end<(len(s)-1):
            if s[start] in vowel:count =count-1
            start = start +1 
            end =end +1 
            if s[end] in vowel : count =count+1 
            res=max(res,count)
            
         
        return res