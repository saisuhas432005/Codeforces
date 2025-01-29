def last(n):
    if n == 0:
        return 1
    l = [8, 4, 2, 6]
    return l[(n - 1) % 4]

n = int(input())
r = last(n)
print(r)
