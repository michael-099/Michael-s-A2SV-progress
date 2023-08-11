class Solution:
    def maxArea(self, height: List[int]) -> int:
        start =0 
        end=len(height)-1
        area=0
        while end>=start:
            a=(end-start)*min(height[start],height[end])
            if height[end]<height[start]:
                end=end-1
            elif height[end]>=height[start]:
                start=start+1
            if a>area:
                area=a
        return area
