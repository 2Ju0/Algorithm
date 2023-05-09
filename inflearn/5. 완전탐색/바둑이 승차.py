import sys


def dfs(idx, sum, tsum):
    global result

    if result > sum + (total - tsum):
        return
    if sum > c:
        return
    if idx == n:
        if sum > result:
            result = sum
    else:
        dfs(idx + 1, sum + weight[idx], tsum + weight[idx])
        dfs(idx + 1, sum, tsum + weight[idx])


if __name__ == "__main__":
    input = sys.stdin.readline

    c, n = map(int, input().split())
    weight = [int(input()) for _ in range(n)]
    total = sum(weight)
    result = 0

    dfs(0, 0, 0)
    print(result)
