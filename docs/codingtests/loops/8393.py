# https://www.acmicpc.net/problem/8393

# 문제
# n이 주어졌을 때, 1부터 n까지 합을 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 n (1 ≤ n ≤ 10,000)이 주어진다.

# 출력
# 1부터 n까지 합을 출력한다.
'''
n = int(input())
d=0

for i in range(n+1):
    d += i
    pass

print(d)
'''

'''
def sumcal():
    d =[]
    for i in range(n):
        d.append(int(i+1))
        pass
    result = sum(d)
    return result

n = int(input())

run=sumcal()
print(run)
'''

def resum():
    n = int(input())
    d =[]
    for i in range(n):
        d.append(int(i+1))
        pass
    result = sum(d)
    print(result)
    return

resum()