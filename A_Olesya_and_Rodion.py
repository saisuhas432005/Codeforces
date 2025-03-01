n, t = map(int, input().split())

if n == 1 and t == 10:
    print(-1)
else:
    if t == 10:
        num = 10 ** (n - 1)
    else:
        num = 10 ** (n - 1) * t
    print(num)
