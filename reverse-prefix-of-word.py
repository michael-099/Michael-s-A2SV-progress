class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        start=0
        end=0
        temp=""
        while ch in word and word[end]!=ch:
            end=end+1
       
        word=list(word)
        while end>=start:
            temp=word[start]
            word[start]=word[end]
            word[end]=temp
            end=end-1
            start=start+1
        w=""
        for i in range (len(word)):
            w=w+word[i]
        return w