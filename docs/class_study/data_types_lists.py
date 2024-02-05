numeric_first = 0
numeric_second = 1
numeric_third = 2
numeric_fourth = 3
numeric_fifth = 4

# 사용 이유 : 값들에 모임을 쉽게 전달
# 숫자 5개 값들로 이루어진 리스트
list_numerics = [0, 1, 2, 3, 4]

# 문자열 3개 값들로 이루어진 리스트
list_fruits = ['apple', 'banana', 'cherry']

# 숫자와 문자 섞은 리스트
list_mixs = [0, 'banana',4,'cherry']

len(list_numerics)
# 5

len(list_mixs)
# 6

## for문 활용 후 다시 오기

# index(색인, 위치값)
list_fruits = ['apple', 'banana', 'cherry', 'melon']
## index로 값 가져오기
list_fruits[0]      # 단일 변수로 여김
#'apple'
list_fruits[3]
#'melon'

# list_fruits[4]
# Traceback (most recent call last):
# File "<string>", line 1, in <module>
# IndexError: list index out of range

pass