n=int(input())
l=list(map(int,input().split()))

l.sort()
o=0
mi=min(l)
ma=max(l)
if len(l)<=2:
    print(0)
else:
    for i in range(1,len(l)-1):
        if l[i]<ma and l[i]>mi:
            o=o+1
    print(o)
        