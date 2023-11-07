class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        start,s=0,0
        res=float("inf")
        for end in range(len(nums)):
            s=s+nums[end]
            while s>=target:
                res=min(res,end-start+1)
                s=s-nums[start]
                start=start+1    
        return 0 if res==float("inf") else res