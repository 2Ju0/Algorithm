import sys


def dfs(cnt, score, time, tsum):
    global result

    if result > score + (total - tsum):
        return
    if time > m:
        return
    if cnt == n:
        if score > result:
            result = score
    else:
        new_score = info[cnt][0]
        new_time = info[cnt][1]
        dfs(cnt + 1, score + new_score, time + new_time, tsum + new_score)
        dfs(cnt + 1, score, time, tsum + new_score)


if __name__ == "__main__":
    input = sys.stdin.readline
    n, m = map(int, input().split())

    info = []
    total = 0
    result = 0

    for _ in range(n):
        tmp = list(map(int, input().split()))
        info.append(tmp)
        total += tmp[0]

    info.sort(reverse=True)

    dfs(0, 0, 0, 0)
    print(result)
