# https://www.acmicpc.net/problem/4948

# 문제
# 베르트랑 공준은 임의의 자연수 n에 대하여, n보다 크고, 2n보다 작거나 같은 소수는 적어도 하나 존재한다는 내용을 담고 있다.

# 이 명제는 조제프 베르트랑이 1845년에 추측했고, 파프누티 체비쇼프가 1850년에 증명했다.

# 예를 들어, 10보다 크고, 20보다 작거나 같은 소수는 4개가 있다. (11, 13, 17, 19) 또, 14보다 크고, 28보다 작거나 같은 소수는 3개가 있다. (17,19, 23)

# 자연수 n이 주어졌을 때, n보다 크고, 2n보다 작거나 같은 소수의 개수를 구하는 프로그램을 작성하시오. 

# 입력
# 입력은 여러 개의 테스트 케이스로 이루어져 있다. 각 케이스는 n을 포함하는 한 줄로 이루어져 있다.

# 입력의 마지막에는 0이 주어진다.

# 출력
# 각 테스트 케이스에 대해서, n보다 크고, 2n보다 작거나 같은 소수의 개수를 출력한다.

# 제한
# 1 ≤ n ≤ 123,456

'''
import sys

def input_str():
    cal_list = []
    while True:
        get_num = int(sys.stdin.readline().strip())
        if get_num != 0:
            cal_list.append(get_num)
        else:
            break
    
    return cal_list

def solution(get_list):
    answer_list = []
    for i in get_list:
        counter = 0
        for j in range(i,i*2+1):
            if j == 2:
                counter +=1
            flag=False
            for k in range(2,int(j**0.5)+1):
                if j%k == 0:
                    flag = False
                    break
                else:
                    flag = True
            if flag:
                counter += 1
        answer_list.append(counter)
    return answer_list
    

get_list = input_str()
answer_list = solution(get_list)
for i in answer_list:
    print(i)
'''

import sys

# 소수를 판별하는 함수
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

# 에라토스테네스의 체를 활용하여 소수를 빠르게 구하는 함수
def primes_up_to_n(n):
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = False
    return [i for i in range(n + 1) if sieve[i]]

# 입력을 여러 개의 테스트 케이스로 받아들이기
def input_str():
    cal_list = []
    while True:
        get_num = int(sys.stdin.readline().strip())
        if get_num != 0:
            cal_list.append(get_num)
        else:
            break
    return cal_list

# 각 테스트 케이스에 대한 소수의 개수 계산
def solution(get_list):
    primes = primes_up_to_n(max(get_list) * 2)
    answer_list = []
    for i in get_list:
        # n을 포함하지 않으므로 1을 빼줌
        answer_list.append(len([prime for prime in primes if i < prime <= 2 * i]))
    return answer_list

get_list = input_str()
answer_list = solution(get_list)
for i in answer_list:
    print(i)
