N, M = map(int, input().split())
products = []

for _ in range(N):
    p, c, *f = map(int, input().split())
    features = set(f)
    products.append((p, features))

for i in range(N):
    for j in range(N):
        pi, ci = products[i]
        pj, cj = products[j]
        if pi >= pj and cj.issuperset(ci) and (pi > pj or ci != cj):
            print("Yes")
            exit()

print("No")
