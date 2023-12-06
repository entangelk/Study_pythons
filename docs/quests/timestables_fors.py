str_intro ="확인할 단의 숫자를 입력하세요 : "
print("{}".format(str_intro))
num_get = int(input())

for num_count in range(9):
    print("{} * {} = {}".format(num_get, num_count+1, (num_get)*(num_count+1)))
