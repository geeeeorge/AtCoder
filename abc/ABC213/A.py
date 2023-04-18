A, B = map(int, input().split())

# Aを二進法にする
A = bin(A)[2:]
# Bを二進法にする
B = bin(B)[2:]
# AとBのxorをとる
xor = int(A, 2) ^ int(B, 2)
print(xor)
