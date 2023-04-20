N = int(input())

l = []

while N > 0:
    if N % 2 == 0:
        N //= 2
        l.append('B')
    else:
        N -= 1
        l.append('A')

# lを逆順にする
l.reverse()

print(''.join(l))
