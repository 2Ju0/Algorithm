import sys

if __name__ == "__main__":
    input = sys.stdin.readline

    n, k = map(int, input().split())
    cards = list(map(int, input().split()))
    res = []

    for i in range(n):
        if i == n - 1:
            continue

        for j in range(i + 1, n):
            if j == n - 1:
                continue

            for l in range(j + 1, n):
                res.append(cards[i] + cards[j] + cards[l])

    res = list(set(res))
    res.sort(reverse=True)
    print(res[k - 1])
