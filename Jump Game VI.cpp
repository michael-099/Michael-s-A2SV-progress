class Solution {
public:
    int maxResult(vector<int>& A, int k) {
        int n = A.size();
        deque<int> q{n-1};
        for(int i = n - 2; i >= 0; i--) {
            A[i] += A[q.front()];
            if(q.front() == i + k) q.pop_front(); 
            while(!q.empty() && A[q.back()] <= A[i]) q.pop_back();
            q.push_back(i);
        }
        return A[0];
    }
};
