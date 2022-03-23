# 완전탐색 - 모의고사

def solution(answers):
    first = [1, 2, 3, 4, 5]
    second = [2, 1, 2, 3, 2, 4, 2, 5]
    third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    cnt = [0,0,0]
    
    for i, answer in enumerate(answers):
        
        cnt[0] = cnt[0] + (answers[i]==first[i%5])
        cnt[1] = cnt[1] + (answers[i]==second[i%8])
        cnt[2] = cnt[2] + (answers[i]==third[i%10])
    
    #print(cnt)
    if (cnt[0]==cnt[1] and cnt[1]==cnt[2]) : submit = [1,2,3]    
    else : 
        max_ = cnt[cnt.index(max(cnt))]
        #print(max_)
        submit = []
        for i, c in enumerate(cnt):
            if(c == max_) : submit.append(i+1)
        submit = sorted(submit)
    return submit