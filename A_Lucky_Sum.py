def f(x):
    S.add(x)
    if x < r:
        f(x * 10 + 4)
        f(x * 10 + 7)

l, r = map(int, input().split())
s = 0
S = set()

for_0 = 0
f(for_0)

while l <= r:
    it = next(i for i in sorted(S) if i >= l)
    s += (min(r, it) - l + 1) * it
    l = it + 1

print(s)

