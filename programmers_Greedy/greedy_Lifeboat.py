# 탐욕법 - 구명보트

def solution(people, limit): # 효율성 0점
    answer = 0
    peoples_r =  people.copy()
    peoples =  people.copy()

    peoples_r.sort(reverse=True)
    peoples.sort()
    
    
    weight = 0
    while(people):
        weight = peoples_r[0]
        answer = answer + 1
        people.remove(weight)
        peoples.remove(weight)
        peoples_r.remove(weight)
        for p in peoples:
            if(weight + p > limit):
                break
            else:
                weight = weight + peoples[0]
                people.remove(peoples[0])
                peoples_r.remove(peoples[0])
                peoples.remove(peoples[0])
        
    return answer