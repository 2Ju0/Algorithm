import sys
import copy


def dfs(cnt, visited):
    global total

    if cnt == m:
        total += 1
        print(' '.join([str(num) for num in result]))
    else:
        for i in range(1, n + 1):
            if not visited[i]:
                new_visited = copy.deepcopy(visited)
                new_visited[i] = 1
                result[cnt] = i
                dfs(cnt + 1, new_visited)
                # visited[i] = 0  # 대칭구조!


if __name__ == "__main__":
    n, m = map(int, sys.stdin.readline().split())
    visited = [0] * (n + 1)
    result = [0] * m
    total = 0
    dfs(0, visited)

    print(total)
