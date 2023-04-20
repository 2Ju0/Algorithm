import sys

if __name__ == "__main__":
    input = sys.stdin.readline

    n = int(input())
    arr = []
    price = 0

    for _ in range(n):
        arr = list(map(int, input().split()))
        set_arr = list(set(arr))
        count = len(set_arr)
        tmp = 0

        if count == 3:  # 모두 다른 눈
            tmp = max(arr) * 100
        elif count == 1:  # 같은 눈 3개
            tmp = 10000 + (arr[0] * 1000)
        else:  # 같은 눈 2개
            for num in set_arr:
                if arr.count(num) == 2:
                    tmp = 1000 + (100 * num)
                    continue

        if tmp > price:
            price = tmp

    print(price)
