class Solution:
    def isPalindrome(self, s: str) -> bool:
        list1=[]
        for i in range (len(s)):
            if s[i].isalpha() or s[i].isdigit():
                list1.append(s[i].lower())
        list2=list1.copy()
        list1.reverse()
        if list1==list2:
            return True
        else :return False 
