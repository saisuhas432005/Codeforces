n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

x = 0
for i in range(n):
    x |= a[i]

y = 0
for i in range(n):
    y |= b[i]

print(x + y)
