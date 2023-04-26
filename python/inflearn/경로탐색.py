import sys
import copy


def dfs(v):
    global total

    if v == n:
        total += 1
        return
    else:
        for i in range(1, n + 1):
            if graph[v][i] == 1 and visited[i] == 0:
                visited[i] = 1
                dfs(i)
                visited[i] = 0


if __name__ == "__main__":
    input = sys.stdin.readline

    n, m = map(int, input().split())
    graph = [[0] * (n + 1) for _ in range(n + 1)]
    visited = [0] * (n + 1)
    total = 0

    for _ in range(m):
        start, end = map(int, input().split())
        graph[start][end] = 1

    dfs(1)
    print(total)
