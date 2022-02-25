def solution(genres, plays):
    answer = []
    play_count = {} # genre가 key, play의 총합이 value
    genre_count = {} # genre가 key (고유번호,play) 튜플이 value
    
    for i in range(len(plays)):
        
        if genres[i] not in play_count.keys():
            play_count[genres[i]]=plays[i]
            genre_count[genres[i]]=[(i,[plays[i]])]
        else:
            play_count[genres[i]]=play_count[genres[i]]+plays[i]
            genre_count[genres[i]].append((i,[plays[i]]))
            
            
    play_count = sorted(play_count.items(), 
                        key = lambda item: item[1], reverse = True)
    
     
    for key in play_count:
        # key[1]이 genre
        s_genre = genre_count[key[0]]
        print(s_genre.sort(key=lambda x: x[1], reverse = True))
        
        if len(s_genre) < 2:
            answer.append(s_genre[0][0])
        else:
            for i in range(2):
                answer.append(s_genre[i][0])
        
        print(s_genre)       
        
    
    return answer