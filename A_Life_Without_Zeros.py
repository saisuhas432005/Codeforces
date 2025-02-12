a = int(input())
b = int(input())

az = int(''.join([char for char in str(a) if char != '0']))

bz = int(''.join([char for char in str(b) if char != '0']))

p = a + b

cz = int(''.join([char for char in str(p) if char != '0']))

if az + bz == cz:
    print("YES")
else:
    print("NO")
