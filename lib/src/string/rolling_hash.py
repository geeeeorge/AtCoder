class RollingHash:
    """
    ローリングハッシュ
    """
    def __init__(self, s, b=3491, m=999999937):
        """任意の基数と法でハッシュを生成する"""
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
        """S[l, r) のハッシュを求める"""
        return (self.prefix[r] - self.power[r-l] * self.prefix[l]) % self.m
