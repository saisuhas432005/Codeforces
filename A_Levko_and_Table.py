a, b = map(int, input().split())

for i in range(a):
    c = [0] * a
    c[i] = b
    print(*c)
