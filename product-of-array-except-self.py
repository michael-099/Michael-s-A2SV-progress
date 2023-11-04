class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix =[1]*(len(nums)+2)
        postfix=[1]*(len(nums)+2)
        output=[1]*(len(nums)+2 )
        for i in range(1,len(nums)+1):
            prefix[i]=nums[i-1]*prefix[i-1]
        # print(prefix)
        for i in range(len(nums)-1,-1,-1):
            postfix[i+1]=postfix[i+2]*nums[i]
        # print(postfix)
        for i in range (1,len(nums)+1):
            output[i]=prefix[i-1]*postfix[i+1]
        # print(output)
        return output[1:len(output)-1]