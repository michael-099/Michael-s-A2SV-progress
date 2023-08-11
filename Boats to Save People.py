class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        start=0
        end=len(people)-1
        people.sort()
        count=0
        while end>=start:
            if people[start]+people[end]<=limit:
                count=count+1
                start=start+1
                end=end-1
            else :
                end=end-1 
                count=count+1
        return count 
                


        # boat=1
        # s=0
        # people.sort()
        # for i in range(len(people)):
        #     if s+people[i]<=limit:
        #         s=s+people[i]
        #     else:
        #         s=people[i]
        #         boat=boat+1
        # return boat
