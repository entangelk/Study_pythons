#list 초기화 방식
list_fruits_primitive = ['melon', 'apple', 'banana','cherry']
tuple_fruits = ('mellon', 'apple', 'banana', 'cherry')
list_fruits_constructor=list(('melon', 'apple', 'banana', 'cherry'))

print(tuple_fruits[0])
pass

# 삭제 대상이 해당 값이 있는 item
list_fruits_constructor.remove('melon')
list_fruits_primitive.remove('apple')
# 삭제 대상이 전체 item
list_fruits_primitive.clear()
# 삭제 대상의 인덱스
list_fruits_primitive.pop(1)