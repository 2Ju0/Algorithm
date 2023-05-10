import sys


def dfs(n):
    if arr[n] > 0:
        return arr[n]
    if n == 1 or n == 2:
        return n
    else:
        arr[n] = dfs(n - 1) + dfs(n - 2)
        return arr[n]


if __name__ == "__main__":
    n = int(sys.stdin.readline())
    arr = [0] * (n + 1)
    print(dfs(n))
