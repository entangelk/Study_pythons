# str_text = "Start, Programming."
# print("{}".format(str_text))
# str_input = input()
# pass


# str_text = "Start, Programming."
# print("{}".format(str_text))
# str_input_desc = "영문이름 입력 : "
# str_input = input("{}".format(str_input_desc))
# pass

# input() 대한 숫자 받아 환산 하기
# 풀기 : 출생년도 입력 받아 나이 계산 (예. 2023(올해) - 2000(출생년도) = 23)


str_text = "Start, Programming."
print("{}".format(str_text))
str_input_desc = "출생년도 입력 : "
num_input_birthyear = input("{}".format(str_input_desc))
num_age = 2023 - int(num_input_birthyear)
print("출생년도 기준 내 나이 계산 : {}살".format(num_age))
pass

multi_val = 3, 5
multi_val
# (3, 5)
num_first, num_second = 3, 5
num_first
# 3
num_second
# 5



#string split()
first, second = "6 8".split()
num_first, num_second = int(first), int(second)
