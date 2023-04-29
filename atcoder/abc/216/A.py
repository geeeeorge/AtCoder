xy = input()

y = int(xy[-1])
x = xy[:-1]
x = x[:-1]

if y <= 2:
    print(x + '-')
elif y <= 6:
    print(x)
else:
    print(x + '+')
