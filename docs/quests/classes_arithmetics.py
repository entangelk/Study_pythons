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
get_num1 = int(input('1번째 숫자를 입력하세요 : '))
get_num2 = int(input('2번째 숫자를 입력하세요 : '))

calculator=Arithmetics(get_num1,get_num2) 
result_plus = calculator.plus()
result_minus = calculator.minus()
result_multiply = calculator.multiply()
result_divide = calculator.divide()
print("덧셈 결과 : {}, 뺄셈 결과 : {}, 곱셈 결과 : {}, 나눗셈 결과 : {}".format(result_plus,result_minus,result_multiply,result_divide))