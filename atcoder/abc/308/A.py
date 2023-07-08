S = list(map(int, input().split()))

for i in range(7):
    if S[i] <= S[i+1]:
        continue
    else:
        print("No")
        exit()

for i in range(8):
    if (100 <= S[i] <= 675) and (S[i] % 25 == 0):
        continue
    else:
        print("No")
        exit()

print("Yes")
