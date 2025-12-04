import sys
input=sys.stdin.read
def main():
    ind=0
    data=input().split()
    n=int(data[ind])
    ind+=1
    m=int(data[ind])
    ind+=1
    vec=[[0]*m for _ in range(n)]
    sum_=0
    for i in range(n):
        for j in range(m):
            val=int(data[ind])
            vec[i][j]=val
            ind+=1
            sum_+=val
    
    
    horizon=[0]*n
    for i in range(n):
        for j in range(m):
            horizon[i]+=vec[i][j]
    
    vertical=[0]*m
    for j in range(m):
        for i in range(n):
            vertical[j]+=vec[i][j]
    
    res=float('inf')
    hor=ver=0
    for i in range(len(horizon)):
        hor+=horizon[i]
        res=min(res,abs(sum_-2*hor))
    for j in range(len(vertical)):
        ver+=vertical[j]
        res=min(res,abs(sum_-2*hor))

    print(res)

if __name__=="__main__":
    main()
    
