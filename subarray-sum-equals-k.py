class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dic={0:1}
        count=0
        Sum=0
        for i in nums:
            Sum=Sum+i
            if Sum-k in dic:
                #  dic[Sum-k]= dic[Sum-k]-1
                 count=count+dic[Sum-k]
            dic[Sum]=dic.get(Sum,0)+1
        return count