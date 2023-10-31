class Solution:
    
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # for i in range(1,len(nums)):
        #     key=nums[i]
        #     j=i-1
        #     while j>=0 and key<nums[j]:
        #         nums[j+1]=nums[j]
        #         j=j-1
        #     nums[j+1]=key
        start =0 
        end=len(nums)-1 
        middle=0
        temp=0
       
        while end>= middle:
            if nums[middle]==0:
               nums[middle],nums[start]=nums[start],nums[middle]
               start=start+1 
               middle=middle +1
            elif nums[middle]==1:
                middle=middle+1
            else:
               nums[middle],nums[end]=nums[end],nums[middle]
               end=end-1    
        return nums