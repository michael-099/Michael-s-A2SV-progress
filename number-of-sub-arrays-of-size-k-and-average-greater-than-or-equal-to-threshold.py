class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        start= 0
        end =k-1 
        count=0 
        s=0
        for i in range (k):
            s=s+arr[i]
        if (s/k>=threshold):
            count=count+1 
        while len(arr)-1>end:
            end=end+1 
            s=s-arr[start]
            s=s+arr[end]
            start=start+1
            if (s/k>=threshold):
              count=count+1 
        return count