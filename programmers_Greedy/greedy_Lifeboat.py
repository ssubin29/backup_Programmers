# 탐욕법 - 구명보트

def solution(people, limit):
    answer = 0
    peoples_r =  people.copy()
    peoples =  people.copy()

    peoples_r.sort(reverse=True)
    peoples.sort()
    
    print(peoples_r)
    print(peoples)
    print(list(enumerate(people)))
    
    weight = 0
    while(people):
        weight = peoples_r[0]
        people.remove(weight)
        peoples.remove(weight)
        peoples_r.remove(weight)
        while(weight <= limit):
            #for people
        
    return answer