class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        start=0
        count=1
        res=0
        v_set=set(word[0])
        for end in range(1,len(word)):
            if word[end]>=word[end-1]:
                v_set.add(word[end])
                count=count+1
            else:
                v_set=set(word[end])
                count=count=1         
            if len(v_set)==5:
                  res=max(count,res)
        return res