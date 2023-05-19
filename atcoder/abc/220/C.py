N = int(input())
A = list(map(int, input().split()))
X = int(input())

ans = 0
lenA = len(A)
sumA = sum(A)

# sumAで引けるだけ引く
ans += (X // sumA) * lenA
X -= sumA * ans // lenA

# 残りを一つずつ見ていく
for a in A:
    if X < a:
        ans += 1
        break
    X -= a
    ans += 1
print(ans)
