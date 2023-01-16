#include<iostream>
using namespace std;
int domino (int row ,int col){
    int n ;
    n=(row*col)/2;
    return n;
}



int main (){
    int row ,col;
    //cout << "enter row ";
   cin >> row ;
   //cout<< "enter  column";
   cin >> col ;
  cout<< domino(row,col);
    
    

}
