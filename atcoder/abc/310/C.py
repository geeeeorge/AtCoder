N = int(input())
balls = set()
for _ in range(N):
    s = input().strip()
    if s not in balls and s[::-1] not in balls:
        balls.add(s)
print(len(balls))
