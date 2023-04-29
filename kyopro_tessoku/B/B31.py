N = int(input())

n3 = N // 3
n5 = N // 5
n7 = N // 7
n15 = N // 15
n21 = N // 21
n35 = N // 35
n105 = N // 105

print(n3 + n5 + n7 - n15 - n21 - n35 + n105)
