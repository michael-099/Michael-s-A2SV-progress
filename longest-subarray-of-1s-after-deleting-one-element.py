class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        start=0
        end=0
        k=1 
        count =0
        res=0
        while len(nums)>end:
            if nums[end]==1:
                count=count+1
            elif nums[end]==0 and k==1:
                k=k-1 
            elif nums[end]==0 and k==0:
                while nums[start]!=0:
                    start=start+1
                    count=count -1 
                start=start+1
            end=end+1 
            res=max(count,res)
        return res if k==0 else res-1