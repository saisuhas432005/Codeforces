n = int(input())
a = [""] * (n + 2)
b = '1'
a[0] = ""
a[n+1] = ""

for i in range(n + 2):
    a[0] += b
    a[n+1] += b

for i in range(1, n + 1):
    a[i] = input()

for i in range(1, n + 1):
    a[i] = b + a[i] + b

z = 0
y = 0
for i in range(1, n + 1):
    for j in range(1, n + 1):
        x = 0
        if a[i][j-1] == 'o':
            x += 1
        if a[i][j+1] == 'o':
            x += 1
        if a[i-1][j] == 'o':
            x += 1
        if a[i+1][j] == 'o':
            x += 1
        if x % 2 == 1:
            y = 1
            break
    if y == 1:
        z = 1
        break

if z == 0:
    print("YES")
else:
    print("NO")
