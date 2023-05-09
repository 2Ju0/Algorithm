import sys


def dfs(cnt):
    global total

    if cnt == m:
        total += 1
        print(' '.join([str(i) for i in answer]))
        return
    else:
        for i in range(1, n + 1):
            if not visited[i]:
                # new_visited = copy.deepcopy(visited) # tail recursion
                visited[i] = 1
                answer[cnt] = i
                dfs(cnt + 1)
                visited[i] = 0


if __name__ == "__main__":
    input = sys.stdin.readline

    n, m = map(int, input().split())
    visited = [0] * (n + 1)
    answer = [0] * m
    total = 0

    dfs(0)
    print(total)
