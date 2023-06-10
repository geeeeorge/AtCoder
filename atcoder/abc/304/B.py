N = int(input())

if N < 1000:
    print(N)
    exit()
if N < 10000:
    # Nの1の位を切り捨て
    print(N - N % 10)
    exit()
if N < 100000:
    # Nの10の位を切り捨て
    print(N - N % 100)
    exit()
if N < 1000000:
    # Nの100の位を切り捨て
    print(N - N % 1000)
    exit()
if N < 10000000:
    # Nの1000の位を切り捨て
    print(N - N % 10000)
    exit()
if N < 100000000:
    # Nの10000の位を切り捨て
    print(N - N % 100000)
    exit()
if N < 1000000000:
    # Nの100000の位を切り捨て
    print(N - N % 1000000)
    exit()
