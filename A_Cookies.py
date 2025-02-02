# n = int(input())
# a = list(map(int, input().split()))
# s = sum(a)
# y = 0
# for i in range(n):
#     x = s - a[i]
#     if x % 2 == 0:
#         y += 1
# print(y)

n=int(input())

l=list(map(int,input().split()))

p=sum(l)
c=0
if p%2==0:
    for i in range(n):
        if l[i]%2==0:
            c=c+1
else:
    for i in range(n):
        if l[i]%2!=0:
            c=c+1
print(c)