
str_intro ="확인할 단의 숫자를 입력하세요 : "
print("{}".format(str_intro))
num_get = int(input())

num_count = 0

while num_count < 9:
    num_count += 1
    result = num_get*num_count
    print('{} * {} = {}'.format(num_get, num_count, result)) 