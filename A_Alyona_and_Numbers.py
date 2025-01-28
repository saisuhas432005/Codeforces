n, m = map(int, input().split())

remainder_counts = [0] * 5

for x in range(1, n + 1):
    remainder_counts[x % 5] += 1

pairs_count = 0
for y in range(1, m + 1):
    pairs_count += remainder_counts[(5 - y % 5) % 5]

print(pairs_count)


# n,m=map(int,input().split())
# c=0
# for i in range(1,n+1):
#     for j in range(1,m+1):
#         if (i+j)%5==0:
#             c=c+1
# print(c)