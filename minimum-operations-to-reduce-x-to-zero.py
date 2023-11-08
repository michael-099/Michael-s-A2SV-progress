class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        Sum=sum(nums)
        target =Sum-x
        if target<0:return -1 
        start,end,s,res=0,0,0,float("inf")
        while end < len(nums):
            s=s+nums[end]
            while s>target:
                s=s-nums[start]
                start=start+1 
            if s==target:
                res=min(res,(len(nums)-(end-start+1)))
            end=end+1 
        return -1 if res==float("inf") else res