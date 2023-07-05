class MyQueue {
public:
    stack <int> one ;
        stack <int> two;
        int count =0;
       int a,b,c,o,x,y;
    MyQueue() {  
       
    }
    
    void push(int x) {
        one.push(x);
        count++;
        
    }
    
    int pop() {
        for(int i=0 ;i<count ;i++){
            a = one.top();
                one.pop();
            two.push(a);
        }
        c=two.top();
         two.pop();
        count --;
        for(int i=0;i<count;i++){
            b=two.top();
                two.pop();
          //  cout<<b;
            one.push(b);
        }
        
        return c;
        
    }
    
    int peek() {
           
           for (int j=0;j<count;j++){
             o=one.top();
              one.pop();
             two.push(o);
               x=two.top();
         }
        for (int k=0;k<=count-1;k++){
            y=two.top();
            two.pop();
            one.push(y);
        }
              
         return x;
  
    }
    
    bool empty() {return one.empty();
        
        
    }
};

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue* obj = new MyQueue();
 * obj->push(x);
 * int param_2 = obj->pop();
 * int param_3 = obj->peek();
 * bool param_4 = obj->empty();
 */
