import sys
input=sys.stdin.read

def main():
    ind=0
    data=input().split()
    n=int(data[ind])
    ind+=1
    vec=[]
    for i in range(ind,ind+n):
        vec.append(int(data[i]))
    ind+=n
    pre=[]
    pre_sum=0
    for i in range(len(vec)):
        pre_sum+=vec[i]
        pre.append(pre_sum)
    # print(vec)
    # print(pre)
    res=[]
    while ind<len(data):
        l=int(data[ind])
        r=int(data[ind+1])
        if l==0:
            res.append(pre[r])
        else:
            res.append(pre[r]-pre[l-1])
        ind+=2
    
    for r in res:
        print(r)

if __name__=="__main__":
    main()
