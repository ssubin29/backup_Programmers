# 탐욕법 - 체육복

def solution(n, lost, reserve):
    
    index = [i+1 for i in range(n)]
    count = [0 for i in range(n)]
    wear = count
    
    
    # lost에 속한 reserve 제외
    available = reserve
    for l in lost:
        for r in reserve:
            if (l==r) : available.remove(l); lost.remove(l);
    
    # 현재 한 학생이 가지고 있는 옷 개수 세기
    for i in index:
        if(i in lost) : count[i-1]=0
        elif(i in available) : count[i-1]=2
        else : count[i-1]=1
    print(count)
    
    if (count[0]==2):
        count[1]=1; count[0]=1;
    print(count[n-2])
    if (count[n-1]==2):
        count[n-2]=1; count[n-1]=1;
    for i in index[:n-1]:
        if (count[i-1]==0) :
            if (count[i]!=0) : 
                count[i-1]=count[i-1]+1
                count[i]=count[i]-1
    
    
    print(count)
    for i in range(n):
        if(count[i]>=1):
            if(count[i]==2 and i>0):
                if(count[i-1]==0): count[i-1]=1; wear[i-1]=1;
            if(count[i]==2 and i<n):
                if(count[i+1]==0): count[i+1]=1; wear[i+1]=1; 
            wear[i]=1
    print(wear)       
    answer = sum(wear)
    return answer