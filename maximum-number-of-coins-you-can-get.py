class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        max=0
        piles.sort()
        chake=[0,0,0]
        n=len(piles)-1
        x=(n+1)//3
        h=0
        for j in range (x): 
          m=0
          chake[0]=piles[n]
          n=n-1
          chake[1]=piles[n]
          n=n-1
          chake[2]=piles[m]
          m=m+1
          h=h+chake[1]
          print(chake)
        return h
        


          
        # print(piles)
        # for i in range(1,len(piles),3):
        #     max=piles[i]+max
        #     print(i)
        # return max
        # dic={"alice":0,"me":0,"bob":0}
        # for i in range(len(piles)):
        #     amax=max(piles)
        #     dic["alice"]=amax+dic["alice"]
        #     piles[piles.index(amax)]=0
        #     print(piles)
        #     mmax=max(piles)
        #     dic["me"]=mmax+dic["me"]
        #     piles[piles.index(mmax)]=0
        #     print(piles)
        #     bmax=max(piles)
        #     dic["bob"]=bmax+dic["bob"]
        #     piles[piles.index(bmax)]=0
        #     print(piles)
        # return dic["me"]