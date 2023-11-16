class NumArray:

    def __init__(self, nums: List[int]):
      self.prefix=[0]*(len(nums)+2)
      for i in range(len(nums)):
          self.prefix[i+1]=self.prefix[i]+nums[i]
      print(prefix)
     

        

    def sumRange(self, left: int, right: int) -> int:
        right_s=self.prefix[right+1]
        left_s=self.prefix[left]
        return right_s-left_s


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)