l=list(map(int,input().split()))
k=input()
s=0
for i in k:
    s=s+l[int(i)-1]
print(s)

