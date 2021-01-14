/*
�ؽ�-����
<��� Ǯ���°�?>
 �ٷ� �� �������� ���� ���� ������ Ȱ���Ͽ� ���� �ٸ� �ǻ��� �̸��� key�� ������ value�� ������ clothMap�̶�� unordered_map ������ �����Ѵ�. 
 �ǻ��� ������ �ٸ� ��� �̸��� ������ �ϳ��� ���� �� �ְų� �ƿ� ���� �� ����. 
 ��, �� �ǻ��� ������ '������ ������ �̸��� �ٸ� ����+1'������ ������ �� �� �ִ� ���̴�. 
 �� ������ �� �ǻ󸶴� �Ѵٰ� ġ��, (a+1)*(b+1)*(c+1)... �̷� ���� �ȴ�. 
 �̷��� ����� �� �ƹ��͵� ���� �ʴ� ��츦 ���ָ� �츮�� ã�� ���̴�
*/
#include <string>
#include <vector>
#include <unordered_map>

using namespace std;

int solution(vector<vector<string>> clothes) {

    int answer = 1;
    unordered_map<string, int> clothMap;

    for (int i = 0; i < clothes.size(); i++)
    {
        string clo = clothes[i][1];
        if (clothMap.end() == clothMap.find(clo))
            clothMap.insert(make_pair(clo, 1));
        else
        {
            clothMap[clo]++;
        }
    }

    unordered_map<string, int>::iterator it;
    for (it = clothMap.begin(); it != clothMap.end(); it++)
    {
        answer *= (it->second) + 1;
    }
    return answer - 1;
}