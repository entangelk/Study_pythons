
intro ="확인할 단의 숫자를 입력하세요 : "
print("{}".format(intro))
getnum = int(input())

i = 0



while i < 9:
    i += 1
    result = getnum*i
    print('{} * {} = {}'.format(getnum, i, result)) 