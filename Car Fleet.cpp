class Solution {
public:
    int carFleet(int target, vector<int>& position, vector<int>& speed) {
        int n = position.size();
        vector<pair<int,int>> v(n);
        for (int i = 0; i < n; i++)
        {
            v[i] = {position[i], speed[i]};
        }
        sort(v.begin(), v.end());
        double time, x;
        int count = 1;
        time = ((target - v[n - 1].first)/(v[n - 1].second/1.0));
        for (int i = n - 2; i >= 0; i--)
        {
            x = ((target - v[i].first)/(v[i].second/1.0));
                if (x > time)
                {
                    time = x;
                    count++;
                }
            
        }
        return count;
    }
};
