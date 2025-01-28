n = int(input())

red = -1
p = []

for _ in range(n):
    h, b, a = input().split()
    b, a = int(b), int(a)
    p.append((h, b, a))
    if b >= 2400:
        red = max(red, b)

anton = -1
for i in p:
    h, b, a = i
    if b < 2400 and a > b and b < red:
        anton = max(anton, a - b)

if anton > 0:
    print("YES")
else:
    print("NO")
