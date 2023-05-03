S = input()
stack = []
ans = []
for i, s in enumerate(S):
    i += 1
    if s == '(':
        stack.append(i)
    elif s == ')':
        start = stack.pop()
        ans.append((start, i))
for a in ans:
    print(*a)
