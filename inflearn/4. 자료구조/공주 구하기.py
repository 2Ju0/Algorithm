import sys
from collections import deque

if __name__ == "__main__":
    input = sys.stdin.readline

    n, k = map(int, input().split())
    que = deque(i for i in range(1, n + 1))

    cnt = 0
    while len(que) != 1:
        cnt += 1
        v = que.popleft()
        if cnt != k:
            que.append(v)
        else:
            cnt = 0

    print(que.pop())
