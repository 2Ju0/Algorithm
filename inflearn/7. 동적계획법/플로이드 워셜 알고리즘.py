import sys

if __name__ == '__main__':
    input = sys.stdin.readline

    n, m = map(int, input().split())
    dp = [[5000] * (n + 1) for _ in range(n + 1)]

    # 그래프 초기화
    for i in range(1, n + 1):
        dp[i][i] = 0

    for i in range(1, m + 1):
        s, e, w = map(int, input().split())
        dp[s][e] = w

    # (i -> j) 비용과 (i -> k -> j) 비용 비교
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if dp[i][j] == 5000:
                print('M', end=' ')
            else:
                print(dp[i][j], end=' ')
        print()
