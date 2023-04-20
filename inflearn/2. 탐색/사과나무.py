import sys

if __name__ == "__main__":
    input = sys.stdin.readline

    n = int(input())
    mid = n // 2
    res = 0

    for i in range(n):
        row = list(map(int, input().split()))

        if i <= mid:
            res += sum(row[mid - i:mid + i + 1])
        else:
            res += sum(row[mid - (n - 1 - i):mid + (n - 1 - i) + 1])

    print(res)
