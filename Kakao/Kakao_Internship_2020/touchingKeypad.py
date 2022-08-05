# 2020 카카오 인턴십 - 키패드 누르기

# 
def solution(numbers, hand):
    answer = ''
    
    position = []
    for num in numbers:
        pos = (0,0)
        if num == 0:
            pos = (3,1)
        elif num%3 == 0:
            pos = (   (num//3)-1, 2  )
        else:
            pos = (   num//3, (num%3)-1   )
        position.append(pos)
    print(position)
    
    hands = {'right':0, 'left':1}
    hands_ = ["R","L"]
    
    curr_right = (3,2)
    curr_left = (3,0)
    for pos in position:
        r = abs(pos[0]-curr_right[0]) + abs(pos[1]-curr_right[1])
        l = abs(pos[0]-curr_left[0]) + abs(pos[1]-curr_left[1])
        
        if r == l:
            ans = hands_[hands[hand]]
        else :
            ans = hands_[l > r]
            
        if ans == "R": curr_right = pos
        elif ans == "L": curr_left = pos
        answer += ans
        
            
    
    return answer