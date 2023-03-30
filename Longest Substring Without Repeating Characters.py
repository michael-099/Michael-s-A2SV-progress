class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        p=0
        q=0
        max=0
        Set= set([])
        for q in range (len(s)):
            while s[q] in Set:
                Set.remove(s[p])
                p=p+1
            Set.add(s[q])
            q=q+1
            if(q-p+1)>max:
                max =(q-p)
            
        return max 
