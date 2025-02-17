n = int(input())
c = list(map(int, input().split()))
k=len(c)-1
m1 = abs(c[0] - c[1])
m2 = abs(c[0] - c[k])

m3 = abs(c[k] - c[-2])
m4 = abs(c[k] - c[0])

print(m1, m2)
for i in range(1, n - 1):
    m5 = min(abs(c[i] - c[i - 1]), abs(c[i] - c[i + 1]))
    m6 = max(abs(c[i] - c[0]), abs(c[i] - c[k]))
    print(m5, m6)
    
print(m3, m4)
