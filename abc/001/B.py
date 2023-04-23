m = int(input())
if m < 100:
    print('00')
elif m <= 5000:
    m //= 100
    if m < 10:
        print('0' + str(m))
    else:
        print(m)
elif m <= 30000:
    m //= 1000
    print(m + 50)
elif m <= 70000:
    m -= 30000
    m //= 5000
    m += 80
    print(m)
else:
    print(89)
