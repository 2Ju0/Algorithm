import sys
import heapq as hq

if __name__ == "__main__":
    input = sys.stdin.readline

    heap = []
    while True:
        n = int(input())
        if n == -1:
            break
        elif n == 0:
            if len(heap) != 0:
                print(hq.heappop(heap))
            else:
                print(-1)
        else:
            hq.heappush(heap, n)
