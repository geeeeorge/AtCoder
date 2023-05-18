X = input()
N = int(input())

a = []
for _ in range(N):
    S = input()
    new_s = ''
    for s in S:
        new_s += chr(X.index(s) + ord('a'))

    a.append((new_s, S))

a.sort(key=lambda x: x[0])
for s in a:
    print(s[1])
