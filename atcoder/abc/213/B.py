N = int(input())
A = list(map(int, input().split()))

max_index = A.index(max(A))
A.pop(max_index)

booby_index = A.index(max(A))
if booby_index >= max_index:
    print(booby_index + 2)
else:
    print(booby_index + 1)
