class Solution {
public:
    static vector<int> pancakeSort(vector<int> arr) {
        const int n = size(arr);
        vector<int> st;

        auto add = [&] (int x) {
            if (x > 1) {
                if (!st.empty() && x == st.back())
                    st.pop_back();
                else
                    st.push_back(x);
            }
        };

        auto dew = [&] (int j, int i) {
            if (i != j) {
                add(i + 1);
                add(i - j + 1);
                add(i - j);
                add(i - j - 1);
                add(i - j);
                add(i + 1);
            }
        };

        vector<int> indices(n);
        for (int i = 0; i < n; ++i)
            indices[arr[i] - 1] = i;
        for (int i = 0; i < n; ++i) {
            int pull = indices[i];
            dew(i, pull);
            swap(indices[arr[i] - 1], indices[i]);
            swap(arr[i], arr[pull]);
        }
        return st;
    }
};
