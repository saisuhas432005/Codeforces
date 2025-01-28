n=int(input())
l=input()
o=l.count('A')
p=l.count('D')

if o>p:
    print('Anton')
elif p>o:
    print("Danik")
else:
    print("Friendship")

