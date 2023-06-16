N = int(input())
a = abs(N - (N // 5) * 5)
b = abs(((N + 5) // 5) * 5 - N)
if a < b:
    print(N // 5 * 5)
else:
    print((N + 5) // 5 * 5)
