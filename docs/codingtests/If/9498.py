# https://www.acmicpc.net/problem/9498

# 문제
# 시험 점수를 입력받아 90 ~ 100점은 A, 80 ~ 89점은 B, 70 ~ 79점은 C, 60 ~ 69점은 D, 나머지 점수는 F를 출력하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 시험 점수가 주어진다. 시험 점수는 0보다 크거나 같고, 100보다 작거나 같은 정수이다.

# 출력
# 시험 성적을 출력한다.
'''
a = int(input())

if a >= 90:
    pass
    print('A')
elif a>=80:
    print('B')
    pass
elif a>=70:
    print('C')
    pass
elif a>=60:
    print('D')
    pass
else:
    print('F')
    pass
'''
def level_set():
    if a >= 90:
        result = 'A'
    elif a>=80:
        result ='B'
        pass
    elif a>=70:
        result ='C'
        pass
    elif a>=60:
        result ='D'
        pass
    else:
        result ='F'
        pass
    return result


a = int(input())

level=level_set()
print(level)