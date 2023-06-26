class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        dic={}
        for i in range (len(paths)):
           a=paths[i].split()
           for j in range (1,len(a)):
                n=a[j].split("(")
                # print(n)
                b=n[0]
                if(n[1] not in dic):
                    dic[n[1]]=[a[0]+"/"+n[0]]
                else:
                    dic[n[1]].append(a[0]+"/"+n[0])
                # print(dic)
        arr=[]
        q=0
        for key in dic:
          if(len(dic[key])>1):
            arr.append(dic[key])
            q=q+1
        return arr