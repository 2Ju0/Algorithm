import sys

if __name__ == "__main__":
    input = sys.stdin.readline

    n, m = map(int, input().split())
    arr = list(map(int, input().split()))

    answer = 0
    start = 1
    end = sum(arr)

    while start <= end:
        mid = (start + end) // 2

        cnt = 1
        tmp = 0
        for v in arr:
            if tmp + v > mid:
                cnt += 1
                tmp = v
            else:
                tmp += v

        if cnt > m:
            start = mid + 1
        else:
            end = mid - 1
            answer = mid

    print(answer)
