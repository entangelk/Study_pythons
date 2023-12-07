# 가로 * 세로 * 높이 = 직육면체
# 입력 : 가로 세로 높이
# 출력 : 가로 세로 높이 = 직육면체

#방법 1 - sys readline 이용 (백준에서 필요한 인풋 기능)
import sys
frchar = "가로 세로 높이를 스페이스를 구분으로 입력하세요 : "

print("{}".format(frchar))
num_ver, num_hor, num_high = map(int, sys.stdin.readline().split())

# 출력 with 계산
print("가로 {}m * 세로 {}m * 높이 {}m = 직육면체 {}m^3".format(num_ver, num_hor, num_high, (num_ver*num_hor*num_high)))


#방법 2 - 일반 input 이용

# 문자열 스플릿으로 입력
print("{}".format(frchar))
str_ver, str_hor, str_high = input().split()

# 문자 -> int 변환
num_ver = int(str_ver)
num_hor = int(str_hor)
num_high = int(str_high)

# 출력 with 계산
print("가로 {}m * 세로 {}m * 높이 {}m = 직육면체 {}m^3".format(num_ver, num_hor, num_high, (num_ver*num_hor*num_high)))