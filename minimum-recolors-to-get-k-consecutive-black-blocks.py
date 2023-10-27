class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        start=0 
        end=k-1
        count=0
        res=0
        for i in range (0,k):
            if blocks[i] is "W":
                count=count+1 
            res =count
            print(count)
        while end<(len(blocks)-1):
            print(blocks[start:end+1])
            if blocks[start]=="W":
                count=count-1
            start=start+1
            end=end+1 
            if blocks[end]=="W":
                count =count+1
            res=min(res,count) 
        return res