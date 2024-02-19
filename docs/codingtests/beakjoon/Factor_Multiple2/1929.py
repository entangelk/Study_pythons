# https://www.acmicpc.net/problem/1929

# 문제
# M이상 N이하의 소수를 모두 출력하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 자연수 M과 N이 빈 칸을 사이에 두고 주어진다. (1 ≤ M ≤ N ≤ 1,000,000) M이상 N이하의 소수가 하나 이상 있는 입력만 주어진다.

# 출력
# 한 줄에 하나씩, 증가하는 순서대로 소수를 출력한다.

def solution(num1,num2):
    answer = []
    flag = False
    for i in range(num1,num2+1):
        if i < 2:
            continue
        flag = True
        for j in range(2,int(i**0.5)+1):
            if i%j == 0:
                flag = False
                break
        if flag:
            answer.append(i)
        pass
    return answer

a,b = map(int, input().split())
answer = solution(a,b)
for i in answer:
    print(i)