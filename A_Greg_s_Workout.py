n = int(input())
rep = list(map(int, input().split()))

c = 0
b = 0
ba = 0

for i in range(n):
    if i % 3 == 0:
        c += rep[i]
    elif i % 3 == 1:
        b += rep[i]
    else:
        ba += rep[i]

m = max(c, b, ba)

if m == c:
    print("chest")
elif m == b:
    print("biceps")
else:
    print("back")
