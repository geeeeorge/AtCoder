from collections import deque

Q = int(input())

stack = deque()
for _ in range(Q):
    query = list(map(str, input().split()))
    if query[0] == "1":
        stack.append(query[1])
    elif query[0] == "2":
        print(stack[0])
    elif query[0] == "3":
        stack.popleft()
    else:
        raise ValueError
