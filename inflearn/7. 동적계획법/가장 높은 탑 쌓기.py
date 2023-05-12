import sys

if __name__ == "__main__":
    input = sys.stdin.readline

    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    arr.sort(reverse=True)
    dp = [0] * n
    dp[0] = arr[0][1]

    answer = 0
    for i in range(1, n):
        ca, ch, cw = arr[i]
        tmp = 0
        for j in range(i - 1, -1, -1):
            pa, ph, pw = arr[j]
            if cw < pw and tmp < dp[j]:
                tmp = dp[j]
        dp[i] = tmp + ch
        answer = max(answer, dp[i])

    print(answer)


