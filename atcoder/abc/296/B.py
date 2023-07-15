S = [input() for i in range(8)]

r = -1
l = -1
for i in range(8):
    for j in range(8):
        if S[i][j] == '*':
            r = i
            l = j

print(chr(ord('a')+l)+str(8-r))
