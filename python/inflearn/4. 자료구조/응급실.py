import sys
from collections import deque

if __name__ == "__main__":
    input = sys.stdin.readline

    n, m = map(int, input().split())
    dq = deque((k, v) for k, v in enumerate(list(map(int, input().split()))))
    cnt = 0

    while dq:
        v = dq.popleft()
        if any(v[1] < x[1] for x in dq):
            dq.append(v)
        else:
            cnt += 1
            if v[0] == m:
                print(cnt)
                break
