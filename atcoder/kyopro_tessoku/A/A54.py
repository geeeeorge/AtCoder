Q = int(input())
d = {}
query = [input().split() for _ in range(Q)]
for q in query:
    if q[0] == "1":
        d[q[1]] = int(q[2])
    else:
        print(d[q[1]])
