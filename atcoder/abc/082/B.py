S = input()
T = input()

S = ''.join(sorted(S))
T = ''.join(sorted(T, reverse=True))

print("Yes" if S < T else "No")
