N = int(input())

# Nを2で何回割れるかという問題
cnt = 0
while N > 1:
    N //= 2
    cnt += 1
print(cnt)