class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        output=[0]*(n+2)
        for i in range (len(bookings)):
            output[bookings[i][0]]=output[bookings[i][0]]+bookings[i][2]
            output[bookings[i][1]+1]=output[bookings[i][1]+1]-bookings[i][2]
        for i in range (1,len(output)):
            output[i]=output[i]+output[i-1]
        return output[1:len(output)-1]