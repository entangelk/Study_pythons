# https://www.acmicpc.net/problem/1764

# 문제
# 김진영이 듣도 못한 사람의 명단과, 보도 못한 사람의 명단이 주어질 때, 듣도 보도 못한 사람의 명단을 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 듣도 못한 사람의 수 N, 보도 못한 사람의 수 M이 주어진다. 이어서 둘째 줄부터 N개의 줄에 걸쳐 듣도 못한 사람의 이름과, N+2째 줄부터 보도 못한 사람의 이름이 순서대로 주어진다. 이름은 띄어쓰기 없이 알파벳 소문자로만 이루어지며, 그 길이는 20 이하이다. N, M은 500,000 이하의 자연수이다.

# 듣도 못한 사람의 명단에는 중복되는 이름이 없으며, 보도 못한 사람의 명단도 마찬가지이다.

# 출력
# 듣보잡의 수와 그 명단을 사전순으로 출력한다.

# 로직은 맞으나 시간초과
'''
def solution_check(num):
    get_list =[]
    for i in range(num):
        get_name = input()
        get_list.append(get_name)
    return get_list

def solution_answer(get_list,num):
    answer_list=[]
    for i in range(num):
        get_name = input()
        if get_name in get_list:
            answer_list.append(get_name)

    return answer_list

a,b = map(int, input().split())

get_list = solution_check(a)
answer_list = solution_answer(get_list,b)
print(len(answer_list))
for i in answer_list:
    print(i)
'''


def solution_check(num):
    get_dic ={}
    for i in range(num):
        get_name = input()
        get_dic[get_name] = True

    return get_dic

def solution_set_dic(get_dic,num):
    for i in range(num):
        get_name = input()
        if get_dic.get(get_name, False) == True:
            get_dic[get_name] = False

    return get_dic

def solution_answer(set_dic):
    answer_list =[]
    counter = 0
    for k,v in set_dic.items():
        if v == False:
            answer_list.append(k)
            counter += 1

    answer_list.sort()
    print(counter)
    for i in answer_list:
        print(i)

    return

a,b = map(int, input().split())

get_dic = solution_check(a)
set_dic = solution_set_dic(get_dic,b)
solution_answer(set_dic)