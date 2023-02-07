class Solution {
public:
    int minPairSum(vector<int>& nums) {
        sort(nums.begin(),nums.end());
        int n=nums.size()-1;
        int maxi=INT_MIN;
        for(int i=0;i<nums.size()/2;i++,n--){
            maxi=max(maxi,nums[i]+nums[n]);
        }
        return maxi;
    }
