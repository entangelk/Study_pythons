# condition이 True 동안 동작
# while True :
#     pass
    
num_virtual = 0

# while 정지 1 case with break문 사용
while True :
    num_virtual += 1
    print("{} = num_virtual+1".format(num_virtual))
    if num_virtual >= 5:
        break
    pass    

num_virtual = 0

# while 정지 2 case without break문
while num_virtual < 5 :
    num_virtual += 1
    print("{} = num_virtual+1".format(num_virtual))
    pass    

# 풀기 : 구구단 5단 결과 매번 출력