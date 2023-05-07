class RollingHash:
    def __init__(self, s, b=3491, m=999999937):
        n = len(s)
        self.prefix = prefix = [0] * (n+1)
        self.power = power = [1] * (n+1)
        self.b = b
        self.m = m
        for i in range(n):
            c = ord(s[i])
            prefix[i+1] = (prefix[i] * b + c) % m
            power[i+1] = (power[i] * b) % m

    def get(self, l, r):
        return (self.prefix[r] - self.power[r-l] * self.prefix[l]) % self.m


N, Q = map(int, input().split())
S = input()

rh1 = RollingHash(S)
rh2 = RollingHash(S[::-1])
for _ in range(Q):
    l, r = map(int, input().split())
    if rh1.get(l-1, r) == rh2.get(N-r, N-l+1):
        print('Yes')
    else:
        print('No')
