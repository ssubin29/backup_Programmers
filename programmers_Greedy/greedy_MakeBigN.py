## 탐욕법 - 큰 수 만들기

def solution(number, k):
    answer = [] # Stack
    
    for num in number:
        while k > 0 and answer and answer[-1] < num:
        # k가 0보다 크고 answer이 차 있고 (기본적인 조건)
        # answer의 제일 위 값이 num보다 작을 때
            answer.pop()
            k -= 1 
            # 방금 asnwer에서 pop한 수가 k개 제거해야 한다는 조건에 해당하는 수
        answer.append(num)
        
    return ''.join(answer[:len(answer) - k])

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