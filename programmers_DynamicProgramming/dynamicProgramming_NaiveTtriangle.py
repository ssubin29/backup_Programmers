# 동적계획법 - 정수 삼각형

def solution(triangle):
    
    dp = [[0,0]] + [[0] + triangle[i] +[0] for i in range(len(triangle))]
    for i in range(1, len(triangle)+1):
        for j in range(1, i+1):
            dp[i][j] = dp[i][j] + max(dp[i-1][j-1], dp[i-1][j]) 
    print(dp)

    return max(dp[-1])