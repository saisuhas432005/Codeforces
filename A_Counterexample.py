l,r=map(int,input().split())
if l%2: 
    l+=1
if l+2>r: 
    print(-1)
else: 
    print(l,l+1,l+2)