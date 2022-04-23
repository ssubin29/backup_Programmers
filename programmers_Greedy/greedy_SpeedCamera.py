# 탐욕법 - 단속카메라

def solution(routes):
    answer = 0
    
    routes = sorted(routes, key=lambda x : x[1])
    start = -30000
    for route in routes:
        if(start < route[0]):
            answer = answer + 1
            start = route[1]
    
    return answer