N = int(input())
W = list(input().split())

a = ["and", "not", "that", "the", "you"]

for i in range(N):
    if W[i] in a:
        print("Yes")
        exit()
print("No")
