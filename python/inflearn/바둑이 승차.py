import sys


def dfs(cnt, sum, tsum):
    global result

    if result > sum + (total - tsum):
        return
    if sum > c:
        return
    if cnt == len(weight):
        if sum > result:
            result = sum
    else:
        dfs(cnt + 1, sum + weight[cnt], tsum + weight[cnt])
        dfs(cnt + 1, sum, tsum + weight[cnt])


if __name__ == "__main__":
    c, n = map(int, sys.stdin.readline().split())
    weight = [int(sys.stdin.readline()) for _ in range(n)]
    total = sum(weight)
    result = 0
    dfs(0, 0, 0)
    print(result)
