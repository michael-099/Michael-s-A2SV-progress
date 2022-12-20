class Solution {
public:
    int numIdenticalPairs(vector<int>& nums) {
     int count=0;
      for(int j=0;j<=nums.size()-1;j++){
        for(int i=0;i<=nums.size()-1;i++){
            if(nums[j]==nums[i]&&j>i){
                count++;
            }

        }}
