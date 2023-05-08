num500 = int(input())
num100 = int(input())
num50 = int(input())
total = int(input())

ans = 0

for i in range(num500+1):
    for j in range(num100+1):
        for k in range(num50+1):
            if i*500 + j*100 + k*50 == total:
                ans += 1
print(ans)
