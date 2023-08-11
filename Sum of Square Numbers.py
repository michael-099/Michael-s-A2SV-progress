class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        start=0
        end=int(c**0.5)
        while end>=start:
            x=end**2+start**2
            if x>c:
                end=end-1
            elif x<c:
                start=start+1
            else:
                return True 
        return False
