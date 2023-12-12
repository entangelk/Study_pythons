# https://www.acmicpc.net/problem/1316

# 문제
# 그룹 단어란 단어에 존재하는 모든 문자에 대해서, 각 문자가 연속해서 나타나는 경우만을 말한다. 예를 들면, ccazzzzbb는 c, a, z, b가 모두 연속해서 나타나고, kin도 k, i, n이 연속해서 나타나기 때문에 그룹 단어이지만, aabbbccb는 b가 떨어져서 나타나기 때문에 그룹 단어가 아니다.

# 단어 N개를 입력으로 받아 그룹 단어의 개수를 출력하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 단어의 개수 N이 들어온다. N은 100보다 작거나 같은 자연수이다. 둘째 줄부터 N개의 줄에 단어가 들어온다. 단어는 알파벳 소문자로만 되어있고 중복되지 않으며, 길이는 최대 100이다.

# 출력
# 첫째 줄에 그룹 단어의 개수를 출력한다.

get_num = int(input())
group_word_count = 0

for _ in range(get_num):
    word = input()
    is_group_word = True
    for i in range(len(word) - 1):  # 각 문자를 순회하면서
        if word[i] != word[i + 1]:  # 현재 문자와 다음 문자가 다르다면
            if word[i] in word[i + 1:]:  # 현재 문자가 뒤에 또 나온다면 그룹 단어가 아닙니다. !!!!!!! [i+1:] 현재 단어 바로 뒤에서부터 끝까지 검사하는 키워드
                is_group_word = False
                break
    if is_group_word:  # 그룹 단어라면 count를 증가시킵니다.
        group_word_count += 1

print(group_word_count)

'''
get_num = int(input())
full_count=0

temp_list=[]
count_list=[]
for i in range(get_num):
    char = input()
    for j in range(len(char)):
        count_list.append(char.count(char[j]))
        temp_list.append(char.index(char[j]))
        pass
    for j in range(len(char)):
        if j < (len(char)-1):
            if j == 1:
                full_count += 1
            elif count_list[j] >= 2:
                if char[temp_list[j]] == char[temp_list[j]+count_list[j]-1]:
                    full_count += 1
                    pass
                pass
            pass
    pass


print(full_count)
'''

'''
문자열 내 알파벳의 각각 갯수를 리스트에 저장 끗
문자열 내 알파뱃의 첫번째 인덱스 추출 이거 끗
문자열 알파벳의 갯수를 인덱스로 사용해서 첫번째 인덱스 추출값과 비교
그 값이 서로 동일하지 않다면, 연속해서 나타나는 알파벳 아님
카운팅 -1
'''