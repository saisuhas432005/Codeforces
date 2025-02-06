n = int(input())

x = list(map(int, input().split()))[1:]  
y = list(map(int, input().split()))[1:]  
k = x + y
o = set(k)

if len(o) == n:  
    print("I become the guy.")
else:
    print("Oh, my keyboard!")
