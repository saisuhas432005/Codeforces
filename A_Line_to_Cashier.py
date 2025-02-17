n=int(input())
b=list(map(int,input().split()))
d=set()
for e in range(n):
    f=list(map(int,input().split()))
    g=sum(f)*5+((len(f))*15)
    d.add(g)
print(min(d))