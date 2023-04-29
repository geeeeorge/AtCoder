N, K = map(int, input().split())

min_k = 2 * N - 2
if K < min_k or K % 2 == 1:
    print('No')
else:
    print('Yes')
