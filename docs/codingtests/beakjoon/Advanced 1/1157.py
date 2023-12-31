# https://www.acmicpc.net/problem/1157

# 문제
# 알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오. 단, 대문자와 소문자를 구분하지 않는다.

# 입력
# 첫째 줄에 알파벳 대소문자로 이루어진 단어가 주어진다. 주어지는 단어의 길이는 1,000,000을 넘지 않는다.

# 출력
# 첫째 줄에 이 단어에서 가장 많이 사용된 알파벳을 대문자로 출력한다. 단, 가장 많이 사용된 알파벳이 여러 개 존재하는 경우에는 ?를 출력한다.
'''
import sys


char = sys.stdin.readline()
char.upper()
count=[0]*len(char)

for i in range(len(char)):
    for j in range(i+1,len(char)):
        if char[i] == char[j]:
            count[i] += 1
            pass
        else :
            pass
    pass

temp=list(count)
count.sort(reverse=True)
# count.sort(reverse=True)
if len(char) == 1:
    answer = char[temp.index(count[0])]
    print(answer.upper())
    pass
elif count[0] == count[1]:
    print("?")
    pass
else:
    answer = char[temp.index(count[0])]
    print(answer.upper())
    pass
    
    '''
'''
import sys

char = sys.stdin.readline().rstrip().upper()  # 개행 문자 제거 및 대문자로 변환
count = [0] * 26  # 알파벳 개수만큼의 리스트 생성

for i in range(len(char)):
    count[ord(char[i]) - ord('A')] += 1  # 해당 알파벳의 등장 횟수 증가

max_count = max(count)

if count.count(max_count) > 1:
    print("?")
else:
    answer = chr(count.index(max_count) + ord('A'))
    print(answer)

주요 변경 사항:

sys.stdin.readline() 결과에 .rstrip()을 사용하여 개행 문자 제거 및 대문자로 변환을 한 번에 수행했습니다.
count 리스트의 크기를 26으로 고정하고 알파벳의 등장 횟수를 직접 해당 알파벳의 아스키 코드를 이용해 카운팅합니다.
count.index(max_count)를 사용하여 최댓값의 인덱스를 찾고, 이를 알파벳으로 변환하여 출력합니다.
count.count(max_count)를 사용하여 최댓값의 개수를 세고, 이를 이용해 중복 최댓값을 판별하고 출력합니다.

'''
'''
def count_char():
    get_char= input().upper()
    check_list=[]
    set_list = list(get_char[i] for i in range(len(get_char)))
    for i in range(len(set_list)):
        check_list.append(set_list.count(set_list[i]))
        pass
    if len(check_list) > 1:
        if len(set(sorted(check_list))) != len(set(sorted(set_list))):
            print("?")
            pass
        else : 
            print(set_list[check_list.index(max(check_list))])
    return

count_char()
'''
def count_char():
    get_char = input().upper()
    count_dict = {}  # 문자별 등장 횟수를 저장할 딕셔너리
    
    for char in get_char:
        if char.isalpha():  # 알파벳인 경우에만 카운트
            if char in count_dict:
                count_dict[char] += 1
            else:
                count_dict[char] = 1
    
    max_count = max(count_dict.values())  # 가장 많이 등장한 횟수
    
    max_chars = [char for char, count in count_dict.items() if count == max_count]  # 최빈 문자들
    
    if len(max_chars) == 1:  # 최빈 문자가 하나라면 해당 문자 출력
        print(max_chars[0])
    else:  # 최빈 문자가 여러 개라면 물음표 출력
        print("?")

count_char()