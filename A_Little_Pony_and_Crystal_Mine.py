n = int(input())

for i in range(n):
    s = abs(n // 2 - i)
    t = n - 2 * s
    print("*" * s + "D" * t + "*" * s)
