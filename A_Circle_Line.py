n = int(input())
d = list(map(int, input().split()))
s, t = map(int, input().split())

c = sum(d[min(s, t) - 1:max(s, t) - 1])

cc = sum(d) - c

print(min(c, cc))
