import heapq

N, H = map(int, input().split())
A, B = [], []
for _ in range(N):
    a, b = map(int, input().split())
    A.append(a)
    # 最大ヒープ
    heapq.heappush(B, -b)

ma = max(A)
cnt = 0
while H > 0:
    if len(B) == 0 or -B[0] <= ma:
        break
    damage = heapq.heappop(B)
    H += damage
    cnt += 1
if H > 0:
    cnt += (H + ma - 1) // ma
print(cnt)
