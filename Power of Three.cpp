class Solution {
public:
    double x=3;
    bool isPowerOfThree(int n) {;
       
        if(x==n){
            return true ;
        }
       if(n==1){
            return true ;
        }
         if(x>n){
            return false ;
        }
        else{
          x=x*3  ;
           return isPowerOfThree(n);
        }
        return false;
        
    }
};
