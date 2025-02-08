# n = int(input())
# s = []
# t = []

# for _ in range(n):
#     a, b = map(int, input().split())
#     s.append(a)
#     t.append(b)

# if any(s[i] != t[i] for i in range(n)):
#     print("rated")
# elif s == sorted(s, reverse=True):
#     print("maybe")
# else:
#     print("unrated")

n=int(input())
t=tuple(tuple(map(int,input().split())) for _ in range(n))
if any(t[i][0]!=t[i][1] for i in range(n)): 
    print("rated")
elif t==tuple(sorted(t,reverse=True)):
    print("maybe")
else:
    print("unrated")
    