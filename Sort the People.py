class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        for i in range (len(heights)):
            j=i
            for j in range(len(heights)):
                if(heights[i]>heights[j]):
                    temp=heights[i]
                    heights[i]=heights[j]
                    heights[j]=temp
                    temp=names[i]
                    names[i]=names[j]
                    names[j]=temp
        return names
