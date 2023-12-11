# 1. import : 같은 파일에 있을 경우 생략
# 2. class instance
# 3. call function

# class basic format
class class_name:
    def __init__(self): # 생성자
        pass
    def function_name(self) : # self 키워드 필요(class 소속 확인용)
        pass
        return 0

# 생성자 예시
# 생성자는 클래스를 호출해서 각 변수에 저장해서 다시 호출하는 기능
# 마치 변수에 리스트를 저장하는 느낌? 
'''
class Person:
    def __init__(self, name, age, country):
        self.name = name
        self.age = age
        self.country = country

# Person 클래스의 인스턴스 생성
person1 = Person("Alice", 30, "USA")
person2 = Person("Bob", 25, "Canada")

print(person1.name, person1.age, person1.country)  # 출력: Alice 30 USA
print(person2.name, person2.age, person2.country)  # 출력: Bob 25 Canada
'''

'''
class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return self.num1 + self.num2

    def subtract(self):
        return self.num1 - self.num2

    def multiply(self):
        return self.num1 * self.num2

    def divide(self):
        if self.num2 != 0:
            return self.num1 / self.num2
        else:
            return "0으로는 나눌 수 없습니다."

# Calculator 클래스의 인스턴스 생성
calc = Calculator(10, 5)

# 계산 수행
print("덧셈:", calc.add())        # 출력: 덧셈: 15
print("뺄셈:", calc.subtract())   # 출력: 뺄셈: 5
print("곱셈:", calc.multiply())   # 출력: 곱셈: 50
print("나눗셈:", calc.divide())   # 출력: 나눗셈: 2.0
'''

'''
매직 메서드들은 다양한 용도로 사용되지만, 특히 자주 쓰이는 매직 메서드들이 있습니다. 몇 가지 자주 사용되는 매직 메서드를 살펴보겠습니다:

__init__: 객체의 초기화를 담당하는 생성자 메서드입니다. 객체가 생성될 때 자동으로 호출됩니다.

__str__ 및 __repr__: 객체의 문자열 표현을 반환하는 메서드입니다. __str__은 사용자가 보기 쉬운 형태의 문자열을 반환하고, __repr__은 객체를 재생성할 수 있는 형태의 문자열을 반환합니다.

__len__: 객체의 길이를 반환하는 메서드입니다. 주로 시퀀스나 컨테이너 클래스에서 사용됩니다.

__getitem__ 및 __setitem__: 객체의 인덱싱과 슬라이싱을 처리하는 메서드입니다. 컬렉션과 같은 객체에서 요소를 가져오거나 설정하는 데 사용됩니다.

__iter__ 및 __next__: 이터레이터 프로토콜을 구현하는 메서드입니다. 컬렉션의 요소를 반복적으로 순회하거나 다룰 때 사용됩니다.

__eq__, __ne__, __lt__, __le__, __gt__, __ge__: 객체 간의 비교 연산을 처리하는 메서드들입니다. __eq__는 등호(==) 비교에, 다른 비교 연산자들은 각각의 연산에 사용됩니다.

__add__, __sub__, __mul__, __truediv__ 등: 연산자 오버로딩을 지원하기 위한 메서드들로, 객체 간의 산술 연산을 정의합니다.

__enter__ 및 __exit__: 컨텍스트 관리 프로토콜을 구현하는 메서드로, with 문과 함께 사용될 때 객체가 할당되고 해제되는 방법을 정의합니다.

이러한 매직 메서드들은 파이썬의 강력한 기능 중 하나로, 클래스의 행동을 커스터마이징하고 특별한 동작을 추가하는 데 유용하게 사용됩니다. 클래스를 정의할 때 이러한 매직 메서드들을 적절히 오버라이드하여 객체의 행동을 원하는 대로 조작할 수 있습니다.
'''

class person:
    def add_age(self) :
        print("45세")
        pass
        return 0
    
# 1. import : 같은 파일에 있을 경우 생략
# 2. class instance
Person = person()
# 3. call function
Person.add_age()


class Arithmetics:
    def __init__(self,num1,num2): # 생성자
        self.num1 = num1
        self.num2 = num2
        pass
    def plus(self) : # self 키워드 필요(class 소속 확인용)
        return self.num1+self.num2
    def minus(self):
        return self.num1-self.num2

calculator=Arithmetics(2,3) 
result = calculator.plus()
print(result)