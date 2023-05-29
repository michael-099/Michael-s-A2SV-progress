class Solution:
    def reverse(self, x: int) -> int:
        y=x
        if(x<0):
            x=x*(-1)
        x=str(x)
        x=list(x)
        x.reverse()
        a=""
        for i in range (len(x)):
                a=a+x[i]
        a=int(a)
        if(y<0):
            a=a*(-1)
        if(a<-2**31  or a>(2**31)-1):
            return 0
        return a
    
