# https://www.acmicpc.net/problem/2438

# 문제
# 첫째 줄에는 별 1개, 둘째 줄에는 별 2개, N번째 줄에는 별 N개를 찍는 문제

# 입력
# 첫째 줄에 N(1 ≤ N ≤ 100)이 주어진다.

# 출력
# 첫째 줄부터 N번째 줄까지 차례대로 별을 출력한다.
'''
getnum = int(input())

for i in range(getnum):
    print('*'*(i+1))
    pass
'''

def print_star():
    getnum = int(input())

    for i in range(getnum):
        print('*'*(i+1))
        pass
    return

print_star()