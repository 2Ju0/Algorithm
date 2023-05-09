"""
효율성 검사 위해
재귀 -> 반복
리스트 -> 힙
"""

from heapq import heapify, heappop, heappush


def is_less_than_scoville(scoville, K):
    for i in range(len(scoville)):
        if scoville[i] < K:
            return True
    return False


def solution(scoville, K):
    answer = 0
    heapify(scoville)

    while 1:
        if is_less_than_scoville(scoville, K):
            if len(scoville) < 2:
                return -1
            answer += 1
            new_food = heappop(scoville) + (heappop(scoville) * 2)
            heappush(scoville, new_food)
        else:
            return answer
