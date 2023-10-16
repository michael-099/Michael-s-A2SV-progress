class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
      a,b={},{}
      if (len(s1)>len(s2)):
          return False
      for i in "abcdefghijklmnopqrstuvwxyz":
          a[i]=0
          b[i]=0
      for i in range (len(s1)):
          a[s1[i]]=a[s1[i]]+1
      start=0
      end=len(s1)-1
      for i in range (len(s1)):
          b[s2[i]]=b[s2[i]]+1
      print (a)    
      print (b)
      if a==b:
          return True 
      while end<len(s2)-1:
          b[s2[start]]-=1
          start=start+1
          end=end+1
          b[s2[end]]+=1
          if a==b:
              return True 
      return False 
          
