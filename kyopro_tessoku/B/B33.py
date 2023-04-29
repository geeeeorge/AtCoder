N, H, W = map(int, input().split())
AB = []
for i in range(N):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    AB.append(a)
    AB.append(b)

# 2Nのニム
xor_sum = AB[0]
for i in range(1, 2 * N):
    xor_sum = xor_sum ^ AB[i]

print('First' if xor_sum != 0 else 'Second')
