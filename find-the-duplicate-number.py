class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        dic={}
        for i in range (len(nums)):
            if nums[i] in dic:
                return nums[i]
            else: 
                dic[nums[i]]=1
        return 0