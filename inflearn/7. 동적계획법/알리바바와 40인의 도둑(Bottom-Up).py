import sys

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    arr = [list(map(int, input().split())) for _ in range(n)]
    dp = [[0] * n for _ in range(n)]
    dp[0][0] = arr[0][0]
    
    # 0행, 0열 초기화
    for i in range(1, n):
        dp[0][i] = dp[0][i - 1] + arr[0][i]
        dp[i][0] = dp[i - 1][0] + arr[i][0]
    
    # 왼, 위에서 오는 값 비교
    for i in range(1, n):
        for j in range(1, n):
            dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + arr[i][j]

    print(dp[n - 1][n - 1])
