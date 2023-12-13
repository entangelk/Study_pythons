# https://www.acmicpc.net/problem/25206

# 문제
# 인하대학교 컴퓨터공학과를 졸업하기 위해서는, 전공평점이 3.3 이상이거나 졸업고사를 통과해야 한다. 그런데 아뿔싸, 치훈이는 깜빡하고 졸업고사를 응시하지 않았다는 사실을 깨달았다!

# 치훈이의 전공평점을 계산해주는 프로그램을 작성해보자.

# 전공평점은 전공과목별 (학점 × 과목평점)의 합을 학점의 총합으로 나눈 값이다.

# 인하대학교 컴퓨터공학과의 등급에 따른 과목평점은 다음 표와 같다.

# A+	4.5
# A0	4.0
# B+	3.5
# B0	3.0
# C+	2.5
# C0	2.0
# D+	1.5
# D0	1.0
# F	0.0
# P/F 과목의 경우 등급이 P또는 F로 표시되는데, 등급이 P인 과목은 계산에서 제외해야 한다.

# 과연 치훈이는 무사히 졸업할 수 있을까?

# 입력
# 20줄에 걸쳐 치훈이가 수강한 전공과목의 과목명, 학점, 등급이 공백으로 구분되어 주어진다.

# 출력
# 치훈이의 전공평점을 출력한다.

# 정답과의 절대오차 또는 상대오차가 
# \(10^{-4}\) 이하이면 정답으로 인정한다.

data_set = {
 'A+':	4.5,
 'A0':	4.0,
 'B+':	3.5,
 'B0':	3.0,
 'C+':	2.5,
 'C0':	2.0,
 'D+':	1.5,
 'D0':	1.0,
 'F':   0.0
}

set_list=[]
my_score=[]

sum_score = 0
my_sum_score=0
for i in range(20):
    subject, score, level = map(str, input().split())
    if level != 'P':
        set_list.append(float(score)*data_set[level])
        my_score.append(float(score))
        pass
    else:
        pass
    pass

for i in range(len(set_list)):
    sum_score += set_list[i]
    my_sum_score += my_score[i]
    pass

if my_sum_score == 0:
    my_sum_score += 1
    pass

print(sum_score/my_sum_score)