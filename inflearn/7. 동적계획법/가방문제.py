import sys


if __name__ == "__main__":
    input = sys.stdin.readline

    n, l = map(int, input().split())
    dp = [0] * (l + 1)

    for _ in range(n):
        w, v = map(int, input().split())
        for i in range(w, l + 1):
            dp[i] = max(dp[i], dp[i - w] + v)

    print(dp[l])
