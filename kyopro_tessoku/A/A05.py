N, K = map(int, input().split())

ans = 0

# 3つの和がKになる組み合わせを求める
# 3重ループにする必要はない
# 2つのループでK - i - jがN以下の場合にカウントすれば良い
for i in range(1, N+1):
    for j in range(1, N+1):
        if 1 <= K - i - j <= N:
            ans += 1

print(ans)

