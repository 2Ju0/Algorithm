import sys


if __name__ == "__main__":
    input = sys.stdin.readline

    v, e = map(int, input().split())

    graph = [[0] * v for _ in range(v)]

    for _ in range(e):
        start, end, weight = map(int, input().split())
        graph[start - 1][end - 1] = weight

    for line in graph:
        print(' '.join(str(v) for v in line))
