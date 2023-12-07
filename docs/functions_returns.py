
## 나오는 값 처리
# first = 5
# second = 4
# sum = first + second
def function_name() :
   first = 5
   second = 4
   sum = first + second
   #    return 0
   return sum

# num_sum = 0
print("add() return 결과 : {}".format(function_name()))

# num_first = 4
# num_second = 5
# # 곱셈 연산
# num_first * num_second

# 두 수를 곱해서 결과 return
def multiply() :
    num_first = 4
    num_second = 5
    result = num_first * num_second
    return result

num_multiply = multiply()
print("num_multiply return value : {}".format(num_multiply))

def return_list():
    list_fruits = ['apple', 'banana', 'cherry', 'melon']
    return list_fruits[0]


# 반복 print 작업을 줄이기위한 function 만들기
def score():
  my_score = 90
  if my_score >= 90 : # 90점 이상 : A
      pass
      print("{}은 90점 이상으로 A학점.".format(my_score))
  elif my_score > 80 : # 80점 초과 B
      pass
      print("{}은 80점 초과이므로 B학점.".format(my_score))
  else :  # 나머지 : F
      pass
      print("{}은 80점 이하이므로 F학점.".format(my_score))

