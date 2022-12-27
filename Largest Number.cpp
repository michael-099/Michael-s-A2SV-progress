class Solution {
public:
    string largestNumber(vector<int>& nums) {
        int n =nums.size();
        string temp;
        string s;
        vector<string> v;
        // for (int i=0;i<n;i++){
        //       int min_index=i;
        //  for(int j=i;j<n;j++){
        //      if(nums[j]<nums[min_index]){
        //          min_index=j;
        //      }
        //  }
        //  if(i != min_index){
        //      temp=nums[i];
        //      nums[i]=nums[min_index];
        //      nums[min_index]=temp;

        //  }

        // }
        // for(int x:nums){
        //     cout<<x<<",";
        // }
        // for (int i=0;i<=n;i++){
        //     for(int j=0;j<=n;j++){
        //         if ()
        //     }
        // }
      for (int i = 0; i < n; i++) {
   v.push_back(to_string(nums[i]));
 }
 cout << "_" << v[0] + v[1] << "_";
 for (int j = 0; j < n; j++) {
   for (int i = 0; i < n - 1; i++) {
     if (v[i] + v[i + 1] < v[i + 1] + v[i]) {
       temp = v[i];
       v[i] = v[i + 1];
       v[i + 1] = temp;
     }

   }
 }
 for (string x: v) {
   cout << x << ",";
 }
 for (int i = 0; i < n; i++) {
  if(s=="" && v[0]=="0"){

   }
  else{s = s + v[i];}
 }
//  if(s.at(0)==0){
//      s.erase(0);
//  }
if(s!=""){
 return s;}
 else{
     return "0";
 }
    }
};
