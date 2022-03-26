# 탐욕법 - 체육복

def solution(n, lost, reserve):
    answer = 0    
    
    student = [1 for i in range(n)]
    for i in range(n):  
        if i+1 in lost:
            student[i] = student[i] - 1
        if i+1 in reserve:
            student[i] = student[i] + 1
    #print('처음 : ', student)
    
    for i in range(n):
        if i == 0:
            if(student[i] == 2) and (student[i+1]==0):
                student[i+1] = 1
                student[i] = 1
        elif i == n-1:
             if(student[i] == 2) and (student[i-1]==0):
                student[i-1] = 1
                student[i] = 1
        else:
            if(student[i] == 2) and (student[i-1]==0):
                student[i-1] = 1
                student[i] = 1
            elif(student[i] == 2) and (student[i+1]==0):
                student[i+1] = 1
                student[i] = 1
    
    #print('나눠준 후 : ', student)
            
    for stu in student:
        if stu > 0 :
            answer = answer + 1
    
    return answer