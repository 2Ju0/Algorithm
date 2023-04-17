import sys


def dfs(cnt, sum):
    global result

    if cnt > result:  # cut edge
        return
    if sum > m:
        return
    if sum == m:
        if cnt < result:
            result = cnt
    else:
        for i in range(n):
            dfs(cnt + 1, sum + coins[i])


if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    coins = list(map(int, input().split()))
    m = int(input())
    result = 12
    coins.sort(reverse=True)

    dfs(0, 0)
    print(result)
