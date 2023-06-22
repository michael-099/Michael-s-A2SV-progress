class Solution {
public:
    void sortColors(vector<int>& nums) {
//  int max =0;
//         for(int i =0 ;i<=nums.size();i++ ){
//             if(nums[i]>nums[i+1]){
//                 max =nums[i];            }
//         }
//         vector<int> x(max,0); 
//             for (int i=0;i<=nums.size();i++){
//        for(int j=0;j<=max;j++){
//            if (nums[i]==j){
//                x[j]=x[j]+1;
               
//            }
//            else{ x[j]=x[j];}
           
           
//        }
//     }  
//         for(int k  : x){
//             cout << x[k];
//         }
         int l=0,mid=0,r=nums.size()-1;
        while(mid<=r)
        {
            if(nums[mid]==1) mid++;
            else if(nums[mid]==0) 
            {
                swap(nums[mid],nums[l]);
                l++;mid++;
            }
            else 
            {
                swap(nums[mid],nums[r]);
                r--;           
            } 
        }

    }
};
