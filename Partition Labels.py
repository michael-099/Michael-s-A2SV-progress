class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        dic={}
        for i in range(len(s)):
            if s[i] in dic:
                dic[s[i]]=i
            else :
                dic[s[i]]=i
        start=0
        end=dic[s[0]]
        arr=[]
        for j in range(len(s)): 
            start=start+1
            if(dic[s[j]]>end):
                end=dic[s[j]]
            if(j==end):
                arr.append(start)
                start=0
            
        return arr
