s = input().strip()
n = int(input().strip())

p = []
for _ in range(n):
    p.append(input().strip())

p.sort()  

f = None
for page in p:
    if page.startswith(s):
        f = page
        break

if f:
    print(f)
else:
    print(s)
