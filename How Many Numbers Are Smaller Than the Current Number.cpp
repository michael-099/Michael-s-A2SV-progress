class Solution {
public:
    vector<int> smallerNumbersThanCurrent(vector<int>& nums) {
        vector<int> a;
        
        for (int i=0;i<=nums.size()-1 ;i++)
        {int count =0;
          for (int j=0;j<=nums.size()-1;j++)
          {if (nums[i]!=nums[j]&&nums[i]>nums[j])
             {
              count++;
              }
          }
           a.push_back(count);
        }
        return a;
           
      
  }};
