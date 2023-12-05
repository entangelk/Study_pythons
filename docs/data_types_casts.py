pass
type("yojulab") # 문자 type
# <class 'str'>

type(199) # 숫자 type
# <class 'int'>

type(1.9999) # 소수 type
# <class 'float'>

a = True
type(a) # T or F bool type
# <class 'bool'>

# cast 불가 경우
mix_val="23k"
int(mix_val)
# Traceback (most recent call last):
#   File "<string>", line 1, in <module>
# ValueError: invalid literal for int() with base 10: '23k'
pass