import sys

if __name__ == "__main__":
    input = sys.stdin.readline

    n = int(input())
    arr = list(map(int, input().split()))
    dp = [0] * n
    dp[0] = 1
    answer = 0

    for i in range(1, n):
        tmp = 0
        for j in range(i - 1, 0, -1):
            if arr[j] < arr[i] and tmp < dp[j]:
                tmp = dp[j]
        dp[i] = tmp + 1
        answer = max(answer, dp[i])

    print(answer)


