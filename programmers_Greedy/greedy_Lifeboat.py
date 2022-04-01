# 탐욕법 - 구명보트

def solution(people, limit): #성공
    count = 0
    
    people =  people.copy()
    people.sort(reverse=True)
    
    left, right = 0, len(people)-1
    while right >= left: # 한 루프당 보트 하나
        count += 1
        # case1) 보트를 둘이서 탈 수 있을 때
        if people[right] + people[left] <= limit: 
            left += 1 
            right -= 1
        # case2) 보트를 한 명만 탈 수 있을 때
        else: 
            left += 1 
        
    return count

def solution1(people, limit): #이시발보트는2명밖에못탄대시발
    count = 0
    
    peoples =  people.copy()
    peoples.sort(reverse=True)
    
    weight = 0
    while(peoples):
        count = count + 1
        weight = peoples[0]
        peoples.remove(weight)
        if (len(peoples) >= 1):
            if (limit >= weight + peoples[-1]):
                peoples.remove(peoples[-1])
    return count

def solution2(people, limit): # 효율성 0점
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

print(solution([70, 50, 80, 50],	100))