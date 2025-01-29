s = {
    "Tetrahedron": 4,
    "Cube": 6,
    "Octahedron": 8,
    "Dodecahedron": 12,
    "Icosahedron": 20
}

n = int(input())

t = 0
for _ in range(n):
    p = input()
    t += s[p]

print(t)
