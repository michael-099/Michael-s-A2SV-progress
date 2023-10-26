class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        #we want a maximum consicative subarrays which have only two numbers  
        # i have to keep track of the not actually indexes but the count of the         frequency  since i need  it when shrinking the window but how can i know if the sliding window have more elements than we need using the dictionary  
        start=0 
        end=0
        dic={}
        count=0
        while end<len(fruits):
            # dic[fruits[end]]=1 if fruits[end] not in dic else dic[fruits[end]]+=1
            if fruits[end] not in dic: 
                dic[fruits[end]]=1 
            else: 
                dic[fruits[end]]= dic[fruits[end]]+1
            end=end+1 
            while len(dic)>2:
                if dic[fruits[start]]>0:
                    dic[fruits[start]]-=1
                if dic[fruits[start]]==0:
                    del(dic[fruits[start]])
                start =start+1
            count=max(count,end-start) 
        return count