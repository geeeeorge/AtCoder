N = int(input())
A = list(map(int, input().split()))

A.sort()
alice = 0
bob = 0

is_alice = True
while A:
    if is_alice:
        alice += A.pop()
    else:
        bob += A.pop()
    is_alice = not is_alice
print(alice - bob)
