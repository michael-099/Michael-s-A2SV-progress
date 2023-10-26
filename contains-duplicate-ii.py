class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dic={}
        for i in range(len(nums)):
            # print(nums[i])
            if nums[i] in dic :
                # print(i)
                if (abs(i-dic[nums[i]]))<=k:
                    
                    # print("hello")
                    return True
                dic[nums[i]]=i
                # print(abs( i-dic[nums[i]]))
            elif nums[i] not in dic:
                dic[nums[i]]=i
            # print(dic)
        return False