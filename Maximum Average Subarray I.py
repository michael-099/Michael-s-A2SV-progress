class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        start=0
        end=k-1
        s=sum(nums[start:end+1])
        # print(s)
        temp=s
        while end<len(nums)-1:
            s=s-nums[start]
            s=s+nums[end+1]
            end=end+1
            start=start+1
            # print(s)
            if s>temp:
                temp=s
            # print (temp)
        average=temp/k
        return average
