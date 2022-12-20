
class Solution
{
	int  select(int arr[], int i)
	{
        // code here such that selectionSort() sorts arr[]
        return 0;
    
	}
	
	void selectionSort(int arr[], int n)
	{
	   
	    //code here 
	    for(int i=0;i<n;i++){
	        int min_index=i;
	        for (int j=i+1;j<=n-1;j++){
	            if(arr[j]<arr[min_index]){
	                min_index=j;
	            }
	                
	            }
	            if(arr[i]!=arr[min_index]){
	                int temp;
	                temp=arr[i];
	                arr[i]=arr[min_index];
	                arr[min_index]=temp;
	            }
	        }
	    }
	}
