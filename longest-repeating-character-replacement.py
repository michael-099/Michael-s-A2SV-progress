class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        start,end,res,max_fr=0,0,0,0
        dic={} 
        while end < len(s):
            dic[s[end]]=dic.get(s[end],0)+1 
            max_fr = max(max_fr,dic[s[end]])
            while (end-start+1)-max_fr > k:
                dic[s[start]]=dic[s[start]]-1 
                start=start+1
            end = end+1 
            res=max(res,(end-start))
        return res