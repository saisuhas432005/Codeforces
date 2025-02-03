t = int(input())

for _ in range(t):
    n = int(input())
    s = input()
    
    a=s
    b=s[::-1]
    
    c=b+a
    print(min(a,c))
