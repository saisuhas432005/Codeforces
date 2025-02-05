n = int(input())

cake = [input() for _ in range(n)]

h = 0

for i in range(n):
    row = cake[i].count('C')
    h += row * (row - 1) // 2

for j in range(n):
    col = sum(cake[i][j] == 'C' for i in range(n))
    h += col * (col - 1) // 2

print(h)
