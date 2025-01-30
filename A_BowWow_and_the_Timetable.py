def binary_string_to_integer(binary_string):
    return int(binary_string, 2)

n=input()

k=binary_string_to_integer(n)
c=0
for i in range(2**100):
    if 4**i<k:
        c=c+1
    else:
        break
print(c)