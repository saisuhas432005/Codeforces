n=int(input())
l=input()

s=l.count("1")
p=l.count("0")

m=max(s,p)
o=min(s,p)

print(m-o)