class Solution {
  public:
  
    char findKthBit(int n, int k) {
      vector<int> lens(n+1);
      lens[1] = 1;
      for (int i = 2; i <= n; i++)
        lens[i] = lens[i-1]*2 + 1;
      return helper(n, k, lens);
    }
  private:
    char helper(int n, int k, vector<int>& lens) {
      if (n == 1)
        return '0';
      if (k == lens[n-1]+1)
        return '1';
      char v = helper(n-1, k > lens[n-1]+1 ? 2*lens[n-1]+2 - k : k, lens);
      if (k > lens[n-1]+1)
        return v == '0' ? '1' : '0';
      return v;
    }
};
