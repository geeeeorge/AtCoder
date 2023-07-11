A, B = map(int, input().split())

if B - A == 1:
    if A != 3 and A != 6:
        print('Yes')
        exit()
print('No')
