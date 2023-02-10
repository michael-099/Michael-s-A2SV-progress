class Solution
{
public:
    unordered_map<int, int> dp;
    
    int f(vector<int>& nums, int l, int r)
    {
        const int key = l + r * 100;
        
        if(!dp.count(key))
        {
            if(l == r)
                dp[key] = nums[l];
            else
                dp[key] = max(nums[l] - f(nums, l + 1, r), nums[r] - f(nums, l, r - 1));
        }
        
        return dp[key];
    }
    
    bool PredictTheWinner(vector<int>& nums)
    {
        return f(nums, 0, nums.size() - 1) >= 0;
    }};
