class Solution {
public:
    int hIndex(vector<int>& c) 
    {
        int ans=0;
        sort(c.begin(),c.end());
        for(int i=c.size()-1;i>=0;i--)
        {
            if(c[i]>=c.size()-i)
            {
                 ans++;
            }  
        }
        return ans;
    }
};
