class Solution:
    def maxScore(self, nums: List[int]) -> int:
        output=[0]*(len(nums)+2)
        nums.sort()
        count=0
        nums.reverse()
        for i in range (len(nums)):
            output[i+1]=nums[i]
        for i in range (1,len(output)):
            output[i]=output[i]+output[i-1]
        for i in range(1,len(output)-1):
            if output[i]>0:
                count=count +1 
        return count