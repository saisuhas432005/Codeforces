k=[]
l=[]
m=[]
for i in range(3):
  n=input()
  k.append(n)
n=k[0]+k[1]
b=k[2]
for i in n:
  l.append(i)
for j in b:
  m.append(j)
l.sort()
m.sort()
if l==m:
  print("YES")
else:
  print("NO")