class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        start=0 
        end=0 
        dic={}
        max_f=0
        res=0
        while end<len(answerKey):
            dic[answerKey[end]]=dic.get(answerKey[end],0)+1
            max_f=max(max_f,dic[answerKey[end]])
            while (end-start+1)-max_f>k:
                dic[answerKey[start]]-=1
                start=start+1
            end=end+1 
            
        res=max(end-start,res)
        return res