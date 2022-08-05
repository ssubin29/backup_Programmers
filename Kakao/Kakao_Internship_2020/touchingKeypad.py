# 2020 카카오 인턴십 - 키패드 누르기

def solution(numbers, hand):
    answer = ''
    
    pos = []
    for num in numbers:
        p = (0,0)
        if num == 0:
            p = (3,1)
        else:
            p = (   num//3, num%3   )
        pos.append(p)
    print(pos)
    return answer