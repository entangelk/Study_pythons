# https://school.programmers.co.kr/learn/courses/30/lessons/42862

# 체육복
# 문제 설명
# 점심시간에 도둑이 들어, 일부 학생이 체육복을 도난당했습니다. 다행히 여벌 체육복이 있는 학생이 이들에게 체육복을 빌려주려 합니다. 학생들의 번호는 체격 순으로 매겨져 있어, 바로 앞번호의 학생이나 바로 뒷번호의 학생에게만 체육복을 빌려줄 수 있습니다. 예를 들어, 4번 학생은 3번 학생이나 5번 학생에게만 체육복을 빌려줄 수 있습니다. 체육복이 없으면 수업을 들을 수 없기 때문에 체육복을 적절히 빌려 최대한 많은 학생이 체육수업을 들어야 합니다.

# 전체 학생의 수 n, 체육복을 도난당한 학생들의 번호가 담긴 배열 lost, 여벌의 체육복을 가져온 학생들의 번호가 담긴 배열 reserve가 매개변수로 주어질 때, 체육수업을 들을 수 있는 학생의 최댓값을 return 하도록 solution 함수를 작성해주세요.

# 제한사항
# 전체 학생의 수는 2명 이상 30명 이하입니다.
# 체육복을 도난당한 학생의 수는 1명 이상 n명 이하이고 중복되는 번호는 없습니다.
# 여벌의 체육복을 가져온 학생의 수는 1명 이상 n명 이하이고 중복되는 번호는 없습니다.
# 여벌 체육복이 있는 학생만 다른 학생에게 체육복을 빌려줄 수 있습니다.
# 여벌 체육복을 가져온 학생이 체육복을 도난당했을 수 있습니다. 이때 이 학생은 체육복을 하나만 도난당했다고 가정하며, 남은 체육복이 하나이기에 다른 학생에게는 체육복을 빌려줄 수 없습니다.
# 입출력 예
# n	lost	reserve	return
# 5	[2, 4]	[1, 3, 5]	5
# 5	[2, 4]	[3]	4
# 3	[3]	[1]	2
# 입출력 예 설명
# 예제 #1
# 1번 학생이 2번 학생에게 체육복을 빌려주고, 3번 학생이나 5번 학생이 4번 학생에게 체육복을 빌려주면 학생 5명이 체육수업을 들을 수 있습니다.

# 예제 #2
# 3번 학생이 2번 학생이나 4번 학생에게 체육복을 빌려주면 학생 4명이 체육수업을 들을 수 있습니다.

def solution(n, lost, reserve):
    lost_list = sorted(lost)
    reserve_list = sorted(reserve)

    rese_dic = {i:True for i in reserve_list}
    lost_dic = {i:False for i in lost_list}



    for i in lost_dic:
        if rese_dic.get(i,False):
            rese_dic[i] = False
            lost_dic[i] = True
            
    for i in lost_dic:
        if i == 1:
            if rese_dic.get(i+1,False):
                rese_dic[i+1] = False
                lost_dic[i] = True
        else:
            if rese_dic.get(i-1,False):
                rese_dic[i-1] = False
                lost_dic[i] = True
            elif rese_dic.get(i+1,False):
                rese_dic[i+1] = False
                lost_dic[i] = True
    answer = n

    for i in range(n):
        if not lost_dic.get(i+1,True):
            answer -= 1

    return answer

solution(5, [4,2], [5,3])

# Test case 1: minimum input values
print(solution(2, [1], [2]))  # Expected output: 2

# Test case 2: all students lost gym suits and all students have extra gym suits
print(solution(5, [1, 2, 3, 4, 5], [1, 2, 3, 4, 5]))  # Expected output: 5

# Test case 3: one student lost a gym suit and the same student has an extra gym suit
print(solution(5, [3], [3]))  # Expected output: 5

# Test case 4: all students lost gym suits and one student has extra gym suits
print(solution(5, [1, 2, 3, 4, 5], [3]))  # Expected output: 1

# Test case 5: one student lost a gym suit and all students have extra gym suits
print(solution(5, [3], [1, 2, 3, 4, 5]))  # Expected output: 5

# Test case 6: random case with no overlapping between lost and reserve
print(solution(5, [2, 4], [1, 3, 5]))  # Expected output: 5

# Test case 7: random case with overlapping between lost and reserve
print(solution(5, [2, 4], [3, 4]))  # Expected output:  5

# Test case 8: all students lost gym suits and no student has extra gym suits
print(solution(5, [1, 2, 3, 4, 5], []))  # Expected output: 0

# Test case 9: no student lost a gym suit and all students have extra gym suits
print(solution(5, [], [1, 2, 3, 4, 5]))  # Expected output: 5

# Test case 10: maximum input values
print(solution(30, [i for i in range(1, 31)], [30]))  # Expected output: 1
