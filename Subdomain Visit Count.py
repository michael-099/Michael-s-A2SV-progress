class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        dic={}
        l=[]
       
        for i in range (len(cpdomains)):
            x=""
            n=cpdomains[i].split()
            arr=n[1].split(".")
            # print(n)
            # print(arr)
            index=len(arr)-1
            # print(index)
            for i in range(index,-1,-1):
                if(i==index):
                    x=arr[i]+x
                else:
                 x=arr[i]+"."+x
                # x=x[0:len(x)-1]
                if x not in dic:
                    dic[x]=n[0]
                elif x in dic:
                    dic[x]=int(dic[x])+int(n[0])
            # print (dic)
        result = ''
        for key, value in dic.items():
         result = f'{value} {key}'
         l.append(result)
            
        return l
