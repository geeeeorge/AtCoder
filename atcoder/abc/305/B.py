p, q = input().split()

al = [3, 1, 4, 1, 5, 9]
if ord(q) < ord(p):
    p, q = q, p

a = ord(p) - ord('A')
b = ord(q) - ord('A')
# al[q]からal[p]までの和
ans = sum(al[a:b])
print(ans)
