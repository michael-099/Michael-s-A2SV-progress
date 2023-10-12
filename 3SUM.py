class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        arr=[]
        for i in range (len(nums)-2):
            if i > 0 and nums[i]==nums[i-1]:
                continue

            start =i+1
            end =len(nums)-1
            while start<end:
                threesum=nums[i]+nums[start]+nums[end]
                if  threesum >0:
                    end =end-1
                elif threesum<0:
                    start=start+1
                elif threesum==0:
                    #  if [nums[i],nums[end],nums[start]] not in arr:
                     arr.append([nums[i],nums[start],nums[end]])  
                     while end>start and  nums[start+1]==nums[start]:
                         start =start+1 
                     while end>start and nums[end]==nums[end-1] :
                         end =end -1 
                     start += 1
                     end -= 1
                    
        return arr    
