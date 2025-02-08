l=list(map(int,input().split()))

k=sum(l)
o=len(l)


if k==0:
    print("-1")
elif k%o==0:
    print(int(k/o))
else:
    print("-1")