#User function Template for python3

class Solution: 
        # code here 
    
    def selectionSort(self, arr,n):
        for i in range (len(arr)):
            min=i
            for  j in range (i+1,len(arr)):
                if arr[j]<arr[min]:
                    min=j
            arr[min],arr[i]=arr[i],arr[min]
        return arr
            