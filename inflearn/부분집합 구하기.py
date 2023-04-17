import sys


# 상태트리
def dfs(v):
    if v > n:
        print(' '.join([str(i) for i in range(1, n + 1) if visited[i] == 1]))
    else:
        visited[v] = 1
        dfs(v + 1)
        visited[v] = 0
        dfs(v + 1)


if __name__ == "__main__":
    n = int(sys.stdin.readline())
    visited = [0] * (n + 1)
    dfs(1)
