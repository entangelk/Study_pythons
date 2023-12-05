
intro ="확인할 단의 숫자를 입력하세요 : "
print("{}".format(intro))
num_get = int(input())

num_count = 0



while num_count < 9:
    num_count += 1
    result = num_get*i
    print('{} * {} = {}'.format(num_get, num_count, result)) 