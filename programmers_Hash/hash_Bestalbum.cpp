/*
해시-베스트앨범
<어떻게 풀었는가?>
1. unordered_map 함수를 사용하여 genres의 값들을 key로 가지고 해당 genre의 play 값들의 합을 value로 가지는 map<string,int>를 만든다.
2. map은 오름차순 정렬이 어려우므로 genreMap의 값들을 vector<pair<int,string>> 형태인 vec에 집어넣은 다음 algorithm 라이브러리의 sort 함수를 이용하여 정렬한다. 여기서 int와 string의 순서가 뒤바뀌는 이유는 play 값들의 합을 기준으로 정렬해야하기 때문이다.
3. 정렬이 되었다면 이제 play 값들의 합은 필요없다. vector<pair<int,string>>의 string 값은 plays 값들로 정렬되어 있는 상태일테니 인덱스 순서대로 vector<string> 형태의 vec2값에 담는다.
4. vector<pair<int,int>> 형태의 list_sameGenre를 선언한다. 그리고 vec의 크기(서로 다른 장르의 개수)만큼의 루프 안에 genres의 크기만큼의 루프를 돌려 genreMap의 key값과 genres의 값이 일치할 때마다 list_sameGenre의 pair에 <plays[해당 인덱스], 주어진 genres의 크기에서 고유번호 뺀 값>을 넣는다. 여기서 주의할 점은 pair의 두번째 값이 고유번호가 아닌 주어진 genres의 크기에서 뺀 값이어야 한다는 점이다. 왜냐하면  베스트음악 재생수가 높고, 고유번호가 낮을수록 앞에 수록되기 때문이다. 그대로 고유번호 값을 넣으면 따로 처리해줘야해서 귀찮아진다. 주어진 genres의 크기에서 뺄 경우 고유번호가 클수록 작아지고 작을수록 커진다.
5. list_sameGenre를 정렬한 후 가장 뒤에 있는 값 (해당 장르 중에서 가장 많이 재생됨)의 고유번호를 result 값에 추가한다. 이를  list_sameGenre을 초기화해가며 서로 다른 장르의 개수만큼 반복한다.
기본적인 코드 돌아가는 방식은 이렇다. 일부 함수는 선입후출로 쌓이기 때문에 앞에서 루프를 돌릴지 뒤에서 돌릴지 주의해야 한다.
*/

#include <string>
#include <vector>
#include <unordered_map>
#include <algorithm>

using namespace std;

vector<int> solution(vector<string> genres, vector<int> plays) {
    vector<int> answer;
    unordered_map <string, int> genreMap;
    const int& SIZE = genres.size();

    for (int i = 0; i < SIZE; i++)
    {
        if (genreMap.end() == genreMap.find(genres[i]))
            genreMap.insert(make_pair(genres[i], plays[i]));
        else
            genreMap[genres[i]] += plays[i];
    }
    vector<pair<int, string>> vec;
    unordered_map<string, int> ::iterator it;
    for (it = genreMap.begin(); it != genreMap.end(); it++)
    {
        vec.push_back(make_pair(it->second, it->first));
    }

    sort(vec.begin(), vec.end());

    const int& GenreKind = vec.size();
    vector<string> vec2;
    for (int i = 0; i < GenreKind; i++)
    {
        vec2.push_back(vec[i].second);
    }

    vector <pair<int, int>> list_sameGenre;
    for (int i = (GenreKind - 1); i >= 0; i--)
    {
        for (int j = 0; j < SIZE; j++)
        {
            if (genres[j] == vec2[i])
            {
                list_sameGenre.push_back(make_pair(plays[j], SIZE - j));
                genreMap[genres[j]] -= plays[j];
                if (!(genreMap[genres[j]])) { break; }
            }
        }

        sort(list_sameGenre.begin(), list_sameGenre.end());
        int s = list_sameGenre.size();
        answer.push_back(SIZE - list_sameGenre[s - 1].second);
        if (s != 1)
        {
            answer.push_back(SIZE - list_sameGenre[s - 2].second);
        }
        list_sameGenre.clear();
    }
    return answer;
}
