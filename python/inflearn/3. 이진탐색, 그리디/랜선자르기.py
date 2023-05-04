import sys

if __name__ == "__main__":
    input = sys.stdin.readline

    k, n = map(int, input().split())
    arr = [int(input()) for _ in range(k)]

    start = 0
    end = max(arr)
    answer = 0

    while start <= end:
        mid = (start + end) // 2

        total = 0
        for i in arr:
            total += i // mid

        if total >= n:
            start = mid + 1
            answer = mid
        else:
            end = mid - 1

    print(answer)
