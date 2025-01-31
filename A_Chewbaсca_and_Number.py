x = input()
result = ''

for digit in x:
    if int(digit) >= 5:
        result += str(9 - int(digit))
    else:
        result += digit

if result[0] == '0':
    result = '9' + result[1:]

print(result)
