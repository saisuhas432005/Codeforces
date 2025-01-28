n=input()
l='abcdefghijklmnopqrstuvwxyz'
p=[]
for i in n:
    if i in l:
        p.append(i)
print(len(set(p)))