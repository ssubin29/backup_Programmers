# 가장 큰 수

def solution(numbers):
    answer = ''
    
    strings = list(map(str, numbers))
    strings.sort(reverse = True)
    
    print(strings)
    return answer