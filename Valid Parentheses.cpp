class Solution {
public:
    bool isValid(string s) {
        stack<char> Z;
   char c;
   for (int i=0; i<s.length(); i++) {
      if (s[i]=='('||s[i]=='['||s[i]=='{') {
         Z.push(s[i]);
         continue;
      }
      if (Z.empty())
         return false;
      switch (s[i]) {
      case ')':
         c = Z.top();
         Z.pop();
         if (c=='{' || c=='[')
            return false;
         break;
      case '}':
         c = Z.top();
         Z.pop();
         if (c=='(' || c=='[')
            return false;
         break;
      case ']':
         c = Z.top();
         Z.pop();
         if (c =='(' || c == '{')
            return false;
         break;
      }
   }
   return (Z.empty());
}
        
    
};
