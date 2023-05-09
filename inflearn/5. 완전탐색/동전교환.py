import sys


def dfs(cnt, sum):
    global answer

    if cnt > answer:  # cut edge
        return
    if sum > m:
        return
    elif sum == m:
        if cnt < answer:
            answer = cnt
            return
    else:
        for i in range(n):
            dfs(cnt + 1, sum + coins[i])


if __name__ == "__main__":
    input = sys.stdin.readline

    n = int(input())
    coins = list(map(int, input().split()))
    m = int(input())

    answer = float('inf')
    coins.sort(reverse=True)

    dfs(0, 0)
    print(answer)
