n=input()
n=n.split()
n=[int(x) for x in n]
arr=input()
arr=arr.split()
arr=[int(x) for x in arr]
arr.sort()
num=0
if n[1] == 0: 
  if arr[0]>1 :
      print(arr[0]-1)
  else :
      print(-1)
elif n[1] == n[0]:
    print(arr[n[0]-1])
elif arr[n[1]-1] == arr[n[1]]:
    print(-1)
else:
    print(arr[n[1]-1])
# if n[1]==0:
#       num=arr[0]-1
# elif n[1]==len(arr) or arr[n[1]-1]==arr[n[1]] :
#        num=-1
# else:
#       num=arr[n[1]-1]

# print(num) 



