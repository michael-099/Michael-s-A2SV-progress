stack<int> s;
    
    int i=0,j=0;
    int n=pushed.size();
    while(i<n)
    {
        if(pushed[i]!=popped[j]){
            s.push(pushed[i]);
        }
        else{
            j++;
            while(!s.empty() && popped[j]==s.top())  //checking if their is a number in stack which can be popped and continue popping until it can be popped :)
            {
                s.pop();
                j++;
            }
        }
        
        i++;
    }
    
    while(!s.empty())
    {
        if(s.top()!=popped[j]) //check the remaining if they match the popped sequence which is given
            return false;
        else{
            s.pop();
            j++;
        }
    }
    
    
    return true;
