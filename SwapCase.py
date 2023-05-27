def swap_case(s):
 x=""
 for i in range (len(s)):
   if(s[i].islower()):
        x=x+(s[i].upper())
        # print("x="+x)
   elif(s[i].isupper):
        x=x+(s[i].lower())
   else:
        x=x+s[i]
 return x
if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
