import sys

if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(sys.stdin.readline())
    dp = [0] * 16
    dp[0] = 2

    for i in range(1, n + 1):
        dp[i] = dp[i - 1] + (dp[i - 1] - 1)

    print(dp[n] ** 2)
