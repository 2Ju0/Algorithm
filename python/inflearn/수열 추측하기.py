import sys


def dfs(cnt):
    if cnt == n:
        sum = 0
        for i in range(n):
            sum += p[i] * result[i]
        if sum == f:
            print(' '.join([str(num) for num in result]))
            sys.exit(0)
    else:
        for i in range(1, n + 1):
            if not visited[i]:
                visited[i] = 1
                result[cnt] = i
                dfs(cnt + 1)
                visited[i] = 0


if __name__ == "__main__":
    n, f = map(int, sys.stdin.readline().split())
    visited = [0] * (n + 1)
    result = [0] * n
    p = [0] * n

    for i in range(n):
        if i == 0:
            p[i] = 1
        elif i == 1:
            p[i] = (n-1)
        else:
            a = 1
            b = 1
            for j in range(i):
                a *= ((n-1)-j)
                b *= (i-j)
            p[i] = a // b

    dfs(0)
