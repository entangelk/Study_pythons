# https://school.programmers.co.kr/learn/courses/30/lessons/12901

# 2016년
# 문제 설명
# 2016년 1월 1일은 금요일입니다. 2016년 a월 b일은 무슨 요일일까요? 두 수 a ,b를 입력받아 2016년 a월 b일이 무슨 요일인지 리턴하는 함수, solution을 완성하세요. 요일의 이름은 일요일부터 토요일까지 각각 SUN,MON,TUE,WED,THU,FRI,SAT

# 입니다. 예를 들어 a=5, b=24라면 5월 24일은 화요일이므로 문자열 "TUE"를 반환하세요.

# 제한 조건
# 2016년은 윤년입니다.
# 2016년 a월 b일은 실제로 있는 날입니다. (13월 26일이나 2월 45일같은 날짜는 주어지지 않습니다)
# 입출력 예
# a	b	result
# 5	24	"TUE"

def solution(a, b):
    answer = ''
    data={
        0 : 0,
        1 : 31,
        2 : 29,
        3 : 31,
        4 : 30,
        5 : 31,
        6 : 30,
        7 : 31,
        8 : 31,
        9 : 30,
        10 : 31,
        11 : 30,
        12 : 31
    }
    week_list =['FRI','SAT','SUN','MON','TUE','WED','THU']
    count_date = 0
    
    for i in range(a):
        count_date += data[i]
    count_date += b

    week = count_date%7
    answer = week_list[week-1]

    return answer

solution(1, 1)