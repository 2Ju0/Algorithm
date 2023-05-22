import sys

if __name__ == '__main__':
    input = sys.stdin.readline

    n = int(input())
    dp = [[100] * (n + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        dp[i][i] = 0

    while True:
        a, b = map(int, input().split())
        if a == -1 and b == -1:
            break
        dp[a][b] = 1
        dp[b][a] = 1

    for k in range(1, n + 1):
        for i in range(1, n + 1):
            if k == i:
                continue
            for j in range(1, n + 1):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])

    scores = [0] * (n + 1)
    for i in range(1, n + 1):
        scores[i] = max(dp[i][1:])

    score = min(scores[1:])
    answer = []
    for i in range(1, n + 1):
        if scores[i] == score:
            answer.append(str(i))

    print(score, len(answer))
    print(' '.join(answer))
