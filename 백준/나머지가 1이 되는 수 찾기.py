def solution(n):
    divisor_lst = []
    for i in range(2, n):
        if (n-1) % i == 0:
            divisor_lst.append(i)

    return divisor_lst[0]