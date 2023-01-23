class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int tracer =0;
        int j=0;
        while (j<nums.size()){
            if(nums[j]!=0){
                swap(nums[j],nums[tracer]);
                tracer++;

            }
            j++;
        }
   
    //    int  pointer=0;
    //    int temp; 
    //    for(int j=0;j<nums.size()-1;j++){
    //      for(int i=0;i<nums.size()-1;i++){
    //          if(nums[i]==0 ){
    //           temp=nums[i+1];
    //           nums[i+1]=nums[i];
    //           nums[i]=temp;
    //          // pointer--;
    //          }
    //      }}
    }
