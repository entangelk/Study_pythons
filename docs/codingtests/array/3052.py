# https://www.acmicpc.net/problem/3052

# 문제
# 두 자연수 A와 B가 있을 때, A%B는 A를 B로 나눈 나머지 이다. 예를 들어, 7, 14, 27, 38을 3으로 나눈 나머지는 1, 2, 0, 2이다. 

# 수 10개를 입력받은 뒤, 이를 42로 나눈 나머지를 구한다. 그 다음 서로 다른 값이 몇 개 있는지 출력하는 프로그램을 작성하시오.

# 입력
# 첫째 줄부터 열번째 줄 까지 숫자가 한 줄에 하나씩 주어진다. 이 숫자는 1,000보다 작거나 같고, 음이 아닌 정수이다.

# 출력
# 첫째 줄에, 42로 나누었을 때, 서로 다른 나머지가 몇 개 있는지 출력한다.

get_list=[]
count_list=[]
for i in range(10):
    get_list.append(int(input())%42)
    count_list.append(0)
    pass
copy_list=get_list.copy()
copy_list.reverse()
print(get_list)
print(copy_list)

for i in range(10):
    for j in range(9):
        if get_list[i] == copy_list[9-j]:
            get_list[i] = 50
            pass

print(get_list)

"""
for j in range(10):
    for k in range(10):
        for l in range(9):
            try:
                if get_list[j+k] == copy_list[j+k+l+1]:
                    copy_list[j+k] = 43
                    print(copy_list)
                    pass
            except:
                print(copy_list)
"""
