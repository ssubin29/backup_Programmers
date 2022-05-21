# 동적계획법 - N으로 표현

def solution(N, number):
    dp = []
    
    for i in range(1, 9):
        numbers = set()
        numbers.add(int(i*str(N)))
        #print(numbers)
        
        for j in range(i-1):
            for x in dp[j]:
                for y in dp[i-j-2]:
                    numbers.add(x+y)
                    numbers.add(x*y)
                    numbers.add(x-y)
                    if y != 0:
                        numbers.add(x//y)
        print(numbers)
        if number in numbers:
            return i
        
        dp.append(numbers)
        #print(dp)
    
    return -1
print(solution(5,	12))