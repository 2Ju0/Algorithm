import sys


def dfs(cnt, score, time):
    global answer

    if time > m:
        return
    if cnt == n:
        if answer < score:
            answer = score
            return
    else:
        dfs(cnt + 1, score + arr[cnt][0], time + arr[cnt][1])
        dfs(cnt + 1, score, time)


if __name__ == "__main__":
    input = sys.stdin.readline

    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    arr.sort(reverse=True)
    answer = 0

    dfs(0, 0, 0)
    print(answer)
