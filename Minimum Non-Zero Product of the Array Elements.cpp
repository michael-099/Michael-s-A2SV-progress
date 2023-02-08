class Solution {
public:
    

    typedef long long ll;
    ll big = 1e9 + 7;
    
    int minNonZeroProduct(int p) {
        if(p == 1) return 1;
        
        vector<ll> v(63, 1) ;
        for(int i=1; i<63; ++i) {
            v[i] = (v[i-1] * 2) % big;
        }
        
        ll a = v[p] - 1, b = v[p] - 2, multi = b;
        for(int i=0; i<p-2; ++i) {
            b = (b * b) % big;
            multi = (multi * b) % big;
        }
        int ans = (a * multi) % big;
        return ans;
    

        
    }
};
