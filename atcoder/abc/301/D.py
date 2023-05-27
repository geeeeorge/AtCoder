from copy import deepcopy


S = input()
N = int(input())

# Sの?をすべて0にする
zero_replaced = S.replace("?", "0")
if int(zero_replaced, 2) > N:
    print(-1)
    exit()

new_s = list(deepcopy(zero_replaced))
# そうでないなら上から貪欲
for i in range(len(S)):
    if S[i] == "?":
        new_s[i] = "1"
        new_s = "".join(new_s)
        if int(new_s, 2) <= N:
            new_s = list(new_s)
        else:
            new_s = list(new_s)
            new_s[i] = "0"

ans = int("".join(new_s), 2)
print(ans)
