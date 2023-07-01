class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        count=[]
        for i in  range (len(nums)):
            x=0
            for j in range(len(nums)):
                if nums[i]>nums[j]:
                 x=x+1
            count.append(x)
        return count