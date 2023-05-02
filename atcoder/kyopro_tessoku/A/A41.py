N = int(input())

S = input()

for i in range(N-2):
    if S[i] == S[i + 1] == S[i + 2]:
        print('Yes')
        exit()
print('No')
