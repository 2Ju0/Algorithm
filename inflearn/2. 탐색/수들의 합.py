import sys


if __name__ == "__main__":
    input = sys.stdin.readline

    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    res = 0

    for i in range(n):
        if arr[i] == m:
            res += 1
            continue
        elif arr[i] > m:
            continue
        tmp = arr[i]

        for j in range(i + 1, n):
            if tmp + arr[j] == m:
                res += 1
                break
            elif tmp + arr[j] > m:
                break
            tmp += arr[j]

    print(res)
