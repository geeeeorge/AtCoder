from collections import deque
N, X = map(int, input().split())
X -= 1
tmp = input()
A = []
for i in range(N):
    A.append(tmp[i])

queue = deque()
queue.append(X)
A[X] = '@'

while queue:
    pos = queue.popleft()
    if pos - 1 >= 0 and A[pos - 1] == '.':
        queue.append(pos - 1)
        A[pos - 1] = '@'
    if pos + 1 < N and A[pos + 1] == '.':
        queue.append(pos + 1)
        A[pos + 1] = '@'

print(*A, sep='')
