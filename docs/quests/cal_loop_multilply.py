# 사용자 입력 곱셈 계산기
# 엔드 조건 = q 입력, q를 입력 시 종료

def calculator(num1,num2):
    if type(num1) == int and type(num2) == int:
        result = num1*num2
        pass
    elif num1=='q' or num2=='q':
        result = '계산기를 종료합니다.' 
        pass
    else :
        result = '입력이 잘못되었습니다. 다시 입력해 주세요'
        pass    
    return result

while True:
    try:
        num1 = int(input("1번째 숫자를 입력하세요 : "))
        num2 = int(input("2번째 숫자를 입력하세요 : "))
        print(calculator(num1,num2))
    except ValueError:
        print("숫자가 아닌 문자를 입력하셨습니다. q를 입력시 종료됩니다.")
        num1 = input(("1번째 숫자를 입력하세요 : "))
        num2 = input(("2번째 숫자를 입력하세요 : "))
        if num1=='q' or num2=='q':
            print(calculator(num1,num2))
            break
        else:
            try:
                int_num1 = int(num1)
                int_num2 = int(num2)
                print(calculator(int_num1,int_num2))
                pass
            except :
                print('두번은 못참아 나가라 넌')
                break
        pass





    