n = input().strip()
m = n.split("WUB")
#print(m)
# print(''.join(map(str,m)))
w = []
for i in m:
    if i != "":
        w.append(i)

o = " ".join(w)
print(o)
