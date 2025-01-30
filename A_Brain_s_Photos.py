n, m = map(int, input().split())
# p = [input().split() for _ in range(n)]
# c = False
# for i in p:
#     for j in i:
#         if j in ['C', 'M', 'Y']:
#             c = True
#             break
#     if c:
#         break

# if c:
#     print("#Color")
# else:
#     print("#Black&White")
l=[]
for i in range(n):
    l1=list(map(str,input().split()))
    for i in l1:
        l.append(i)
o=set(l)
c=0
for i in o:
    if i=="B" or i=="W" or i=="G":
        c=c+1
    else:
        c=c+3
if c==len(o):
    print("#Black&White")
else:
    print("#Color")
    