class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        start=0
        end=0 
        count=0
        res=0
        dic={}
        while end<=len(nums)-1:
            if nums[end]==1:
                count=count+1 
            elif nums[end]==0:
                count=count+1 
                k= k-1 
            # res=max(count,res)
            while k==-1 and end>=start:
                 if nums[start]!=0:
                   start=start+1 
                   count=count-1 
                 else :
                   k=k+1 
                   start=start +1 
                   count=count-1 
            end=end+1
            res=max(count,res)
            
        return res