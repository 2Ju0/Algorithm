if __name__ == "__main__":
    n = int(input())
    ans = 'abcdefghijklmnopqrstuvwxyz'

    for i in range(1, n + 1):
        str = input()
        answer = 0
        for j in range(len(str)):
            if str[j] != ans[j]:
                break
            answer += 1
        print("#%d %d" % (i, answer))
