def solution(clothes):
    answer = 1
    clothes_count = {}
    
    for cloth in clothes:
        if (cloth[1] not in clothes_count.keys()):
            clothes_count[cloth[1]] = 1
        else :
            clothes_count[cloth[1]] = clothes_count[cloth[1]] + 1
            
    for n in clothes_count.values():
        answer = answer * (n+1)
        
    return answer-1