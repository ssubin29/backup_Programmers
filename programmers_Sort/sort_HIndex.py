# 정렬 - H-index

def solution(citations):
    answer = 0
    
    citations.sort(reverse=True)
    
    for i in range(1,len(citations)+1): # i는 1부터 len(citations)-1까지
        if i <= citations[i-1]:
            answer += 1
        else :
            break
        
    return answer