class Solution {

public:
    vector<int> nextGreaterElement(vector<int>& nums1, vector<int>& nums2) {
        unordered_map<int, int> m;
        for (int i = 0; i < nums2.size(); i++) {
            int j = i + 1;
            for (; j < nums2.size(); j++) {
               
				if (nums2[j] > nums2[i]) {
                    m[nums2[i]] = nums2[j];
                    break;
                }
            }
		
            if (j == nums2.size())
                m[nums2[i]] = -1;
        }

        vector<int> res;
        for (auto n : nums1) {
            res.push_back(m[n]);
        }
        return res;
    }

};
