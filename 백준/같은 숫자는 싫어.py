def solution(arr):
    answer = []
    cur = ''
    for item in arr:
        if not cur == item:
            cur = item
            answer.append(item)
    return answer