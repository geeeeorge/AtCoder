C = [list(map(int, input().split())) for _ in range(3)]
a1 = 0
b1 = C[0][0] - a1
b2 = C[0][1] - a1
b3 = C[0][2] - a1
a2 = C[1][0] - b1
a3 = C[2][0] - b1

# 未確定の4つが正しいか確認
if C[1][1] == a2 + b2 and C[1][2] == a2 + b3 and C[2][1] == a3 + b2 and C[2][2] == a3 + b3:
    print("Yes")
else:
    print("No")
