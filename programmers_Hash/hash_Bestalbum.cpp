/*
�ؽ�-����Ʈ�ٹ�
<��� Ǯ���°�?>
1. unordered_map �Լ��� ����Ͽ� genres�� ������ key�� ������ �ش� genre�� play ������ ���� value�� ������ map<string,int>�� �����.
2. map�� �������� ������ �����Ƿ� genreMap�� ������ vector<pair<int,string>> ������ vec�� ������� ���� algorithm ���̺귯���� sort �Լ��� �̿��Ͽ� �����Ѵ�. ���⼭ int�� string�� ������ �ڹٲ�� ������ play ������ ���� �������� �����ؾ��ϱ� �����̴�.
3. ������ �Ǿ��ٸ� ���� play ������ ���� �ʿ����. vector<pair<int,string>>�� string ���� plays ����� ���ĵǾ� �ִ� �������״� �ε��� ������� vector<string> ������ vec2���� ��´�.
4. vector<pair<int,int>> ������ list_sameGenre�� �����Ѵ�. �׸��� vec�� ũ��(���� �ٸ� �帣�� ����)��ŭ�� ���� �ȿ� genres�� ũ�⸸ŭ�� ������ ���� genreMap�� key���� genres�� ���� ��ġ�� ������ list_sameGenre�� pair�� <plays[�ش� �ε���], �־��� genres�� ũ�⿡�� ������ȣ �� ��>�� �ִ´�. ���⼭ ������ ���� pair�� �ι�° ���� ������ȣ�� �ƴ� �־��� genres�� ũ�⿡�� �� ���̾�� �Ѵٴ� ���̴�. �ֳ��ϸ�  ����Ʈ���� ������� ����, ������ȣ�� �������� �տ� ���ϵǱ� �����̴�. �״�� ������ȣ ���� ������ ���� ó��������ؼ� ����������. �־��� genres�� ũ�⿡�� �� ��� ������ȣ�� Ŭ���� �۾����� �������� Ŀ����.
5. list_sameGenre�� ������ �� ���� �ڿ� �ִ� �� (�ش� �帣 �߿��� ���� ���� �����)�� ������ȣ�� result ���� �߰��Ѵ�. �̸�  list_sameGenre�� �ʱ�ȭ�ذ��� ���� �ٸ� �帣�� ������ŭ �ݺ��Ѵ�.
�⺻���� �ڵ� ���ư��� ����� �̷���. �Ϻ� �Լ��� ��������� ���̱� ������ �տ��� ������ ������ �ڿ��� ������ �����ؾ� �Ѵ�.
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
