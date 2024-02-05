# 같은 폴더에 있는 class 호출
# 1차적인 방법 - 싹다 호출되서 이거 뭐 1개의 클레스에 모든게 있는게 아니면 쓰레기
import classes_formats as cal

calculator = cal.Arithmetics(5,4)
people = cal.person()
result2 = people.add_age()
result = calculator.plus()
print(result,result2)
pass

## import 시 주로 사용하는 방식
from classes_formats import Arithmetics

calculator=Arithmetics(5,4)
result = calculator.plus()
print(result)