# https://www.acmicpc.net/problem/4134

# 문제
# 정수 n(0 ≤ n ≤ 4*109)가 주어졌을 때, n보다 크거나 같은 소수 중 가장 작은 소수 찾는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 테스트 케이스의 개수가 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있고, 정수 n이 주어진다.

# 출력
# 각각의 테스트 케이스에 대해서 n보다 크거나 같은 소수 중 가장 작은 소수를 한 줄에 하나씩 출력한다.
import sys
def solution(num):
    get_list = [int(sys.stdin.readline().strip()) for i in range(num)]

    answer_list = []
    for i in get_list:
        if i <= 2:
            answer_list.append(2)
        else:
            if i%2==0:
                i+=1
            j = i
            while True:
                check = True
                for k in range(3,int(j**0.5)+1,2):
                    if j%k == 0:
                        check = False
                        break
                if check:
                    answer_list.append(j)
                    break
                j+=2
    return answer_list

a = int(sys.stdin.readline().strip())
for i in solution(a):
    print(i)