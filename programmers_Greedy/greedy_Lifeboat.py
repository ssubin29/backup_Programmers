# 탐욕법 - 구명보트

def solution(people, limit):
    answer = 0
    peoples_r =  people.copy()
    peoples =  people.copy()

    peoples_r.sort(reverse=True)
    peoples.sort()
    
    print(peoples_r)
    print(peoples)
        
    return answer