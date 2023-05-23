S = input()
R = []
K = []
B = []
for i in range(8):
    if S[i] == "B":
        B.append(i)
    if S[i] == "R":
        R.append(i)
    if S[i] == "K":
        K.append(i)

print("Yes" if B[0] % 2 != B[1] % 2 and R[0] < K[0] < R[1] else "No")
