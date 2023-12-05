#input : 몸무게, 키 (정수)
# BMI = 몸무게(kg) / 키(m)^2
# BMI 분류

# 18 미만 : 저체중
# 18 ~ 22 : 정상
# 23 ~ 24 : 과체중
# 25 이상 : 비만

intro1="몸무게를 입력하세요(kg단위) :"
intro2="키를 입력하세요(m단위) : "
#몸무게 입력
print("{}".format(intro1))
weight= float(input())

#키 입력
print("{}".format(intro2))
hight= float(input())

#bmi 계산공식
exbmi = (weight) / (hight**2)

if exbmi >= 25:
    print("BMI 수치는 {}로 비만입니다.".format(int(exbmi)))
    pass
elif exbmi >= 23:
    print("BMI 수치는 {}로 과체중입니다.".format(int(exbmi)))
    pass
elif exbmi >= 18:
    print("BMI 수치는 {}로 정상입니다.".format(int(exbmi)))
    pass
else :
    print("BMI 수치는 {}로 저체중입니다.".format(int(exbmi)))
    pass

