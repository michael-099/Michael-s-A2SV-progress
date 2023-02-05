class Solution {
public:
    vector<int> rearrangeArray(vector<int>& nums) {
        int x= 0, y = 1;
        for(int i=2;i<nums.size();i++){
            if((nums[i]<nums[y] && nums[y]<nums[x])||
(nums[i]>nums[y] && nums[y]>nums[x])){
                int temp=nums[y];
                nums[y]=nums[i];
                nums[i]=temp;
            }
                
                y++;
                x++;
        }
        return nums;
    }
};
