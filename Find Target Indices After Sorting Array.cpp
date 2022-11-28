class Solution {
 public:
  vector<int> targetIndices(vector<int>& nums, int target) {
    int temp = 0;
    vector<int> v;
      for (int i = 0; i < nums.size()-1; i++) {
      for (int j = 0; j <nums.size()-1; j++) {
        if (nums[j] > nums[j + 1]) {
          temp = nums[j];
          nums[j] = nums[j + 1];
          nums[j + 1] = temp;
        }
      }
    }
   for (int i = 0; i < nums.size(); i++) {
      if (nums[i] == target) {
        v.push_back(i);
      }
    }
    return v;
  }
};
