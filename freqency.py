test = {'Codingal':2, 'is':2, 'best':2, 'for':2, 'coding':1}

print('Orignal dictionary:', str(test))

K = 2
res = 0
for key in test:
    if test[key] == K:
        res += 1

print('The frequency of K is ', res)