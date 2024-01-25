# https://www.acmicpc.net/problem/1934

# 문제
# 두 자연수 A와 B에 대해서, A의 배수이면서 B의 배수인 자연수를 A와 B의 공배수라고 한다. 이런 공배수 중에서 가장 작은 수를 최소공배수라고 한다. 예를 들어, 6과 15의 공배수는 30, 60, 90등이 있으며, 최소 공배수는 30이다.

# 두 자연수 A와 B가 주어졌을 때, A와 B의 최소공배수를 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 테스트 케이스의 개수 T(1 ≤ T ≤ 1,000)가 주어진다. 둘째 줄부터 T개의 줄에 걸쳐서 A와 B가 주어진다. (1 ≤ A, B ≤ 45,000)

# 출력
# 첫째 줄부터 T개의 줄에 A와 B의 최소공배수를 입력받은 순서대로 한 줄에 하나씩 출력한다.

def solution():
    answer_pri_dic = {}
    answer_sec_dic = {}
    a,b = map(int, input().split())
    '''
    while True:
        if a == 1:
            break
        i = 1
        while True:
            i+=1
            if a%i==0:
                a /=i
                answer_pri_dic[i]= answer_pri_dic.get(i,0)+1
                break

    
    while True:
        if b == 1:
            break
        i = 1
        while True:
            i+=1
            if b%i==0:
                b /=i
                answer_sec_dic[i]= answer_sec_dic.get(i,0)+1
                break
    '''

    i = 2
    while i * i <= a:
        if a % i:
            i += 1
        else:
            a //= i
            answer_pri_dic[i]= answer_pri_dic.get(i, 0) + 1
    if a > 1:
        answer_pri_dic[a] = answer_pri_dic.get(a, 0) + 1
    
    i = 2
    while i * i <= b:
        if b % i:
            i += 1
        else:
            b //= i
            answer_sec_dic[i]= answer_sec_dic.get(i, 0) + 1
    if b > 1:
        answer_sec_dic[b] = answer_sec_dic.get(b, 0) + 1

    return answer_pri_dic,answer_sec_dic


def solution_print(dic1,dic2):
    for k,v in dic1.items():
        if dic2.get(k,False):
            if v >= dic2[k]:
                dic2[k] = dic1[k]
        else:
            dic2[k] = v

    answer = 1    
    for k,v in dic2.items():
        answer *= k**v

    return answer

a = int(input())
for i in range(a):
    sol_pri_dic,sol_sec_dic = solution()
    print(solution_print(sol_pri_dic,sol_sec_dic))