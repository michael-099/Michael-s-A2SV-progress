n=input()
for i in range(int(n)):
    no=input()
    a=input().split()
    a=[int(x) for x in a]
   
    a.sort()
    for j in range (0,len(a)):
        for i in range(j+1,len(a)):
         if a[i]-a[j]==0 or a[i]-a[j]==1:
            a[j]=0
            # print(a)
    for i in range (0,len(a)-1): 
        if 0 in a:a.pop(a.index(0))
    # print(a)
    if(len(a)==1):
        print("YES")
    else:print("NO")
