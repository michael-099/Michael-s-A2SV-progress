class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        length=len(arr)
        maxx=0
        out=[]
        
        for l in range (1,length):
          maxx= arr[:length].index(max(arr[:length]))
          out.append(maxx+1)
          j=0
          while j<=maxx:
              arr[j],arr[maxx]=arr[maxx],arr[j]
              j=j+1
              maxx=maxx-1  
          print(arr)
          arr[0:length]=arr[0:length][::-1]
          out.append(length)
          print(arr)
          length=length-1
        return out