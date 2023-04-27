def solution(numbers):
    numbers = list(map(str, numbers))
    m_length = max([len(n) for n in numbers])
    numbers.sort(key=lambda x: x*(m_length), reverse=True)
    return str(int(''.join(numbers)))