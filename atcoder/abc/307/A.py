N = int(input())
A = list(map(int, input().split()))

for i in range(len(A)//7):
    print(sum(A[i*7:(i+1)*7]), end=' ')
