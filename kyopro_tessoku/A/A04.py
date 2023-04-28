N = int(input())

# Nを2進数に変換
N_bin = bin(N)[2:]

# N_binを8桁にパディング
N_bin = N_bin.zfill(10)
print(N_bin)
