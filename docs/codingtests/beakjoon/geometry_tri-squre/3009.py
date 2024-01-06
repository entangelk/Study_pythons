# https://www.acmicpc.net/problem/3009

# 문제
# 세 점이 주어졌을 때, 축에 평행한 직사각형을 만들기 위해서 필요한 네 번째 점을 찾는 프로그램을 작성하시오.

# 입력
# 세 점의 좌표가 한 줄에 하나씩 주어진다. 좌표는 1보다 크거나 같고, 1000보다 작거나 같은 정수이다.

# 출력
# 직사각형의 네 번째 점의 좌표를 출력한다.

def solution():
    set_list=[]
    get_list=[]
    answer_list=[]
    for i in range(3):
        a,b = map(int,input().split())
        set_list.append(a)
        get_list.append(b)
        set_list.sort()
        get_list.sort()

    if set_list.count(set_list[0]) == 2:
        answer_list.append(str(set_list[-1]))
    else:
        answer_list.append(str(set_list[0]))

    if get_list.count(get_list[0]) == 2:
        answer_list.append(str(get_list[-1]))
    else:
        answer_list.append(str(get_list[0]))
    answer = ' '.join(answer_list)
    return answer
    
print(solution())
