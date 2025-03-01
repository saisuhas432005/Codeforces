n = int(input())
r = input()

c = 0
grp = []

for i in r:
    if i == 'B':
        c += 1
    else:
        if c > 0:
            grp.append(c)
            c = 0

if c > 0:
    grp.append(c)

print(len(grp))
print(*grp)
