class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dct={}
        for i in range (len(nums)):
            x=target-nums[i]
            print(x)
            if(nums[i] in dct):
                 j=nums[i]
                 return(i,dct[j])
            if(nums[i] not in dct):
                 dct[x]=i
               
     
           
