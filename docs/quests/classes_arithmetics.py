class Arithmetics:
    def __init__(self,num1,num2): # 생성자
        self.num1 = num1
        self.num2 = num2
        pass
    def plus(self) : # self 키워드 필요(class 소속 확인용)
        return self.num1+self.num2
    def minus(self):
        return self.num1-self.num2
    def multiply(self):
        return self.num1*self.num2
    def divide(self):
        if self.num2 !=0:
            return self.num1/self.num2
        else :
            error = '0으로는 나눌 수 없습니다.'
            return error
while True:
    try:
        get_num1 = int(input('1번째 숫자를 입력하세요 : '))
        try:
            get_num2 = int(input('2번째 숫자를 입력하세요 : '))
            calculator=Arithmetics(get_num1,get_num2) 
            result_plus = calculator.plus()
            result_minus = calculator.minus()
            result_multiply = calculator.multiply()
            result_divide = calculator.divide()
            print("덧셈 결과 : {}, 뺄셈 결과 : {}, 곱셈 결과 : {}, 나눗셈 결과 : {}".format(result_plus,result_minus,result_multiply,result_divide))
            pass
        except:
            print("숫자를 입력하세요")
        pass
    except:
        print("숫자를 입력하세요")
        pass
           
    print("계속 진행하시려면 Y, 프로그램을 종료하시려면 N을 입력해주세요")
    get_char = input()
    if get_char in ['Y','y']:
        print('프로그램을 계속 진행합니다.')
        pass
    elif get_char in ['N','n']:
        print('프로그램을 종료합니다.')
        break
    else :
        print('잘못된 입력을 하셨습니다. 프로그램을 계속 진행합니다.')
        pass

