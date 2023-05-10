from collections import deque
H, W = map(int, input().split())
A = deque(deque() for _ in range(H))
B = deque(deque() for _ in range(H))
for i in range(H):
    a = input()
    for j in range(W):
        A[i].append(a[j])

for i in range(H):
    b = input()
    for j in range(W):
        B[i].append(b[j])


def check(A, B):
    for i in range(H):
        for j in range(W):
            if A[i][j] != B[i][j]:
                return False
    return True


for _ in range(H):
    for _ in range(W):
        if check(A, B):
            print('Yes')
            exit()

        # 右に回転
        for i in range(H):
            A[i].rotate(1)

    # 下に回転
    A.rotate(1)

print('No')
