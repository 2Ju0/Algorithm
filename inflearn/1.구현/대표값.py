import sys

if __name__ == "__main__":
    input = sys.stdin.readline

    n = int(input())
    scores = list(map(int, input().split()))

    average = round(sum(scores) / len(scores))
    abs_score = 100
    student_num = 0

    for i in range(n):
        score = scores[i]
        tmp = score - average

        if 0 <= tmp < abs_score:
            abs_score = tmp
            student_num = i + 1

    print(average, student_num)

