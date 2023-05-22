import sys


if __name__ == "__main__":
    input = sys.stdin.readline

    n = int(input())
    coins = list(map(int, input().split()))
    m = int(input())

    dp = [1000] * (m + 1)
    dp[0] = 0

    for coin in coins:
        for i in range(coin, m + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    print(dp[m])
