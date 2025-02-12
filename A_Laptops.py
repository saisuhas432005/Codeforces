n = int(input())
l = [tuple(map(int, input().split())) for _ in range(n)]
l.sort()

for i in range(1, n):
    if l[i][1] < l[i-1][1]:
        print("Happy Alex")
        break
else:
    print("Poor Alex")
