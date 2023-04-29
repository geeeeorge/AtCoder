N = int(input())
A = list(map(int, input().split()))

# ニム
xor_sum = A[0]
for i in range(1, N):
    xor_sum = xor_sum ^ A[i]
print('First' if xor_sum != 0 else 'Second')
