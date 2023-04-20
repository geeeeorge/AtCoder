def weak_or_strong(password):
    arr = [str(i) for i in range(10)]
    arr.append('0')

    # 連続チェック
    for i in range(3):
        if a[i] != a[i+1]:
            break
        if i == 2:
            return "Weak"

    # リングチェック
    for i in range(3):
        idx1 = arr.index(a[i])
        idx2 = arr.index(a[i+1])
        if arr[idx1+1] != arr[idx2]:
            break
        if i == 2:
            return "Weak"
    return "Strong"


if __name__ == '__main__':
    a = str(input())
    print(weak_or_strong(a))
