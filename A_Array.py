n=int(input())
l=list(map(int,input().split()))

p=[]
n=[]
z=[]

for i in l:
    if i<0:
        n.append(i)
    elif i>0:
        p.append(i)
    else:
        z.append(i)
        
if len(n)%2==0:
    z.append(n.pop())
if len(p) == 0:
    p.append(n.pop())
    p.append(n.pop())
    
print(len(n),*n)
print(len(p),*p)
print(len(z),*z)

