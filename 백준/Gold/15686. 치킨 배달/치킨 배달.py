import sys


def combi(idx, arr):
    global chickens, combinations

    if len(arr) == m:
        combinations.append(arr)
        return
    for i in range(idx, len(chickens)):
        combi(i + 1, arr + [chickens[i]])


def get_chicken_dis(house, chickens):
    answer = float('inf')
    for chicken in chickens:
        answer = min(answer, abs(house[0] - chicken[0]) + abs(house[1] - chicken[1]))

    return answer


if __name__ == '__main__':
    input = sys.stdin.readline
    n, m = map(int, input().split())
    graph = []
    chickens = []
    houses = []
    combinations = []
    answer = float('inf')

    for i in range(n):
        row = list(map(int, input().split()))
        graph.append(row)
        for j in range(n):
            if row[j] == 1:
                houses.append((i, j))
            if row[j] == 2:
                chickens.append((i, j))

    combi(0, [])

    for combination in combinations:
        city_dis = 0
        for house in houses:
            chicken_dis = get_chicken_dis(house, combination)
            city_dis += chicken_dis

        answer = min(answer, city_dis)

    print(answer)
