class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if(len(s)<len(p)):return []
        dic_s={}
        dic_p={}
        output=[]
        letters="abcdefghijklmnopqrstuvwxyz"
        
        for i in range (len(letters)):
            dic_s[letters[i]]=0
            dic_p[letters[i]]=0
        start=0
        end=0
        for i in range (len(p)):
            dic_p[p[i]]=dic_p[p[i]]+1 
            dic_s[s[i]]=dic_s[s[i]]+1 
            end=end+1 
        if(dic_s==dic_p):
            output.append(start)
        while len(s)>end:
            dic_s[s[start]]= dic_s[s[start]]-1
            start=start+1 
            dic_s[s[end]]=dic_s[s[end]]+1
            end=end +1 
            if(dic_s==dic_p):
                output.append(start)
        return output