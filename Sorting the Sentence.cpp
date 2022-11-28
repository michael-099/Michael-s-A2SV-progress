#include <string>
class Solution {
 public:
  string sortSentence(string s) {
    int count = 0;
    string sentence;
    vector<string> v;
    vector<string> x;
    string final ;
    for(int  k:s) {
      if(k==' '){
         count++;
        }
    }
    s = s + " ";
    for (int i = 0; i < s.length(); i++) {
      if (s.at(i) != ' ') {
        sentence = sentence + s.at(i);
      } else {
        v.push_back(sentence);
        sentence.erase();
      }
    } string temp;
      for(int j=0;j<v.size()-1;j++){
      for(int i=0;i<v.size()-1;i++){
        int n1= v[i].length()-1;
            int n2=v[i+1].length()-1;
          if(((int)(v[i].at(n1)))> ((int)(v[i+1].at(n2)))){
              temp=v[i];
              v[i]=v[i+1];
              v[i+1]=temp;
      }}}
      for(int i=0;i<v.size();i++){
          final = final+v[i].substr(0,v[i].length()-1)+" ";}
          final=final.substr(0,final.length()-1);
      
     

     return final;
}
}
;








 // for(int i=0;i<=v.size();i++){
      // int n=v[i].length()-1;
      // int r= (int)v[i].at(n);
      //     cout<<r;
      // }
//   } string temp;
//       for(int i=0;i<v.size();i++){
         
//           if((int)v[i].at(v[i].length()-1)> (int)v[i+1].at(v[i+1].length()-1)){
//               temp=v[i];
//               v[i]=v[i+1];
//               v[i+1]=temp;
//       }}
//       for(auto i:v){
//           cout<<i;
//       }



//int p=v.size();
  //      vector<string> x(p,0)
  // for(int i=0;i<v.size();i++){
  //     int n=v[i].length()-1;
  //     int r= (int)v[i].at(n);
  //     x[r-1]=v[i];






// for (string  i:v){
        //     cout<< i<<"    ";
        // }
       
