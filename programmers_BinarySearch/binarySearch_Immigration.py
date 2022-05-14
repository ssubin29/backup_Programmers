# 이분 탐색 - 입국심사

def solution(n, times):
    answer = 0
    times.sort()
    
    left = times[0]
    right = times[-1] * n
    #print(left, right)
    
    while left <= right:
        mid = (left+ right) // 2
        people = 0
        for time in times:
            # people 은 모든 심사관들이 mid 동안 심사한 사람의 수
            people += mid // time
            # times를 전부 돌지 않아도 mid 동안 n명 이상의 심사를 할 수 있다면 break
            if people >= n:
                break
        
        # 심사한 사람의 수가 심사 받아야할 사람의 수(n)보다 많거나 같은 경우
        if people >= n:
            answer = mid
            right = mid - 1 # 왼쪽을 검사
        # 심사한 사람의 수가 심사 받아야할 사람의 수(n)보다 적은 경우
        elif people < n:
            left = mid + 1 # 오른쪽을 검사
    
    return answer