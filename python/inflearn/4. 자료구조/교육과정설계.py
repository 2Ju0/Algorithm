import sys
from collections import deque

if __name__ == "__main__":
    input = sys.stdin.readline

    mandatory = input().strip()
    n = int(input())

    for i in range(n):
        plan = input()
        dq = deque(mandatory)
        is_right = True

        for v in plan:
            if v in dq and dq.popleft() != v:
                print("#%d NO" % (i + 1))
                is_right = False
                break

        else:
            if dq:
                print("#%d NO" % (i + 1))
            else:
                print("#%d YES" % (i + 1))
