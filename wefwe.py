s=int(input())
for i in range(s):
    n=list(map(int,input().split()))
    n.sort()
    print(n,end=" ")
