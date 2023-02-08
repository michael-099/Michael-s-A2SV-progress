class Pair{
    public : 
    int taskCount, availableTime; 
    Pair(int taskCount, int availableTime)
    {
        this->taskCount = taskCount;
        this->availableTime = availableTime;
    }
};
class Solution {
public:
    int leastInterval(vector<char>& tasks, int n) 
    {
        vector<int>mp(26, 0);
        for (char task : tasks) mp[task - 'A']++;
        priority_queue<int>pq; //MAX_HEAP
        for (char taskIdx = 0; taskIdx < 26; taskIdx++)
        {
            int count = mp[taskIdx];
            if (count >= 1) pq.push(count); 
        }
        
        queue<Pair>waitingQueue;
        int currTime = 1;
        while(!pq.empty() || !waitingQueue.empty())
        {
        
            while(!waitingQueue.empty())
            {
                if (waitingQueue.front().availableTime == currTime) 
                {
                    pq.push(waitingQueue.front().taskCount);
                    waitingQueue.pop();
                }
                else break;
            }
   
            if (!pq.empty())
            {
                int leftOutTaskCount = pq.top() - 1;
                pq.pop();
                if (leftOutTaskCount != 0) waitingQueue.push(Pair(leftOutTaskCount, currTime + n + 1));
            }
          
            currTime++;
        }
        return currTime - 1;
        
    }
};
