class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        start=0
        end=(2*k)
        n=len(nums)
        d=(end+1)-start
        arr=[-1]*n
        c=k
        if (end>=n):
            return arr
        s=sum(nums[start:end+1])
        avg=s//d
        end = end +1 
        arr[c]=avg
        while end<=n-1:
            c=c+1
            s=s-nums[start]
            start=start+1
            s=s+nums[end]
            avg=s//d
            end=end+1
            arr[c]=avg
        return arr
        
        
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
        # n=len(nums)-1
        # start=0
        # arr=[]
        # i=0
        # for i in range (len(nums)-1):
        #     if i>=k and i+k<=n:
        #         s=sum(nums[start:i+k+1])
        #         print(len(nums[start:(2*k)+1]))
        #         if s >0:
        #             avg=s//((2*k)+1)
        #         else : avg=s
        #         # print(avg)

        #         print("hello")
        #         arr.append(avg)
        #         while i>=k and i+k<=n:
        #             # print("hello")
        #             print(nums[i])
        #             s=s-start
        #             start=start+1
        #             s=s+(i+k+1)
        #             if s >0:
        #                avg=s//((2*k)+1)
        #             else : 
        #                 avg=s
        #             arr.append(avg)
        #             i = i + 1
        #             # print(i)
        #     else:
        #         arr.append(-1)
        # return arr 




        
