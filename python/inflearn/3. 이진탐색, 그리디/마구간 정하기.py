import sys

if __name__ == "__main__":
    input = sys.stdin.readline

    n, c = map(int, input().split())
    arr = [int(input()) for _ in range(n)]
    arr.sort()

    start = arr[0]
    end = arr[n - 1]
    answer = 0

    while start <= end:
        mid = (start + end) // 2

        cnt = 1
        tmp = arr[0]
        for x in arr[1:]:
            if tmp + mid <= x:
                cnt += 1
                tmp = x

        if cnt >= c:
            start = mid + 1
            answer = mid
        else:
            end = mid -1

    print(arr)
