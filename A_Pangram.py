n = int(input())
k = list(map(str, input().strip()))
k.sort()
l = [string.lower() for string in k]
m = set(l)

if len(m) == 26:
    print("YES")
else:
    print("NO")
