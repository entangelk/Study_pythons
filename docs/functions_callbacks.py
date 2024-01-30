# call back function
def add(first, second): # 호출 시 변수에 값이 할당됨
    sum = first + second
    return sum # 상수 대신 변수 사용

def multiply(first, second): # 호출 시 변수에 값이 할당됨
    result = first * second
    return result # 상수 대신 변수 사용

def process_call_function(first, second, callback_function):
    result = process_call_function(first, second)
    return result

if __name__ == '__main__':
    result = process_call_function(5,6,add)
    result = process_call_function(5,6,multiply)


