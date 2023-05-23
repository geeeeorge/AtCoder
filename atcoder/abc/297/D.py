A, B = map(int, input().split())

ans = 0
while A != B:
    if A > B:
        ans += A // B
        A = A % B
        if A == 0:
            ans -= 1
            break
    else:
        ans += B // A
        B = B % A
        if B == 0:
            ans -= 1
            break
print(ans)
