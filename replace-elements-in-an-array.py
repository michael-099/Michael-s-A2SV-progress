class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        d={}
        for i,value in enumerate(nums):
            d[value]=i
        for f,s in operations:
            nums[d[f]]=s
            temp = d[f] 
            nums[temp] = s 
            del d[f]   
            d[s] = temp 
        return nums
            

        
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
        # dic={}
        # print(len(operations))
        # e=sys.getsizeof(dic)
        # # print(f'e= {e}')
        # for i in range (len(operations)):
        #     # print(len(operations))
        #     dic[operations[i][0]]=operations[i][1]
        #     # print(dic)
        # print(len(dic))
        # for i in range (len(operations)):
        #     if operations[i][0] in nums:
        #         x=nums.index(operations[i][0])
        #         nums[x]=operations[i][1]
        # return nums