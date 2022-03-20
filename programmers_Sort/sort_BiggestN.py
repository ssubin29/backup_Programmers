# 가장 큰 수

def solution(numbers):
    answer = ''    
    strings = list(map(str, numbers))
    for n in range(len(strings)):
        strings[n] = '0'*(4-len(strings[n])) + strings[n]
    strings.sort(reverse=True)
    print(strings)
    return answer


def solution2(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x * 3, reverse=True)
    # num 인자 각각의 문자열을 3번 반복한 것을 오름차순 정렬한다
    print(numbers)
    return str(int(''.join(numbers)))
       