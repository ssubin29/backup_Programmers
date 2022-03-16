# H-index

def solution(citations):
    answer = 0
    
    citations.sort()
    print(citations)
    
    for i in range(1,len(citations)-1):
        if i > citations[i-1]:
            answer = i+1
        else :
            break
            
    return answer