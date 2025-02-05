# n = int(input())
# g = [input() for _ in range(n)]

# c = {}
# for i in g:
#     if i in c:
#         c[i] += 1
#     else:
#         c[i] = 1

# m = 0
# k = None
# for i, s in c.items():
#     if s > m:
#         m = s
#         k = i

# print(k)

n=int(input())
l=[]

for i in range(n):
    u=input()
    l.append(u)
    
k=set(l)

l.sort()

print(l[int(n//2)])
