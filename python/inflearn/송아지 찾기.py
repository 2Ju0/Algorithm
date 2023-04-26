import sys
from collections import deque

if __name__ == "__main__":
    s, e = map(int, sys.stdin.readline().split())

    MAX = 10000
    dis = [0] * (MAX + 1)
    visited = [0] * (MAX + 1)

    visited[s] = 1
    dis[s] = 0

    dQ = deque()
    dQ.append(s)

    while dQ:
        now = dQ.pop()

        if now == e:
            break

        for next in (now - 1, now + 1, now + 5):
            if 0 < next <= MAX:
                if not visited[next]:
                    dQ.append(next)
                    visited[next] = 1
                    dis[next] = dis[now] + 1

print(dis[e])
