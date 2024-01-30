import pandas as pd

# 리스트 컴프리헨션 - 속도에 강점
list_comprehension = [i for i in range(10) if i % 2 == 0]

# 제너레이터 표현식 - 메모리에 강점
generator_expression = (i for i in range(10) if i % 2 == 0)


print(list_comprehension)
print(list(generator_expression))

list_comprehension = [(lambda x:x)(i) for i in range(10) if i % 2 == 0]
print(list_comprehension)

# 각 숫자의 제곱을 계산
numbers = [1, 2, 3, 4, 5]
squared = map(lambda x: x**2, numbers)
print(list(squared))  # [1, 4, 9, 16, 25]

print(list(map((lambda x:x+1),[1,2,3,4,5])))