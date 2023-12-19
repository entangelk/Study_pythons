# function에 들어가는 값들

def add(first, second):
    sum = first + second
    #return 0
    return sum

if __name__=="__main__":
  num_sum=add(5,4)
  print(num_sum)


# 반복 print 작업을 줄이기위한 function 만들기
def return_grade(my_score):     # 자신을 불렀을 때 값들 할당
  my_grade = ''
  if my_score >= 90 : # 90점 이상 : A
    my_grade='A'
  elif my_score > 80 : # 80점 초과 B
    my_grade='B'
  else :  # 나머지 : F
    my_grade='C'
    return my_grade
  


if __name__ == "__main__": # 테스트 용으로 사용하는 기능 (임포트시에는 if문에 안걸리니까 작동이 안됨 -> 내 코드내에서의 테스트)
  # str_grade = return_grade(99) #호출 시 값들이 넘어감(순서 매칭)
  my_score = 88
  str_grade = return_grade()
  print("당신의 학점 : {}.".format(str_grade))