n=input()

dist=[]

for i in n:
    if i not in dist:
        dist.append(i)
if len(dist)%2==0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")
    
