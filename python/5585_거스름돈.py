import sys

if __name__ == "__main__":
    coins = [500, 100, 50, 10, 5, 1]
    money = 1000 - int(sys.stdin.readline())
    cnt = 0

    for coin in coins:
        if money // coin > 0:
            cnt += money // coin
            money %= coin
            if money == 0:
                break

    print(cnt)
