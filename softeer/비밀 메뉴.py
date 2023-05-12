import sys


if __name__ == "__main__":
    input = sys.stdin.readline

    m, n, k = map(int, input().split())
    menu = list(map(int, input().split()))
    user = list(map(int, input().split()))

    if len(user) < len(menu):
        print('normal')
        sys.exit(0)

    for i in range(n):
        if user[i] == menu[0]:
            for j in range(1, m):
                if n <= i + j:
                    break
                if n > i + j and user[i + j] != menu[j]:
                    break
            else:
                print('secret')
                sys.exit(0)

    print('normal')
