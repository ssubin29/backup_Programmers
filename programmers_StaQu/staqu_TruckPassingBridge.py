# 스택/큐 - 다리를 지나는 트럭

def solution(bridge_length, weight, truck_weights):
    answer = 0
    
    count = 0
    bridge_weights = 0
    
    while(truck_weights):
        bridge_weights += truck_weights.pop(0)
        if bridge_weights >= weight:
            count = count + 1
    
    return answer