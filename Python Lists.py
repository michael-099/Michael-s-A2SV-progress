if __name__ == '__main__':
    N = int(input())
    # print(N)
    arr=[]
    for i in range (N):
        inpu=input()
        list1=inpu.split(" ")
        # print(list1)
        if(list1[0]=="insert"):
            arr.insert(int(list1[1]),int(list1[2]))
        if(list1[0]=="print"):
            print(arr)
            
        if(list1[0]=="remove"):
            arr.remove(int(list1[1]))
        if(list1[0]=="append"):
            arr.append(int(list1[1]))
        if(list1[0]=="sort"):
            arr.sort()
        if(list1[0]=="pop"):
            arr.pop()
        if(list1[0]=="reverse"):
            arr.reverse()
