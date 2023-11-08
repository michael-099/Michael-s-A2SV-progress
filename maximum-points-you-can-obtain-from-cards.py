class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        start,res,count =0,0,0
        end=len(cardPoints)-k-1
        Sum=sum(cardPoints)
        window_sum=sum(cardPoints[start:end+1])
        count=Sum-window_sum
        res=max(res,count)
        for end in range(len(cardPoints)-k,len(cardPoints)):
            window_sum=window_sum - cardPoints[start]
            start=start+1 
            window_sum=window_sum+cardPoints[end]
            count=Sum-window_sum
            res=max(count,res)
        return res