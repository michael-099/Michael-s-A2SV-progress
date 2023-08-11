lass Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p=len(nums)
        q=p-k
        k=k%p
        nums.reverse()
        # nums[0:k:-1]
        # nums[k:p:-1]
        nums[0:k]=reversed(nums[0:k])
        # print(nums)
        nums[k:p]=reversed(nums[k:p])
