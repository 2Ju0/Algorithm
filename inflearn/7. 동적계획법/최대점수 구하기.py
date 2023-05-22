import sys

if __name__ == '__main__':
    input = sys.stdin.readline

    n, m = map(int, input().split())
    dp = [0] * (m + 1)

    for _ in range(n):
        score, time = map(int, input().split())
        for i in range(time, m + 1):
            dp[i] = max(dp[i], dp[i - time] + score)

    print(dp[m])
