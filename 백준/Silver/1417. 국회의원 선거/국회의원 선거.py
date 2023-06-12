import sys

if __name__ == '__main__':
    input = sys.stdin.readline
    n = int(input())
    winner = int(input())
    votes = [int(input()) for _ in range(n - 1)]
    answer = 0

    votes.sort(reverse=True)

    if n == 1:
        print(0)
    else:
        while votes[0] >= winner:
            winner += 1
            votes[0] -= 1
            answer += 1
            votes.sort(reverse=True)

        print(answer)
