import sys

if __name__ == "__main__":
    input = sys.stdin.readline

    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()

    start = 0
    end = n - 1

    while start <= end:
        mid = (start + end) // 2

        if arr[mid] == m:
            print(mid + 1)
            break
        elif arr[mid] < m:
            start = mid + 1
        else:
            end = mid - 1
