class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        x=-1
        for i in range (len(nums)):
            if(i!=nums[i]):
                x=i
                return x
        return i+1
        
