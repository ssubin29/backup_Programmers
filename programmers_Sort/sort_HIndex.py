# H-index

def solution(citations):
    answer = 0
    
    citations.sort(reverse=True)
    print(citations)
    
    i=0
    for i in range(1,len(citations)): # i는 1부터 len(citations)-1까지
        if i <= citations[i-1]:
            answer = answer + 1
        else :
            i = i - 1
            break
    if i+1 == len(citations):
        answer = answer + 1
    return answer