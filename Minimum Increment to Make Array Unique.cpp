const int N = 2e5 + 5;
class Solution {
public:
    int minIncrementForUnique(vector<int>& nums) {

        vector<int> mp(N, 0);

        for (auto i : nums)mp[i]++;

        int moves = 0;

        for (int i = 0 ; i < N  ; i++) {

            if (mp[i] <= 1)continue;

            mp[i + 1] += (mp[i] - 1);
            moves += (mp[i] - 1);
        }

        return moves;
    }
};
