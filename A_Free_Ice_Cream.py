n,x=map(int,input().split())
c=0
d=0
p=0
for i in range(n):
    a,b=map(str,input().split())
    if a=="+":
        x=x+int(b)
    else:
        if x<int(b):
            c=c+1
        else:
            x=x-int(b)
print(x,c)

