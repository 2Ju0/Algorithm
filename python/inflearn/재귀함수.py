import sys


def dfs(n):
    if n > 0:
        dfs(n - 1)
        print(n, end=" ")


if __name__ == "__main__":
    n = int(sys.stdin.readline())
    dfs(n)
