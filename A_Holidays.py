n=int(input())
w=n//7
m=w*2
j=n%7
if j==0:
    print(m,m)
elif j==1:
    print(m,m+1)
elif j==2 or j==3 or j==4 or j==5:
    print(m,m+2)
else:
    m=m+1
    print(m,m+1)
