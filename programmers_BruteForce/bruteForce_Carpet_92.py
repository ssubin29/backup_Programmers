# 완전탐색 - 카펫

def solution(brown, yellow):
    answer = []
    
    # 중요한 건 테두리의 1줄만이 갈색이라는 점이다......
    # 예를 들어 갈색+노랑 부분이 m*n이라고 하고 노랑 부분이 a*b라고 하면 (가로*세로순이다)
    # b = m-2고 a = n-2 가 된다..... 이래야 목표하는 모양의 카펫이 되는거다...
    
    alll = brown + yellow
    
    all_available = []
    yellow_available = []
    
    alls_divisors = get_divisor(alll)
    yellows_divisors = get_divisor(yellow)
    
    for divisor in alls_divisors:
        a = alll // divisor
        if not a == alll:
            all_available.append([a,divisor])
            
    for divisor in yellows_divisors:
        a = yellow // divisor
        if not a < 3 or a == yellow:
            yellow_available.append([a,divisor])
            
    yellow_available.sort(reverse=True)
    
    for avail in yellow_available:
        if [avail[0]+2, avail[1]+2] in all_available:
            return [avail[0]+2, avail[1]+2]
    
    return answer


def get_divisor_simple(n):
    divisors = []
    for i in range(1, n + 1):
        if (n % i == 0):            
            divisors.append(i)        
    return divisors


def get_divisor(n):
    n = int(n)
    divisors = []
    divisors_back = [] 

    for i in range(1, int(n**(1/2)) + 1): 
        if (n % i == 0):            
            divisors.append(i)
            if (i != (n // i)): 
                divisors_back.append(n//i)

    return divisors + divisors_back[::-1]
