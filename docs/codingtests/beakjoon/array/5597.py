# https://www.acmicpc.net/problem/5597

# 문제
# X대학 M교수님은 프로그래밍 수업을 맡고 있다. 교실엔 학생이 30명이 있는데, 학생 명부엔 각 학생별로 1번부터 30번까지 출석번호가 붙어 있다.

# 교수님이 내준 특별과제를 28명이 제출했는데, 그 중에서 제출 안 한 학생 2명의 출석번호를 구하는 프로그램을 작성하시오.

# 입력
# 입력은 총 28줄로 각 제출자(학생)의 출석번호 n(1 ≤ n ≤ 30)가 한 줄에 하나씩 주어진다. 출석번호에 중복은 없다.

# 출력
# 출력은 2줄이다. 1번째 줄엔 제출하지 않은 학생의 출석번호 중 가장 작은 것을 출력하고, 2번째 줄에선 그 다음 출석번호를 출력한다.
'''
fullclass = []
for i in range(30):
    fullclass.append(i+1)
    pass

inputclass=[]
for j in range(28):
    inputclass.append(int(input()))
    pass

for k in range(30):
    for l in range(28):
     if fullclass[k] == inputclass[l]:
        fullclass[k]=0
        pass
     pass
    pass
fullclass.sort(reverse=True)

print(fullclass[1])
print(fullclass[0])

'''

def name_check():
    student_list = list(i+1 for i in range(30))
    result=[]

    for i in range(28):
        get_num = int(input())
        result.append(get_num)
        pass

    for i in range(len(student_list)):
        if student_list[i] not in result:
            answer = student_list[i]
            print(answer)
            pass
        pass
    return

name_check()        