test = {'Codingal': '3', 'is': '2', 'best': '2', 'for': '2', 'coding': '1'}

print('Orignal dictionary:', str(test))

K = input('ENter key:')
res = 0
for key in test:
    if test[key] == K:
        res += 1

print('The frequency of K is ', res)
