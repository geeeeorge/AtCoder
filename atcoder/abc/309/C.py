from collections import defaultdict

N, K = map(int, input().split())
prescribed_medicines = defaultdict(int)

for _ in range(N):
    a, b = map(int, input().split())
    prescribed_medicines[a] += b

prescribed_days = list(prescribed_medicines.keys())
prescribed_days.sort()

# Aの2つ目の要素の後ろから累積和を求める
N = len(prescribed_days)
B = [0] * (N + 1)
for i in range(0, N):
    B[N-i-1] = B[N-i] + prescribed_medicines[prescribed_days[N-i-1]]

for i in range(N):
    if B[i] <= K:
        if i == 0:
            print(1)
        else:
            print(prescribed_days[i-1] + 1)
        exit()
print(prescribed_days[N-1] + 1)
