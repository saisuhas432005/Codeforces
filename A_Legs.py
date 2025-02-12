l=int(input())
for i in range(l):
    k=int(input())
    p=k%4
    if p==0:
        print(k//4)
    else:
        print(k//4+1)