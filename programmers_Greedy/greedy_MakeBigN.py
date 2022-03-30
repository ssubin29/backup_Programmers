## 탐욕법 - 큰 수 만들기

import itertools

def solution_time(number, k): #시간 초과
    answer = ''
    
    orders = list(map(''.join, itertools.combinations(number,len(number)-k)))
    answer = max(orders)
    return answer


def solution_missed(number, k): #아예 잘못 품
    answer = ''
    
    number = list(number)
    numbers = list(enumerate(number))
    
    numbers_sorted = sorted(numbers, key=lambda x : x[1])
    for n in numbers_sorted:
        if k > 0 :
            number.remove(n[1])
            k = k - 1
        else :
            break
            
    answer = ''.join(number)
    return answer