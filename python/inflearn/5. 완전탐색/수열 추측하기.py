import sys
import itertools as it


def dfs(cnt):
    if cnt == n:
        sum = 0
        for i in range(n):
            sum += answer[i] * p[i]
        if sum == f:
            print(' '.join([str(i) for i in answer]))
            sys.exit(0)
    else:
        for i in range(1, n + 1):
            if not visited[i]:
                visited[i] = 1
                answer[cnt] = i
                dfs(cnt + 1)
                visited[i] = 0


if __name__ == "__main__":
    input = sys.stdin.readline

    n, f = map(int, input().split())
    visited = [0] * (n + 1)
    answer = [0] * n
    p = [0] * n

    tmp = [i for i in range(1, n)]
    for i in range(n):
        p[i] = len(list(it.combinations(tmp, i)))

    dfs(0)
