import sys


def dfs(n):
    global answer

    if n == v:
        answer += 1
        return
    else:
        for i in range(1, v + 1):
            if graph[n][i] == 1 and visited[i] == 0:
                visited[i] = 1
                dfs(i)
                visited[i] = 0


if __name__ == "__main__":
    input = sys.stdin.readline

    v, e = map(int, input().split())
    graph = [[0] * (v + 1) for _ in range(v + 1)]
    visited = [0] * (v + 1)
    answer = 0

    for _ in range(e):
        start, end = map(int, input().split())
        graph[start][end] = 1

    visited[1] = 1
    dfs(1)
    print(answer)
