class Solution {
public:
  vector<int> findOriginalArray(vector<int>& changed) {
        
        vector<int> ans;
        
        map<int,int> m;
        for(auto i:changed)
           m[i]++;
        
        for(auto i:m)
        {
            if(i.first==0)
            {
                if(i.second%2)
                    return {};
                
                for(int k=0;k<i.second/2;k++)
                    ans.push_back(0);
            }
            else if(i.second!=0)
            {
                int a=i.first;
                int b=2*i.first;
                
                if(m[a]>m[b]) 
                    return {};
                
                for(int k=0;k<m[a];k++)
                    ans.push_back(a);
                

                m[a]=m[b]-=m[a];  
            }
        }
        return ans;
    }
