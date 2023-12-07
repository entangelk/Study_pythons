# 기본 if 구문
if True:
    pass

# 문자 비교
str_name = "yoju lab"
str_name == "yoju lab"

# 문자 비교
str_name = "yoju lab"

# 문자에 긍정으로 질문
if str_name == "yoju lab":
    pass
    print("name is {}.".format(str_name))

# 문자에 대한 부정으로 질문
if str_name != "yoju lab":
    pass
    print("name is {}.".format(str_name))

# if - else
# num_first >= 4 -> True : 큼, False : 작음
num_first = 5
if num_first >=4 : # 무조건 둘 중 하나 표현
    pass    # condition이 True
    print("{}는 4보다 크다.".format(num_first))
else : 
    pass    # condition이 False
    print("{}는 4보다 작다.".format(num_first))


# if - elif - else
# 점수에 따른 표시
# 90점 이상 : A, 80점 초과 : B, 나머지 : F
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


print('End Program!')