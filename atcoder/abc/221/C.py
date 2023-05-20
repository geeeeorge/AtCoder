from itertools import product


N = list(input())

max_ans = 0
# a: 0, b: 1
for bits in product([0, 1], repeat=len(N)):
    a = [x for bit, x in zip(bits, N) if bit == 0]
    b = [x for bit, x in zip(bits, N) if bit == 1]
    if not a or not b:
        continue
    a.sort()
    b.sort()

    a.reverse()
    b.reverse()
    max_ans = max(max_ans, int(''.join(a)) * int(''.join(b)))

print(max_ans)
