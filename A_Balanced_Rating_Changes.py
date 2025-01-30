n = int(input())
m = 1
for i in range(n):
    rating_change = int(input())
    if rating_change % 2 == 0:
        print(rating_change // 2)
    else:
        print(rating_change // 2 + m)
        m = 1 - m
