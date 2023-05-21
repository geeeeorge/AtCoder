H, W = map(int, input().split())
S = []
for i in range(H):
    S.append(input())

# 縦、横、斜めに"s", "n", "u", "k", "e"が連続してあるかチェック
for i in range(H):
    for j in range(W):
        if S[i][j] == "s":
            if i + 4 < H:
                if S[i + 1][j] == "n" and S[i + 2][j] == "u" and S[i + 3][j] == "k" and S[i + 4][j] == "e":
                    i, j = i+1, j+1
                    print(i, j)
                    print(i+1, j)
                    print(i+2, j)
                    print(i+3, j)
                    print(i+4, j)
                    break
            if i - 4 >= 0:
                if S[i - 1][j] == "n" and S[i - 2][j] == "u" and S[i - 3][j] == "k" and S[i - 4][j] == "e":
                    i, j = i+1, j+1
                    print(i, j)
                    print(i-1, j)
                    print(i-2, j)
                    print(i-3, j)
                    print(i-4, j)
                    break
            if j + 4 < W:
                if S[i][j + 1] == "n" and S[i][j + 2] == "u" and S[i][j + 3] == "k" and S[i][j + 4] == "e":
                    i, j = i+1, j+1
                    print(i, j)
                    print(i, j+1)
                    print(i, j+2)
                    print(i, j+3)
                    print(i, j+4)
                    break
            if j - 4 >= 0:
                if S[i][j - 1] == "n" and S[i][j - 2] == "u" and S[i][j - 3] == "k" and S[i][j - 4] == "e":
                    i, j = i+1, j+1
                    print(i, j)
                    print(i, j-1)
                    print(i, j-2)
                    print(i, j-3)
                    print(i, j-4)
                    break
            if i + 4 < H and j + 4 < W:
                if S[i + 1][j + 1] == "n" and S[i + 2][j + 2] == "u" and S[i + 3][j + 3] == "k" and S[i + 4][j + 4] == "e":
                    i, j = i+1, j+1
                    print(i, j)
                    print(i+1, j+1)
                    print(i+2, j+2)
                    print(i+3, j+3)
                    print(i+4, j+4)
                    break
            if i + 4 < H and j - 4 >= 0:
                if S[i + 1][j - 1] == "n" and S[i + 2][j - 2] == "u" and S[i + 3][j - 3] == "k" and S[i + 4][j - 4] == "e":
                    i, j = i+1, j+1
                    print(i, j)
                    print(i+1, j-1)
                    print(i+2, j-2)
                    print(i+3, j-3)
                    print(i+4, j-4)
                    break
            if i - 4 >= 0 and j + 4 < W:
                if S[i - 1][j + 1] == "n" and S[i - 2][j + 2] == "u" and S[i - 3][j + 3] == "k" and S[i - 4][j + 4] == "e":
                    i, j = i+1, j+1
                    print(i, j)
                    print(i-1, j+1)
                    print(i-2, j+2)
                    print(i-3, j+3)
                    print(i-4, j+4)
                    break
            if i - 4 >= 0 and j - 4 >= 0:
                if S[i - 1][j - 1] == "n" and S[i - 2][j - 2] == "u" and S[i - 3][j - 3] == "k" and S[i - 4][j - 4] == "e":
                    i, j = i+1, j+1
                    print(i, j)
                    print(i-1, j-1)
                    print(i-2, j-2)
                    print(i-3, j-3)
                    print(i-4, j-4)
                    break
