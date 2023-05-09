import sys
from collections import deque


if __name__ == "__main__":
    input = sys.stdin.readline

    s, e = map(int, input().split())

    MAX = 10000
    visited = [0] * (MAX + 1)
    dis = [0] * (MAX + 1)
    dis[s] = 0

    que = deque([s])
    while que:
        now = que.popleft()

        if now == e:
            break

        for next in (now - 1, now + 1, now + 5):
            if 1 <= next <= MAX and not visited[next]:
                que.append(next)
                visited[next] = 1
                dis[next] = dis[now] + 1

    print(dis[e])
