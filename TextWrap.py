import textwrap

def wrap(string, max_width):
    x=""
    s=""
    list1=[]
    p=0
    q=max_width
    for i in range ((len(string)//max_width)+1):
        x=string[p:q]
        s=s+x+"\n"
        p=q
        q=q+max_width
        
    # w=s.split(" ")
    # w.pop()
    # print(w)
    # for i in range (len(w)):
    #      print(w[i])   
    return s

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
