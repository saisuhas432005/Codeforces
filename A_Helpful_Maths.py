
numbers = list(map(int, input().split('+')))  
numbers.sort()
new_sum_string = '+'.join(map(str, numbers))
print(new_sum_string)
